from openpyxl import Workbook
from openpyxl import load_workbook
import csv
import os
from NameClasses import MaleNames, FemaleNames
from typing import List

"""write year in each file, load multiple workbooks, 
open wb['TOTAL'], create custom objects, write to a csv"""

os.chdir("/Users/rosinascampino/Desktop/names_project/spain")
spain_dir = "/Users/rosinascampino/Desktop/names_project/spain"


wbs = []

for file in os.listdir(spain_dir):
    if file.endswith('.xlsx'):
        wb = load_workbook(os.path.join(spain_dir, file))
        sheet = wb['TOTAL']
        for row in sheet['C5:C105']:
            file_year = (file.split('.')[0])
            for cell in row:
                cell.value = file_year

        wbs.append(wb['TOTAL'])


print(len(wbs))

data = []

for ws in wbs:
    for row in ws.iter_rows(min_row=5, max_row=104, min_col=1, max_col=5, values_only=True):
        data.append(list(row))

print(len(data))

# def extract_data(directory):
#     for file in os.listdir(directory):
#         if file.endswith('.xlsx'):
#             file_year = (file.split('.')[0])
#             data = []
#             wb = load_workbook(filename=os.path.join(
#                 directory, file), data_only=True)
#             totals = wb['TOTAL']
#             for row in totals.iter_rows(min_row=5, max_row=104, values_only=True):
#                 data.append(list(row))

#     return data


# spain_names = extract_data(spain_dir)

# print(len(spain_names))
