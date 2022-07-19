from bs4 import BeautifulSoup
import os
from typing import List
import csv

'''Define the class Row that will hold the data I need'''


class Row:
    def __init__(self, rank, male_name, male_percent, fem_name, fem_percent, totals, year):
        self.rank = int(rank)
        self.male_name = male_name.title()
        self.male_percent = float(
            male_percent.replace("%", "").replace(",", "."))
        self.fem_name = fem_name.title()
        self.fem_percent = float(
            fem_percent.replace("%", "").replace(",", "."))
        self.totals = totals
        self.year = year
        self.male_count = 0
        self.fem_count = 0
        self.m_gender = 'M'
        self.f_gender = 'F'
        self.country = 'Chile'

    def update_male_count(self):
        '''Takes the percentage and gets the total count'''
        self.male_count = round((self.male_percent * self.totals) / 100)
        return self.male_count

    def update_fem_count(self):
        '''Takes the percentage and gets the total count'''
        self.fem_count = round((self.fem_percent * self.totals) / 100)
        return self.fem_count

    def male_names_as_array(self):
        '''Returns male names data as a list'''
        return [self.rank, self.male_name, self.male_count, self.m_gender, self.year, self.country]

    def fem_names_as_array(self):
        '''Returns female names data as a list'''
        return [self.rank, self.fem_name, self.fem_count, self.f_gender, self.year, self.country]


class FileData:
    def __init__(self, file_path, file_year):
        self.file_path = file_path
        self.file_year = file_year
        self.file_totals = 0

    def extract_data(self):
        '''Extract td for each html file located at self.file_path'''

        with open(self.file_path, 'r', encoding="iso-8859-1") as file:
            soup = BeautifulSoup(file, 'html.parser')
            file_contents = [
                [td.get_text(strip=True) for td in tr.find_all('td')]
                for tr in soup.find_all('tr')
            ]

            '''Next two lines get the total name count for that file'''
            string = [i.replace('.', '') for i in file_contents[-2]]
            self.file_totals = int(
                ''.join(filter(str.isdigit, ''.join(string))))

            '''Delete unnecessary rows'''
            del file_contents[0:2]

            '''Append file totals and file year to each row'''
            for line in file_contents:
                line.append(self.file_totals)
                line.append(self.file_year)

            return file_contents


dir_chile = "/Users/rosinascampino/Desktop/names_project/html_chile"


def get_file_objects(directory):
    '''Iterates over the given directory and returns an array of FileData objects'''

    list_of_file_data: List[FileData] = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".html"):
            fname = os.path.join(directory, file_name)
            year = int(file_name.split('.')[0])
            file_data = FileData(fname, year)
            list_of_file_data.append(file_data)

    return list_of_file_data


all_files = get_file_objects(dir_chile)

extracted_data = []

'''Iterates over an array of FileData objects, calls the extract_data() method in each object and adds the data to the list extracted_data'''
for file in all_files:
    extracted_data.extend(file.extract_data())

listOfRowObjects: List[Row] = []

'''Iterates over extracted_data and returns an array of Row instances'''
for line in extracted_data:
    if len(line) == 8:
        new_object = Row(line[0], line[1], line[2],
                         line[4], line[5], line[6], line[7])
        listOfRowObjects.append(new_object)


def update_count(rows):
    '''Updates male name and female name count'''

    for row in listOfRowObjects:
        row.update_male_count()
        row.update_fem_count()
    return rows


'''This is the final list of cleaned up Row objects'''
rows = update_count(listOfRowObjects)

'''Get male names and female names data as an array of lists'''
m_table = [i.male_names_as_array() for i in rows]
f_table = [i.fem_names_as_array() for i in rows]


new_directory = os.chdir(
    '/Users/rosinascampino/Desktop/names_project/html_chile/chile_csv')


def write_male_names(m_table):
    with open('chile_male_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Name', 'Count', 'Gender', 'Year', 'Country'])
        writer.writerows(m_table)


def write_female_names(f_table):
    with open('chile_female_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Name', 'Count', 'Gender', 'Year', 'Country'])
        writer.writerows(f_table)


write_male_names(m_table)
write_female_names(f_table)
