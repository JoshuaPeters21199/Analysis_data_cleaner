import csv
import re
import pandas as pd
import sys

clean_data_lst = []
csv_filename = sys.argv[1]
clean_filename = csv_filename + '_clean.csv'

def checkString(str):
    match = re.search(r'[a-zA-Z]+', str) and re.search(r'[0-9]+', str)
    if match:
        return True
    else:
        return False

def main():
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if not checkString(row[15]):
                clean_data_lst.append(row)

    csv_file.close()

    with open(clean_filename, 'w', newline='') as file:
        writer = csv.writer(file)

        for i in clean_data_lst:
            writer.writerow(i)

    file.close()

if __name__ == "__main__":
    main()

