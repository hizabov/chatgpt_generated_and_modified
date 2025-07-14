import csv
import json


def csv_to_json_object(csv_filepath, json_object_filepath):
    data = []
    with open(csv_filepath, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    with open(json_object_filepath, mode='w', encoding='utf-8') as json_file_object:
        json.dump(data, json_file_object, indent=4)
