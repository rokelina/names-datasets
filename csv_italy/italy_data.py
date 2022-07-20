import csv
import os


dir_italy = '/Users/rosinascampino/Desktop/names_project/csv_italy'
italy_table = [['Name', 'Count', 'Year', 'Country']]

for filename in os.listdir(dir_italy):
    if filename.endswith('.csv'):
        fname = os.path.join(dir_italy, filename)
        with open(fname, "r", newline='', encoding="ISO-8859-1") as file:
            reader = csv.reader(row.replace(';', ',') for row in file)
            next(reader, None)
            for row in reader:
                name = row[0].replace('"', '').replace(' ', '').title()
                count = int(row[1].replace('.', ''))
                year = int(filename.split('.')[0])
                country = "Italy"
                new_line = [name, count, year, country]
                italy_table.append(new_line)

os.chdir('/Users/rosinascampino/Desktop/names_project/cleaned_data')

with open('italy_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(italy_table)
