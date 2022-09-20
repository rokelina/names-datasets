import os
import csv
from names_classes.argentina_names import ArgentinaNames
from typing import List


def get_argentina_names_objects(directory):
    list_of_name_objects: List[ArgentinaNames] = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            fname = os.path.join(directory, filename)
            with open(fname, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    name = row[0].strip().title()
                    count = int(row[1])
                    year = int(row[2])
                    new_object = ArgentinaNames(name, count, year)
                    list_of_name_objects.append(new_object)
                return list_of_name_objects


argentina_directory = "/Users/rosinascampino/Desktop/names_project/argentina"
argentina_names_objects = get_argentina_names_objects(argentina_directory)
