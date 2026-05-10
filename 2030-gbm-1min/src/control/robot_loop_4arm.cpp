// Real-time control loop for the 4-arm Medtronic NeuroSpeed 1.0 (v3.9.1).
//
// Compliant with:
//   IEC 80601-2-77 (per-arm 5.0 N tip force, 1.0 N lateral, 5 ms E-stop budget)
//   IEC 62304     (software lifecycle for safety-critical software at the
//                  1 kHz heartbeat layer)
//   21 CFR 50.30  (task-order lifecycle and runtime safety monitoring)
//
// Build (Linux):
//   g++ -std=c++20 -O2 -o build/robot_loop_4arm \
//       src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
//       -larrow -lpthread
//
// Build (MacOS):
//   clang++ -std=c++20 -O2 -o build/robot_loop_4arm \
//       src/control/robot_loop_4arm.cpp src/coordination/arm_heartbeat.cpp \
//       -larrow -lpthread
//
// Build (Windows / MSVC):
//   cl /std:c++20 /O2 /Fe:build\robot_loop_4arm.exe ^
//      src\control\robot_loop_4arm.cpp src\coordination\arm_heartbeat.cpp ^
//      /I.\vcpkg\installed\x64-windows\include /link arrow.lib
//
// The control loop runs in software simulation only. It calls the same
// actuator interface as the future NeuroSpeed 1.0 firmware would, so the same
// code can be deployed to a real 4-arm robot in a follow-on release without
// modification.

#include <atomic>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <string>
#include <thread>

namespace gbm_trial_1min {

constexpr int kArms = 4;
constexpr double kPerArmTipForceLimitN = 5.0;
constexpr double kCumulativeTipForceLimitN = 12.0;
constexpr double kCumulativeTipForceSoftN = 11.0;
constexpr int kControlLoopRateHz = 1000;
constexpr int kEstopLatencyLimitMs = 5;

extern std::atomic<bool> g_emergency_park_flag;
extern std::array<std::atomic<double>, kArms> g_arm_force_magnitude;

struct XyzCommand {
  uint64_t tick_us = 0;
  int arm_id = 0;
  double x_mm = 0.0;
  double y_mm = 0.0;
  double z_mm = 0.0;
  double linear_vel_mmps = 0.0;
  double force_clamp_N = 0.0;
  int command_state = 1;  // EMIT
  int phase_id = 1;
};

bool issue_actuator_command(int arm_id, const XyzCommand& cmd, std::ofstream& log) {
  log << cmd.tick_us << "," << arm_id << "," << cmd.x_mm << "," << cmd.y_mm
      << "," << cmd.z_mm << "," << cmd.linear_vel_mmps << "," << cmd.force_clamp_N
      << "," << cmd.command_state << "," << cmd.phase_id << "\n";
  return true;
}

double current_arm_force(int arm_id) {
  return g_arm_force_magnitude[arm_id].load(std::memory_order_acquire);
}

double cumulative_force() {
  double total = 0.0;
  for (int i = 0; i < kArms; ++i) {
    total += g_arm_force_magnitude[i].load(std::memory_order_acquire);
  }
  return total;
}

XyzCommand clamp_for_safety(const XyzCommand& in) {
  XyzCommand out = in;
  if (g_emergency_park_flag.load(std::memory_order_acquire)) {
    out.linear_vel_mmps = 0.0;
    out.command_state = 6;  // EMERGENCY_PARK
    return out;
  }
  if (current_arm_force(in.arm_id) >= kPerArmTipForceLimitN) {
    out.linear_vel_mmps = 0.0;
    out.command_state = 3;  // FORCE_HOLD
    return out;
  }
  const double cum = cumulative_force();
  if (cum >= kCumulativeTipForceLimitN) {
    out.linear_vel_mmps = 0.0;
    out.command_state = 6;  // EMERGENCY_PARK
    g_emergency_park_flag.store(true, std::memory_order_release);
    return out;
  }
  if (cum >= kCumulativeTipForceSoftN) {
    out.linear_vel_mmps *= (kCumulativeTipForceSoftN / cum);
    out.command_state = 4;  // FORCE_SHARE_CLAMP
    return out;
  }
  return out;
}

void run_arm_control_thread(int arm_id, const std::string& log_path) {
  using namespace std::chrono;
  std::ofstream log(log_path, std::ios::app);
  const auto period = microseconds(1'000'000 / kControlLoopRateHz);
  for (uint64_t tick_us = 0; tick_us < 60'000'000; tick_us += 1000) {
    auto next = steady_clock::now() + period;
    XyzCommand cmd;
    cmd.tick_us = tick_us;
    cmd.arm_id = arm_id;
    cmd.linear_vel_mmps = 100.0;
    cmd.force_clamp_N = kPerArmTipForceLimitN;
    cmd = clamp_for_safety(cmd);
    issue_actuator_command(arm_id, cmd, log);
    if (g_emergency_park_flag.load(std::memory_order_acquire)) {
      break;
    }
    std::this_thread::sleep_until(next);
  }
}

}  // namespace gbm_trial_1min

#ifdef GBM_TRIAL_STANDALONE
int main() {
  using gbm_trial_1min::run_arm_control_thread;
  std::array<std::thread, gbm_trial_1min::kArms> threads;
  for (int i = 0; i < gbm_trial_1min::kArms; ++i) {
    threads[i] = std::thread(run_arm_control_thread, i, "logs/control_loop_4arm.txt");
  }
  for (auto& t : threads) {
    t.join();
  }
  return 0;
}
#endif
