import unicodecsv
import os
import pandas as pd


def readCSV(fileName):
    log_data = pd.read_csv(fileName)
    print(log_data)
    return log_data

def scanCSVFile(fileName):
    csvFile = fileName
    with open(csvFile, 'rb') as csvFilePtr:
        reader = unicodecsv.DictReader(csvFilePtr)
        fileData = list(reader)
    return fileData

def formatData(data):
    for row in data:
        row['timestamp'] = int(row['timestamp'])
        row['response_time'] = int(row['response_time'])
        row['response_code'] = int(row['response_code'])




