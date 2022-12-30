import os
import csv
from name_classes import ArgentinaNames
from csv_utils import write_csv_file


def get_argentina_names_objects(directory):
    list_of_name_objects: list[ArgentinaNames] = []
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
                    if new_object.count >= 5:
                        list_of_name_objects.append(new_object)
    return list_of_name_objects


argentina_directory = "/Users/rosinascampino/Desktop/names_project/raw_data/argentina"
argentina_names_objects = get_argentina_names_objects(argentina_directory)
argetina_names_as_array = [i.as_array() for i in argentina_names_objects]

write_csv_file(argetina_names_as_array, "argentina_names.csv")
