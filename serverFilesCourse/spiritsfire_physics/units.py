from dataclasses import dataclass


@dataclass(frozen=True)
class Conversion:
    value: float
    source_unit: str
    target_unit: str
    multiplier: float

    @property
    def result(self):
        return self.value * self.multiplier


def conversion(value, source_unit, target_unit, multiplier):
    if value <= 0 or multiplier <= 0 or source_unit == target_unit:
        raise ValueError("conversion must use positive values and distinct units")
    return Conversion(value, source_unit, target_unit, multiplier)
