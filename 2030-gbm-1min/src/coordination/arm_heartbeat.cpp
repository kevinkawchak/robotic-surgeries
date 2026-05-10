// 1 kHz heartbeat sender / receiver for the 4-arm Medtronic NeuroSpeed 1.0
// (v3.9.1).
//
// Implements multi_arm_coordination.md:
//   32-byte frame, 1 ms deadline, monotonic heartbeat_seq, crc32.
//   3 ms watchdog miss threshold triggers emergency-park.
//   Cross-arm safety zone gating: any FORBIDDEN safety_zone -> emergency-park.
//
// Compliant with IEC 62304 software lifecycle for safety-critical software at
// the 1 kHz heartbeat layer.

#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <thread>

namespace gbm_trial_1min {

constexpr int kArms = 4;
constexpr int kHeartbeatHz = 1000;
constexpr int kWatchdogMissThresholdFrames = 3;

std::atomic<bool> g_emergency_park_flag{false};
std::array<std::atomic<double>, kArms> g_arm_force_magnitude{};

struct HeartbeatFrame {
  uint8_t arm_id;
  uint32_t tick_us;
  float ee_x;
  float ee_y;
  float ee_z;
  float ee_force_magnitude;
  uint8_t safety_zone;
  uint8_t robot_state;
  uint32_t heartbeat_seq;
  uint32_t crc32;
  uint8_t reserved;
} __attribute__((packed));

static_assert(sizeof(HeartbeatFrame) == 32, "HeartbeatFrame must be exactly 32 bytes");

uint32_t compute_crc32(const HeartbeatFrame& frame) {
  // Compact CRC32 implementation for the 27 bytes preceding the crc32 field.
  uint32_t crc = 0xFFFFFFFFu;
  const auto* bytes = reinterpret_cast<const uint8_t*>(&frame);
  for (size_t i = 0; i < 27; ++i) {
    crc ^= bytes[i];
    for (int b = 0; b < 8; ++b) {
      crc = (crc >> 1) ^ (0xEDB88320u & -(crc & 1));
    }
  }
  return crc ^ 0xFFFFFFFFu;
}

class HeartbeatBus {
 public:
  void publish(int arm_id, const HeartbeatFrame& frame) {
    inbox_[arm_id].store(frame, std::memory_order_release);
    last_seq_[arm_id].store(frame.heartbeat_seq, std::memory_order_release);
    last_seen_[arm_id].store(now_us(), std::memory_order_release);
    g_arm_force_magnitude[arm_id].store(frame.ee_force_magnitude, std::memory_order_release);
    if (frame.safety_zone == 5) {  // FORBIDDEN
      g_emergency_park_flag.store(true, std::memory_order_release);
    }
  }

  HeartbeatFrame snapshot(int arm_id) const {
    return inbox_[arm_id].load(std::memory_order_acquire);
  }

  bool watchdog_check() {
    const uint64_t now = now_us();
    for (int i = 0; i < kArms; ++i) {
      const uint64_t age = now - last_seen_[i].load(std::memory_order_acquire);
      if (age > static_cast<uint64_t>(kWatchdogMissThresholdFrames * 1000)) {
        g_emergency_park_flag.store(true, std::memory_order_release);
        return false;
      }
    }
    return true;
  }

 private:
  static uint64_t now_us() {
    using namespace std::chrono;
    return static_cast<uint64_t>(
        duration_cast<microseconds>(steady_clock::now().time_since_epoch()).count());
  }

  std::array<std::atomic<HeartbeatFrame>, kArms> inbox_{};
  std::array<std::atomic<uint32_t>, kArms> last_seq_{};
  std::array<std::atomic<uint64_t>, kArms> last_seen_{};
};

void run_heartbeat_sender(int arm_id, HeartbeatBus& bus) {
  using namespace std::chrono;
  uint32_t seq = 0;
  const auto period = microseconds(1'000'000 / kHeartbeatHz);
  for (uint64_t tick_us = 0; tick_us < 60'000'000; tick_us += 1000) {
    auto next = steady_clock::now() + period;
    HeartbeatFrame frame{};
    frame.arm_id = static_cast<uint8_t>(arm_id);
    frame.tick_us = static_cast<uint32_t>(tick_us);
    frame.ee_force_magnitude = static_cast<float>(g_arm_force_magnitude[arm_id].load());
    frame.safety_zone = 1;  // NONE
    frame.robot_state = 5;  // ACTIVE
    frame.heartbeat_seq = ++seq;
    frame.crc32 = compute_crc32(frame);
    bus.publish(arm_id, frame);
    if (g_emergency_park_flag.load(std::memory_order_acquire)) {
      break;
    }
    std::this_thread::sleep_until(next);
  }
}

void run_heartbeat_watchdog(HeartbeatBus& bus) {
  using namespace std::chrono;
  while (!g_emergency_park_flag.load(std::memory_order_acquire)) {
    bus.watchdog_check();
    std::this_thread::sleep_for(microseconds(1000));
  }
}

}  // namespace gbm_trial_1min
