import os
import sys
from fileHandler import *
from dataParser import *
from utils import *

if __name__ == "__main__":
    fileName = "Sample input - Log Parser.csv"
    if os.path.isfile(fileName) == False:
        print("File Not Found")
        sys.exit(0)
    fileData = scanCSVFile(fileName)
    #print(fileData)
    formatData(fileData)
    convertURLtotype(fileData)
    df = converttoDF(fileData)

    sorted_df = get_freq(df)
    print("1.	Top 5 highest throughput URLs:")
    print(sorted_df.iloc[:5])


    print("2.	Time taken for each endpoint:")
    print_res_time_details(df)


