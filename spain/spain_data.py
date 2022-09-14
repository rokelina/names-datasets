from openpyxl import Workbook
from openpyxl import load_workbook
import csv
import os
from dataclasses import dataclass
from typing import List

"""write year in each file, load multiple workbooks, 
open wb['TOTAL'], create custom objects, write to a csv"""

os.chdir("/Users/rosinascampino/Desktop/names_project/spain")
spain_dir = "/Users/rosinascampino/Desktop/names_project/spain"


def extract_data(directory):
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            file_year = (file.split('.')[0])
            data = []
            wb = load_workbook(filename=os.path.join(
                directory, file), data_only=True)
            totals = wb['TOTAL']
            for row in totals.iter_rows(min_row=5, max_row=104, values_only=True):
                data.append(list(row))

    return data


spain_names = extract_data(spain_dir)

print(len(spain_names))
