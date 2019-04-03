import sys
import csv
import json

def csv_to_json(in_file, out_file):
    """
    Purpose : Write to new JSON file with the content from CSV file.
    Input   : in_file  (str) - Input CSV file path
            : out_file (str) - Output JSON file path
    Example : csv_to_json('csv.txt', 'json.txt')
    """
    with open(out_file, 'w') as json_file:
        with open(in_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                json.dump(row, json_file)
