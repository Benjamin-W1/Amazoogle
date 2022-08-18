import csv
import json
import re

cols = 12
maxVal = 9.9
headings = ['"batch_id"', '"timestamp"', '"reading1"', '"reading2"', '"reading3"', '"reading4"',\
     '"reading5"', '"reading6"', '"reading7"', '"reading8"', '"reading9"', '"reading10"']

def logError(message, fileName):
    data = {
        'file' : fileName,
        'issue' : message
    }
    with open('log.json', 'a') as file:
        json.dump(data, file)

def validateFileName(path):
    x = path.split("/")
    name = x[len(x) - 1]
    # must match     MED_DATA_  Y    Y    Y    Y    M    M    D    D    H    H    M    M    S    S     .csv
    return re.search("MED_DATA_[0-2][0-9][0-9][0-9][0-1][0-9][0-3][0-9][0-2][0-9][0-5][0-9][0-5][0-9]\.csv", name)

def validateFile(path):
    if not validateFileName(path):
        logError("File name is invalid", path)
        return False
    batches = set()
    with open(path, newline = '\n') as csvfile:
        reader=csv.reader(csvfile, delimiter=',', quotechar='|')
        lineCount = 0
        for row in reader:

            #check row has enough columns
            if len(row) != cols:
                logError("Row is incomplete.", path)
                return False

            if lineCount == 0:
                #headings
                for i in range(0, cols):
                    if row[i] != headings[i]:
                        logError("Headings are incorrect.", path)
                        return False
            else:
                #check not duplicate batch id
                batchId = row[0]
                if batchId in batches:
                    logError("Repeated batch id.", path)
                    return False
                else:
                    batches.add(batchId)
                
                #check values are in range
                for i in range(2, cols):
                    try:
                        if float(row[i]) > maxVal:
                            logError("Value too large.", path)
                            return False
                    except:
                        #not a number
                        logError("Reading is not a number.", path)
                        return False
            
            lineCount += 1

    return True
        
