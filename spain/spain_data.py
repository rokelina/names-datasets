from openpyxl import load_workbook
import csv
import os
from NameClasses import MaleNames, FemaleNames
from typing import List


os.chdir("/Users/rosinascampino/Desktop/names_project/spain")
spain_dir = "/Users/rosinascampino/Desktop/names_project/spain"


def get_worksheets(directory_path):
    worksheets = []
    for file in os.listdir(directory_path):
        if file.endswith('.xlsx'):
            wb = load_workbook(os.path.join(directory_path, file))
            sheet = wb['TOTAL']
            for row in sheet['C5:C105']:
                file_year = (file.split('.')[0])
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
    with open('spain_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Male Name', 'Male Count', 'Year',
                        'Female name', 'Female Count'])
        writer.writerows(list_of_data)
