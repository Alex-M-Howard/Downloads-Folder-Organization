import os
from utilities import check_file_existence, move_file

HARD_DRIVE = 'C'
USERNAME = 'alexa'
TEMPORARY_FILES = ['crdownload', 'tmp']
PATH = f'{HARD_DRIVE}:/Users/{USERNAME}/Downloads'

for file in os.listdir(PATH):
    try:
        if os.path.isfile(os.path.join(PATH, file)):
            file_name = file[::-1].split('.')
            extension = file_name[0][::-1]             # Getting file name and extension
            #file_name = file.split(f'.{extension}')    # Can probably be simplified, will learn later
            #file_name = f'{file_name[0]}.{extension}'
            file_name = file
            file_path = f'{PATH}/{file_name}'

            if extension not in TEMPORARY_FILES:
                file_name, file_path = check_file_existence(file_name, file_path, PATH)
                move_file(file_name, extension, file_path, PATH)
        else:
            continue
    except:
        pass
