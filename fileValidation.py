import csv

cols = 12
maxVal = 9.9
headings = ['"batch_id"', '"timestamp"', '"reading1"', '"reading2"', '"reading3"', '"reading4"',\
     '"reading5"', '"reading6"', '"reading7"', '"reading8"', '"reading9"', '"reading10"']

def validateFile(path):
    batches = set()
    with open(path, newline = '\n') as csvfile:
        reader=csv.reader(csvfile, delimiter=',', quotechar='|')
        lineCount = 0
        for row in reader:
            print(row)

            #check row has enough columns
            if len(row) != cols:
                print("Row is incomplete.")
                return False

            if lineCount == 0:
                #headings
                for i in range(0, cols):
                    if row[i] != headings[i]:
                        print(row[i] + " " + headings[i])
                        return False
            else:
                #check not duplicate batch id
                batchId = row[0]
                if batchId in batches:
                    print("Repeated batch id.")
                    return False
                else:
                    batches.add(batchId)
                
                #check values are in range
                for i in range(2, cols):
                    try:
                        if float(row[i]) > maxVal:
                            print("Value too large.")
                            return False
                    except:
                        #not a number
                        print("Reading is not a number.")
                        return False
            
            lineCount += 1

    return True
        
