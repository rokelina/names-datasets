import csv
import os


dir_argentina = '/Users/rosinascampino/Desktop/names_project/csv_argentina'
arg_table = [['Name', 'Count', 'Year', 'Country']]

for filename in os.listdir(dir_argentina):
    if filename.endswith('.csv'):
        fname = os.path.join(dir_argentina, filename)
        with open(fname, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                name = row[0].strip().title()
                count = int(row[1])
                year = row[2]
                country = 'Argentina'
                new_line = [name, count, year, country]
                # since the dataset contains many names with a frequency value of one,
                # we'll append those names which frequency value is equal or greater than 50
                if count >= 50:
                    arg_table.append(new_line)
                else:
                    pass


os.chdir('/Users/rosinascampino/Desktop/names_project/cleaned_data')

with open('argentina_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(arg_table)
