import sys
import pandas as pd 
import re
import csv

csv_file = sys.argv[1]

def read_and_store_data():
    dataframe = pd.read_excel(csv_file)
    print(dataframe)

def main():
    read_and_store_data()

if __name__ == "__main__":
    main()