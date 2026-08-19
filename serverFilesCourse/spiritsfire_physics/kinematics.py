from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantAccelerationCase:
    initial_velocity: int
    final_velocity: int
    elapsed_time: int

    @property
    def velocity_change(self):
        return self.final_velocity - self.initial_velocity

    @property
    def acceleration(self):
        return self.velocity_change / self.elapsed_time

    def params(self):
        return {
            "vi": self.initial_velocity,
            "vf": self.final_velocity,
            "dt": self.elapsed_time,
            "delta_v": self.velocity_change,
            "acceleration": round(self.acceleration, 4),
        }

    def answers(self):
        return {
            "delta_v": self.velocity_change,
            "acceleration": self.acceleration,
        }


def acceleration_case(rng, level):
    """Generate a constrained case; every scaffold level uses this physics model."""
    if level == "guided":
        initial = rng.randint(2, 14)
        change = rng.randint(6, 20)
        elapsed = rng.randint(2, 8)
    elif level == "partial":
        initial = rng.randint(8, 26)
        changes = [value for value in range(-16, 17) if abs(value) >= 5 and initial + value >= 1]
        change = rng.choice(changes)
        elapsed = rng.randint(2, 9)
    elif level == "independent":
        initial = 0
        change = rng.randint(40, 100)
        elapsed = rng.randint(10, 35)
    else:
        raise ValueError(f"Unknown acceleration scaffold level: {level}")
    return ConstantAccelerationCase(initial, initial + change, elapsed)
