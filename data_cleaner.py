import sys
import pandas as pd 
import re
import csv
from pprint import pprint
import inquirer

csv_file = sys.argv[1]
all_rows = []

'''
Titles/Headers for shipping cost:
Label Cost, Shipping Cost
'''

def extract_headers():
    row_count = 0
    with open(csv_file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if row_count == 0:
                return row

def verify_headers(header_list):
    headers = extract_headers()
    for header in headers:
        print(f'{header}')
    questions = [
        inquirer.List('shipping_cost',
                      message='Which column contains the correct shipping cost?',
                      choices=header_list,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers

def read_and_store_data():
    row_count = 0
    with open(csv_file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if row_count == 0:
                file_headers = row
            else:
                all_rows.append(row)
            row_count += 1

def main():
    read_and_store_data()
    verify_headers(extract_headers())

if __name__ == "__main__":
    main()