import os
from names_classes.chile_names import ChileFilesData, ChileFemaleNames, ChileMaleNames
from typing import List


def get_file_data_objects(directory):
    list_of_file_data = []
    for file in os.listdir(directory):
        if file.endswith('.html'):
            file_path = os.path.join(directory, file)
            file_year = int(file.split('.')[0])
            file_data = ChileFilesData(file_path, file_year)
            list_of_file_data.append(file_data)
    return list_of_file_data


def get_list_of_male_names_objects(list_of_data):
    chile_male_name_objects: List[ChileMaleNames] = []
    for row in list_of_data:
        if len(row) == 8:
            new_object = ChileMaleNames(row[1], row[2], row[6], row[7])
            chile_male_name_objects.append(new_object)
    return chile_male_name_objects


def get_list_of_female_names_objects(list_of_data):
    chile_female_name_objects: List[ChileFemaleNames] = []
    for row in list_of_data:
        if len(row) == 8:
            new_object = ChileFemaleNames(row[4], row[5], row[6], row[7])
            chile_female_name_objects.append(new_object)
    return chile_female_name_objects


def update_name_count(list_of_objects):
    for object in list_of_objects:
        object.update_count()
    return list_of_objects


chile_directory = '/Users/rosinascampino/Desktop/names_project/chile/html_files'

list_of_rows = []
file_data = get_file_data_objects(chile_directory)

for file in file_data:
    list_of_rows.extend(file.extract_data())

male_name_objects = update_name_count(
    get_list_of_male_names_objects(list_of_rows))

female_name_objects = update_name_count(
    get_list_of_female_names_objects(list_of_rows))

chile_male_names = [i.as_array() for i in male_name_objects]
chile_female_names = [i.as_array() for i in female_name_objects]
