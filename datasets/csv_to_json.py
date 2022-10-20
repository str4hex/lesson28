import os
import csv
import json

file_name_path = os.listdir()
file_name = []

for files_name in file_name_path:
    if files_name.split('.')[1:2] == ['csv']:
        file_name.append(files_name)

for files_to_json in file_name:
    with open(files_to_json, encoding='utf-8') as file_csv:
        reader = csv.DictReader(file_csv)
        rows = list(reader)
    file = "".join(files_to_json.split('.')[0] + '.json')

    with open(file, 'w', encoding='utf-8') as file_json:
        json.dump(rows, file_json, indent=4, ensure_ascii=False)
