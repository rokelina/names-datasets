from bs4 import BeautifulSoup
import os
import csv
from typing import List

'''Define class Row that will hold all female names and male names data'''


class Row:
    def __init__(self, rank, male_name, male_count, fem_name, fem_count, file_year):
        self.rank = int(rank)
        self.male_name = male_name
        self.male_count = int(male_count.replace(',', ''))
        self.fem_name = fem_name
        self.fem_count = int(fem_count.replace(',', ''))
        self.file_year = file_year
        self.country = 'USA'

    def print_row(self):
        print(
            f"{self.rank}, {self.male_name}, {self.male_count}, {self.fem_name}, {self.fem_count}, {self.file_year}")

    def male_names_as_array(self):
        '''Returns male names data as an array of lists'''
        return [self.rank, self.male_name, self.male_count,
                self.file_year, self.country]

    def fem_names_as_array(self):
        '''Returns female names data as an array of lists'''
        return [self.rank, self.fem_name, self.fem_count,
                self.file_year, self.country]


class FileData:
    def __init__(self, file_path, year):
        self.file_path = file_path
        self.year = year

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

            '''The data we need is on tables[2], checks for rows that have 5 objects in it'''
            main_data = []
            for item in tables[2]:
                if len(item) == 5:
                    main_data.append(item)

            '''Return a list of Row objects that we create with each row data on main_data'''
            list_of_row_objects: List[Row] = []
            for row in main_data:
                new_object = Row(row[0], row[1], row[2],
                                 row[3], row[4], self.year)
                list_of_row_objects.append(new_object)
            return list_of_row_objects


dir_usa = "/Users/rosinascampino/Desktop/names_project/html_usa"


def get_file_info(directory):
    '''Iterates over the given directory and returns an array of FileData objects'''

    list_of_file_data: List[FileData] = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".html"):
            fname = os.path.join(directory, file_name)
            year = int(file_name.split('.')[0])
            file_data = FileData(fname, year)
            list_of_file_data.append(file_data)

    return list_of_file_data


all_files = get_file_info(dir_usa)

extracted_data: List[Row] = []
'''Iterate over the directory and returns an array of Row objects'''
for fileDataObject in all_files:
    extracted_data.extend(fileDataObject.extract_data())

'''male_table as an array of lists'''
m_table = [i.male_names_as_array() for i in extracted_data]


'''fem_table as an array of lists'''
f_table = [i.fem_names_as_array() for i in extracted_data]


new_directory = os.chdir(
    '/Users/rosinascampino/Desktop/names_project/html_usa/usa_csv')


def write_male_names(m_table):
    with open('usa_male_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Name', 'Count', 'Year', 'Country'])
        writer.writerows(m_table)


def write_female_names(f_table):
    with open('usa_female_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Name', 'Count', 'Year', 'Country'])
        writer.writerows(f_table)


write_male_names(m_table)
write_female_names(f_table)
