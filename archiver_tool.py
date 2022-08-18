from pathlib import Path
import pathlib
import shutil



#needs .csv
string = "MED_DATA_20220803153918.csv"


def store_file(string):

    #splice filename
    year = string[9:13]
    month = string[13:15]
    day = string[15:17]
    hour = string[17:19]
    minute = string[19:21]
    second = string[21:23]

    #create path
    path = pathlib.Path(f'Archive/{year}/{month}/{day}/{hour}/{minute}/{second}')
    path.mkdir(parents=True, exist_ok=True)

    #change source to where downloaded from ftp
    source = f'C:/Users/gibcl/Downloads/{string}'
    destination = path

    #check file doesnt already exist
    if not path.is_file():

        shutil.move(source, destination)
    
store_file(string)
