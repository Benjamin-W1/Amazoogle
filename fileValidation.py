import csv

cols = 12
maxVal = 9.9

def validateHeadings(row):
    return len(row) == 12

def validateFile(path):
    batches = {}
    with open(path, newline = '\n') as csvfile:
        reader=csv.reader(csvfile, delimiter=',', quotechar='|')
        lineCount = 0
        for row in reader:
            #check row has enough columns
            if len(row) != cols:
                return False

            if lineCount == 0:
                #headings
                if not validateHeadings(row):
                    return False
            else:
                #check not duplicate batch id
                batchId = row[0]
                if batchId in batches:
                    return False
                else:
                    batches.add(batchId)
                
                #check values are in range
                for r in range(2, cols):
                    if r > maxVal:
                        return False
            
            lineCount += 1
        

validateFile("test.csv")