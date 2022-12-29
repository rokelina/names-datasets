import csv
import os


def write_csv_file(names_list, file_name: str):
    os.chdir("/Users/rosinascampino/Desktop/names_project/cleaned_data/")
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Count", "Year", "Gender", "Country"])
        writer.writerows(names_list)
