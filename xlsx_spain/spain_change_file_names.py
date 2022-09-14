import openpyxl
import csv
import os
from dataclasses import dataclass
from typing import List

"""change file names"""

os.chdir("/Users/rosinascampino/Desktop/names_project/xlsx_spain/")
directory = "/Users/rosinascampino/Desktop/names_project/xlsx_spain/"

for file in os.listdir(directory):
    if file.endswith(".xlsx"):
        new_name = '20' + file.split('c')[1]
        os.rename(
            file, f"/Users/rosinascampino/Desktop/names_project/spain/{new_name}")
