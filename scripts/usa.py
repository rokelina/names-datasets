import os
from name_classes import UsaNames
from csv_utils import write_csv_file


def get_list_of_name_objects(directory):
    list_of_name_objects: list[UsaNames] = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            fname = os.path.join(directory, filename)
            with open(fname, 'r', encoding='utf-8') as file:
                for row in file:
                    line = row.split(',')
                    new_object = UsaNames(line[0], int(
                        line[2]), int(filename[3:7]), str(line[1]))
                    list_of_name_objects.append(new_object)
    return list_of_name_objects


usa_dir = "/Users/rosinascampino/Desktop/names_project/raw_data/usa"
usa_names = get_list_of_name_objects(usa_dir)
usa_names_as_array = [i.as_array() for i in usa_names]

write_csv_file(usa_names_as_array, "us_names.csv")
