from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class ArgentinaNames:
    name: str
    count: int
    year: int
    gender: str = None
    county: str = 'Argentina'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender}, {self.county}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.county]
