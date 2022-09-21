from dataclasses import dataclass


'''A module that contains all the name classes for each dataset'''


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
    name: str
    count: int
    year: int
    gender: str = 'M'
    country: str = 'Spain'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender}, {self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]


@dataclass(init=True, frozen=True)
class SpainFemaleNames:
    name: str
    count: int
    year: int
    gender: str = 'F'
    country: str = 'Spain'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender}, {self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]


@dataclass(init=True)
class ChileMaleNames:
    name: str
    percent: float
    totals: int
    year: int
    count: int = 0
    gender: str = 'M'
    country: str = 'Chile'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender} ,{self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]

    def update_count(self):
        self.count = round((self.percent * self.totals) / 100)


@dataclass(init=True)
class ChileFemaleNames:
    name: str
    percent: float
    totals: int
    year: int
    count: int = 0
    gender: str = 'F'
    country: str = 'Chile'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender} ,{self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]

    def update_count(self):
        self.count = round((self.percent * self.totals) / 100)


@dataclass(init=True, frozen=True)
class UsaMaleNames:
    name: str
    count: int
    year: int
    gender: str = 'M'
    country: str = 'USA'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender} ,{self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]


@dataclass(init=True, frozen=True)
class UsaFemaleNames:
    name: str
    count: int
    year: int
    gender: str = 'F'
    country: str = 'USA'

    def __str__(self) -> str:
        return f"{self.name}, {self.count}, {self.year}, {self.gender} ,{self.country}"

    def as_array(self):
        return [self.name, self.count, self.year, self.gender, self.country]