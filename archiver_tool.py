from pathlib import Path
import pathlib
import shutil

def store_file(string):

    year = string[9:13]
    month = string[13:15]
    day = string[15:17]
    hour = string[17:19]
    minute = string[19:21]
    second = string[21:23]


    path = pathlib.Path(f'Archive/Y{year}/M{month}/D{day}')
    path.mkdir(parents=True, exist_ok=True)

    source = f'{pathlib.Path().resolve()}/{string}'
    destination = path

    if path.is_file():

        shutil.move(source, destination)
