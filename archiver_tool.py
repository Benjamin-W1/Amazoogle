from pathlib import Path
import pathlib
import shutil




string = "MED_DATA_20220803153918"


def store_file(string):

    year = string[9:13]
    month = string[13:15]
    day = string[15:17]
    hour = string[17:19]
    minute = string[19:21]
    second = string[21:23]


    path = pathlib.Path(f'Archive/{year}/{month}/{day}/{hour}/{minute}/{second}')
    path.mkdir(parents=True, exist_ok=True)

    
    source = f'C:\\Users\\gibcl\\Downloads\\{string}'
    destination = path

    if path.is_file():

        shutil.move(source, destination)
    


store_file(string)

