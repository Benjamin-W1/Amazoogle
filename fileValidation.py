import csv

def validateFile(path):
    with open(path, newline = '\n') as csvfile:
        reader=csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)
            print(row[0])

validateFile("test.csv")