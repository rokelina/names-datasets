import csv
from names_classes.italy_names import ItalyNames
import os
from typing import List


def get_italy_names_objects(directory):
    list_of_name_objects: List[ItalyNames] = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            fname = os.path.join(directory, filename)
            with open(fname, "r", newline='', encoding="ISO-8859-1") as file:
                reader = csv.reader(row.replace(';', ',') for row in file)
                next(reader, None)
                for row in reader:
                    name = row[0].replace('"', '').replace(' ', '').title()
                    count = int(row[1].replace('.', ''))
                    year = int(filename.split('.')[0])
                    new_object = ItalyNames(name, count, year)
                    list_of_name_objects.append(new_object)
                return list_of_name_objects


italy_directory = "/Users/rosinascampino/Desktop/names_project/italy"

italy_names_objects = get_italy_names_objects(italy_directory)
print(italy_names_objects[-1])
