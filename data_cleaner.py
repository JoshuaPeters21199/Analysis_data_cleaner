import sys
import pandas as pd 

excel_file = sys.argv[1]

def open_data():
    dataframe = pd.read_excel(excel_file)
    print(dataframe)

def main():
    open_data()

if __name__ == "__main__":
    main()