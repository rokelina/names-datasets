import os


"""change file names"""

os.chdir("/Users/rosinascampino/Desktop/names_project/raw_data/spain/")
directory = "/Users/rosinascampino/Desktop/names_project/raw_data/spain/"

for file in os.listdir(directory):
    if file.startswith("nomnac"):
        new_name = '20' + file.split('c')[1]
        os.rename(
            file, f"/Users/rosinascampino/Desktop/names_project/raw_data/spain/{new_name}")
