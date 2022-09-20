from dataclasses import dataclass
from bs4 import BeautifulSoup


class UsaFilesData:
    def __init__(self, file_path, file_year):
        self.file_path = file_path
        self.file_year = file_year

    def extract_data(self):
        '''Extract td for each html file located at self.file_path'''

        with open(self.file_path, 'r', encoding="iso-8859-1") as file:
            soup = BeautifulSoup(file, "html.parser")
            tables = [
                [
                    [td.get_text(strip=True) for td in tr.find_all('td')]
                    for tr in table.find_all('tr')
                ]
                for table in soup.find_all('table')
            ]

            '''The data we need is on tables[2], checks for rows that have 5 objects in it (rank, male name, male count, female name, female count)'''
            main_data = []
            for item in tables[2]:
                if len(item) == 5:
                    '''we only want to append male name, male count, female name, female count and file year'''
                    new_row = [item[1], item[2],
                               item[3], item[4], self.file_year]
                    main_data.append(new_row)
            return main_data


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
