from dataclasses import dataclass


'''A module that contains all the name classes'''


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


@dataclass(init=True, frozen=True)
class ItalyNames:
    name: str
    count: int
    year: int
    gender: str = None
    county: str = 'Italy'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender}, {self.county}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.county]


@dataclass(init=True, frozen=True)
class SpainMaleNames:
    male_name: str
    male_count: int
    male_year: int
    male_gender: str = 'M'
    male_country: str = 'Spain'

    def __str__(self) -> str:
        return f"{self.male_name}, {self.male_count}, {self.male_year}, {self.male_gender}, {self.male_country}"

    def as_array(self):
        return [self.male_name, self.male_count, self.male_year, self.male_gender, self.male_country]


@dataclass(init=True, frozen=True)
class SpainFemaleNames:
    fem_name: str
    fem_count: int
    fem_year: int
    fem_gender: str = 'F'
    fem_country: str = 'Spain'

    def __str__(self) -> str:
        return f"{self.fem_name}, {self.fem_count}, {self.fem_year}, {self.fem_gender}, {self.fem_country}"

    def as_array(self):
        return [self.fem_name, self.fem_count, self.fem_year, self.fem_gender, self.fem_country]
