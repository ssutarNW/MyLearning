import sys
import csv
import json

def csv_to_json(in_file, out_file):
    """
    Purpose : Write to new JSON file with the content from CSV file.
              Assume that your function returns 0 when the reversed integer overflows.
    Input   : in_file  (str) - Input CSV file path
            : out_file (str) - Output JSON file path
    Example : csv_to_json('csv.txt', 'json.txt')
    """
    with open(out_file, 'w') as json_file:
        with open(in_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                json.dump(row, json_file)

if __name__ == "__main__" :
    print ("Converting CSV file {} into JSON file {}".format(sys.argv[1], sys.argv[2]))
    csv_to_json(sys.argv[1],sys.argv[2])
