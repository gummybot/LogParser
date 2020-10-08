import os
import sys
from fileHandler import *
from dataParser import *





if __name__ == "__main__":
    filePath = os.path.curdir
    fileName = "Sample input - Log Parser.csv"
    fileData = scanCSVFile(fileName, filePath)
    if fileData == False:
        print("File Not Found")
        sys.exit(0)
    print(fileData)
    formatData(fileData)
    filteredData = filterDataByMethod(fileData)
    for method in filteredData.keys():
        filteredData2 = filterDataByURL(filteredData[method])
        filteredData[method] = filteredData2

    print(filteredData)

    filteredData3 = filterDataByURL(fileData)
    for url in filteredData3.keys():
        filteredData4 = filterDataByMethod(filteredData3[url])
        filteredData3[url] = filteredData4

    print(filteredData3)
    print(filteredData3[4])


