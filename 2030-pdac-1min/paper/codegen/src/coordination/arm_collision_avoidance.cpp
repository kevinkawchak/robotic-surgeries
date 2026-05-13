// arm_collision_avoidance.cpp
//
// Per arm collision avoidance state machine. Reads the per arm tip position
// from the coordination master, computes the nearest neighbor distance, and
// emits a 4 state finite state machine output (clear / proximity / contact /
// unsafe). Output is consumed by the per arm robot control loop and the
// safety zone gate.
//
// Build: clang++ -std=c++20 -O3 -Wall -Wextra arm_collision_avoidance.cpp -o arm_collision_avoidance

#include <array>
#include <cmath>
#include <cstdint>
#include <cstdio>

namespace pdac_1min {

constexpr int kArms = 8;

enum class CollisionState : uint8_t {
  kClear = 0,
  kProximity = 1,
  kContact = 2,
  kUnsafe = 3,
};

struct ArmTipPosition {
  double x;
  double y;
  double z;
};

static CollisionState classify(double distance_mm) {
  if (distance_mm > 30.0) return CollisionState::kClear;
  if (distance_mm > 15.0) return CollisionState::kProximity;
  if (distance_mm > 5.0) return CollisionState::kContact;
  return CollisionState::kUnsafe;
}

static double distance(const ArmTipPosition &a, const ArmTipPosition &b) {
  double dx = a.x - b.x;
  double dy = a.y - b.y;
  double dz = a.z - b.z;
  return std::sqrt(dx * dx + dy * dy + dz * dz);
}

std::array<CollisionState, kArms> compute_states(
    const std::array<ArmTipPosition, kArms> &positions) {
  std::array<CollisionState, kArms> states{};
  for (int i = 0; i < kArms; ++i) {
    double nearest = 1e9;
    for (int j = 0; j < kArms; ++j) {
      if (i == j) continue;
      double d = distance(positions[i], positions[j]);
      if (d < nearest) nearest = d;
    }
    states[i] = classify(nearest);
  }
  return states;
}

}  // namespace pdac_1min

int main() {
  std::array<pdac_1min::ArmTipPosition, pdac_1min::kArms> positions = {{
      {18.0, -30.0, -42.0},
      {18.5, -30.5, -42.0},
      {22.0, -35.0, -45.0},
      {18.0, -30.0, -42.0},
      {18.0, -30.0, -42.0},
      {15.0, -30.0, -40.0},
      {12.0, -30.0, -38.0},
      {10.0, -30.0, -36.0},
  }};
  auto states = pdac_1min::compute_states(positions);
  for (int i = 0; i < pdac_1min::kArms; ++i) {
    std::printf("arm %d collision_state %d\n", i + 1, static_cast<int>(states[i]));
  }
  return 0;
}
