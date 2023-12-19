import sys
import pandas as pd 
import re
import csv

csv_file = sys.argv[1]

'''
Titles/Headers for shipping cost:
Label Cost, Shipping Cost
'''

def read_and_store_data():
    with open(csv_file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            pass

def main():
    read_and_store_data()

if __name__ == "__main__":
    main()