import os
from name_classes import ChileFemaleNames, ChileMaleNames
from file_data_classes import ChileFiles
from csv_utils import write_csv_file


def get_file_data_objects(directory):
    """Iterates over a directory, returns a list of FileData objects"""
    list_of_file_data: list[ChileFiles] = []
    for file in os.listdir(directory):
        if file.endswith('.html'):
            file_path = os.path.join(directory, file)
            file_year = int(file.split('.')[0])
            file_data = ChileFiles(file_path, file_year)
            list_of_file_data.append(file_data)
    return list_of_file_data


def get_list_of_male_names_objects(list_of_data):
    """Iterates over a list of rows and returns a list of MaleNames objects"""
    chile_male_name_objects: list[ChileMaleNames] = []
    for row in list_of_data:
        if len(row) == 8:
            new_object = ChileMaleNames(row[1].title(), float(
                row[2].replace("%", "").replace(",", ".")), row[6], row[7])
            chile_male_name_objects.append(new_object)
    return chile_male_name_objects


def get_list_of_female_names_objects(list_of_data):
    """Iterates over a list of rows and returns a list of FemaleNames objects"""
    chile_female_name_objects: list[ChileFemaleNames] = []
    for row in list_of_data:
        if len(row) == 8:
            new_object = ChileFemaleNames(row[4].title(), float(
                row[5].replace("%", "").replace(",", ".")), row[6], row[7])
            chile_female_name_objects.append(new_object)
    return chile_female_name_objects


def update_name_count(list_of_objects):
    """calls the update_count() method on each Name object"""
    for object in list_of_objects:
        object.update_count()
    return list_of_objects


chile_directory = '/Users/rosinascampino/Desktop/names_project/raw_data/chile'

list_of_rows = []
file_data = get_file_data_objects(chile_directory)

for file in file_data:
    # calls the extract_data() method on each FileData object and adds all of its contents to an empty list
    list_of_rows.extend(file.extract_data())

chile_MaleNames_objects = update_name_count(
    get_list_of_male_names_objects(list_of_rows))

chile_FemaleNames_objects = update_name_count(
    get_list_of_female_names_objects(list_of_rows))

chile_male_names = [i.as_array() for i in chile_MaleNames_objects]
chile_female_names = [i.as_array() for i in chile_FemaleNames_objects]

chile_all_names = [i.as_array() for i in chile_MaleNames_objects] + \
    [i.as_array() for i in chile_FemaleNames_objects]

write_csv_file(chile_all_names, "chile_names.csv")
