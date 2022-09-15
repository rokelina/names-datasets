from dataclasses import dataclass

'''A set of classes to store female and male names'''


@dataclass(init=True, frozen=True)
class MaleNames:
    male_name: str
    male_count: int
    male_year: int
    male_gender: str = 'M'
    male_country: str = 'Spain'

    def __str__(self) -> str:
        return f"{self.male_name}, {self.male_count}, {self.male_year}, {self.male_gender}, {self.male_country}"


@dataclass(init=True, frozen=True)
class FemaleNames:
    fem_name: str
    fem_count: int
    fem_year: int
    fem_gender: str = 'F'
    fem_country: str = 'Spain'
