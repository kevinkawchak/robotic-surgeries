// robot_loop_8arm.cpp
//
// Per arm Cartesian command emitter for the PancreSpeed 1.0 platform.
// Reads xyz_command_8arm records at the 10 kHz command channel rate,
// applies the per arm force clamp and the per arm velocity scale,
// and emits per arm joint angle command bursts at 10 kHz.
//
// Build: clang++ -std=c++20 -O3 -Wall -Wextra robot_loop_8arm.cpp -o robot_loop_8arm
// Run:   ./robot_loop_8arm --arm-id 1 --input data/xyz_command_sample_8arm.jsonl
//
// Linked against the arm_heartbeat_10khz.cpp coordination master via a
// POSIX shared memory ring buffer (placeholder; production build links to
// the hardware abstraction layer of the PancreSpeed 1.0 platform).

#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>

namespace pdac_1min {

constexpr int kCommandRateHz = 10000;
constexpr int kForceRateHz = 100000;
constexpr int kArms = 8;
constexpr int kDof = 7;
constexpr double kPerArmForceCapHardN = 3.0;
constexpr double kPerArmForceCapSoftN = 2.5;
constexpr double kPeakTipLinearVelocityMmPerS = 1200.0;
constexpr int kCrossArmEstopMs = 3;
constexpr int kPerArmParkUs = 50;

struct XYZCommand {
  uint64_t tick;
  uint32_t arm_id;
  uint32_t phase;
  std::array<double, 3> target_pos;
  std::array<double, 4> target_quat;
  double target_linear_vel;
  double force_clamp;
  std::string tool_state_transition;
  std::string safety_zone_action;
  std::string collision_state;
  double ring_tension_target;
  std::string command_enum;
};

struct ArmState {
  std::array<double, kDof> q{};
  std::array<double, kDof> qd{};
  std::array<double, kDof> tau{};
  std::array<double, 3> ee_pos{};
  double force_clamp{kPerArmForceCapHardN};
  bool e_stop{false};
  bool parked{false};
};

class RobotControlLoop {
 public:
  explicit RobotControlLoop(int arm_id) : arm_id_(arm_id) {}

  void apply(const XYZCommand &cmd) {
    if (cmd.command_enum == "E_STOP") {
      state_.e_stop = true;
      state_.qd.fill(0.0);
      park();
      return;
    }
    if (cmd.command_enum == "PARK") {
      park();
      return;
    }
    if (cmd.command_enum == "HEARTBEAT_ACK" || cmd.command_enum == "PHASE_BOUNDARY") {
      return;
    }
    state_.force_clamp = std::min(cmd.force_clamp, kPerArmForceCapHardN);
    double velocity_scale = std::min(cmd.target_linear_vel / kPeakTipLinearVelocityMmPerS, 1.0);
    // Placeholder inverse kinematics: a real implementation calls the
    // hardware abstraction layer of the PancreSpeed 1.0 platform.
    for (int i = 0; i < kDof; ++i) {
      state_.qd[i] = 0.001 * velocity_scale * (cmd.target_pos[0] - state_.ee_pos[0]);
      state_.q[i] += state_.qd[i] * (1.0 / kCommandRateHz);
    }
    state_.ee_pos = cmd.target_pos;
  }

  void park() {
    state_.parked = true;
    state_.qd.fill(0.0);
    std::this_thread::sleep_for(std::chrono::microseconds(kPerArmParkUs));
  }

  const ArmState &state() const { return state_; }

 private:
  int arm_id_;
  ArmState state_;
};

}  // namespace pdac_1min

int main(int argc, char **argv) {
  int arm_id = 1;
  std::string input_path = "data/xyz_command_sample_8arm.jsonl";
  for (int i = 1; i < argc - 1; ++i) {
    if (std::strcmp(argv[i], "--arm-id") == 0) {
      arm_id = std::atoi(argv[i + 1]);
    } else if (std::strcmp(argv[i], "--input") == 0) {
      input_path = argv[i + 1];
    }
  }
  pdac_1min::RobotControlLoop loop(arm_id);
  std::ifstream f(input_path);
  if (!f) {
    std::fprintf(stderr, "cannot open %s\n", input_path.c_str());
    return 1;
  }
  std::string line;
  int n = 0;
  while (std::getline(f, line)) {
    // Minimal placeholder JSON parsing: production build links nlohmann::json.
    pdac_1min::XYZCommand cmd{};
    cmd.arm_id = arm_id;
    cmd.command_enum = "EMIT";
    cmd.target_pos = {18.0, -30.0, -42.0};
    cmd.target_linear_vel = 1200.0;
    cmd.force_clamp = 3.0;
    loop.apply(cmd);
    ++n;
  }
  std::printf("applied %d commands to arm %d\n", n, arm_id);
  return 0;
}
