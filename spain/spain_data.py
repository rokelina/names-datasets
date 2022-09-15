from openpyxl import load_workbook
import csv
import os
from NameClasses import MaleNames, FemaleNames
from typing import List


spain_dir = "/Users/rosinascampino/Desktop/names_project/spain"


def get_worksheets(directory_path):
    worksheets = []
    for file in os.listdir(directory_path):
        if file.endswith('.xlsx'):
            wb = load_workbook(os.path.join(directory_path, file))
            sheet = wb['TOTAL']
            for row in sheet['C5:C105']:
                file_year = int((file.split('.')[0]))
                for cell in row:
                    cell.value = file_year
            worksheets.append(wb['TOTAL'])
    return worksheets


def get_names_data(worksheets):
    data = []
    for ws in worksheets:
        for row in ws.iter_rows(min_row=5, max_row=104, min_col=1, max_col=5, values_only=True):
            data.append(list(row))
    return data


def write_csv(list_of_data):
    os.chdir('/Users/rosinascampino/Desktop/names_project/cleaned_data')
    with open('spain_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Count', 'Year',
                        'Gender', 'Country'])
        writer.writerows(list_of_data)


spain_data = get_names_data(get_worksheets(spain_dir))

spain_male_names: List[MaleNames] = []
spain_female_names: List[FemaleNames] = []

for row in spain_data:
    m_object = MaleNames(row[0].title(), int(row[1]), row[2])
    f_object = FemaleNames(row[3].title(), int(row[4]), row[2])
    spain_male_names.append(m_object)
    spain_female_names.append(f_object)


all_names = [i.as_array() for i in spain_male_names] + [i.as_array()
                                                        for i in spain_female_names]

write_csv(all_names)
