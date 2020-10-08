import unicodecsv
import os



def scanCSVFile(fileName, filePath):
    csvFile = filePath + "\\" + fileName
    fileData = False
    if os.path.isfile(csvFile) == False:
        return fileData
    with open(csvFile, 'rb') as csvFilePtr:
        reader = unicodecsv.DictReader(csvFilePtr)
        fileData = list(reader)
    return fileData

def formatData(data):
    for row in data:
        row['timestamp'] = int(row['timestamp'])
        row['response_time'] = int(row['response_time'])
        row['response_code'] = int(row['response_code'])
    print(data[0])




