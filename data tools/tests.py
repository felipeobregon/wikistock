from tools import csv_to_json

import os

cwd = os.getcwd()
print(cwd)
files = os.listdir(cwd)

print(files)

#csv_to_json('data tools/a.csv')