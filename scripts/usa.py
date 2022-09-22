import os
from name_classes import UsaMaleNames, UsaFemaleNames
from file_data_classes import UsaFiles


def get_file_data_objects(directory):
    list_of_file_data: list[UsaFiles] = []
    for file in os.listdir(directory):
        if file.endswith('.html'):
            file_path = os.path.join(directory, file)
            file_year = int(file.split('.')[0])
            file_data = UsaFiles(file_path, file_year)
            list_of_file_data.append(file_data)
    return list_of_file_data


def get_list_of_male_names_objects(list_of_data):
    usa_male_name_objects: list[UsaMaleNames] = []
    for row in list_of_data:
        new_object = UsaMaleNames(row[0], row[1], row[4])
        usa_male_name_objects.append(new_object)
    return usa_male_name_objects


def get_list_of_female_names_objects(list_of_data):
    usa_female_name_objects: list[UsaFemaleNames] = []
    for row in list_of_data:
        new_object = UsaFemaleNames(row[2], row[3], row[4])
        usa_female_name_objects.append(new_object)
    return usa_female_name_objects


usa_directory = "/Users/rosinascampino/Desktop/names_project/raw_data/usa"

usa_file_data = get_file_data_objects(usa_directory)

usa_data = []
for file in usa_file_data:
    usa_data.extend(file.extract_data())

usa_MaleNames_objects = get_list_of_male_names_objects(usa_data)
usa_FemaleNames_objects = get_list_of_female_names_objects(usa_data)
usa_all_names_as_arrays = [i.as_array() for i in usa_MaleNames_objects] + \
    [i.as_array() for i in usa_FemaleNames_objects]
