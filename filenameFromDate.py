import datetime

# search for files matching "name*.csv"
def filenameFromDate(date):
    name = "MED_DATA_"
    name += date.strftime("%Y%m%d")
    return name

print(filenameFromDate(datetime.datetime.now()))

