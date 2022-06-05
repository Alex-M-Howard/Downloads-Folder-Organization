import os
from utilities import check_file_existence, move_file

HARD_DRIVE = 'C'
USERNAME = 'alexa'                                 # Change the hard_drive letter and username to match your machine!
TEMPORARY_FILES = ['crdownload', 'tmp']            # Add whatever temp files you have seen. This ignores them while something is STILL downloading
PATH = f'{HARD_DRIVE}:/Users/{USERNAME}/Downloads'

for file in os.listdir(PATH):
    try:
        if os.path.isfile(os.path.join(PATH, file)):
            file_name = file[::-1].split('.')
            extension = file_name[0][::-1]              # Getting file name and extension
            file_name = file
            file_path = f'{PATH}/{file_name}'

            if extension not in TEMPORARY_FILES:
                file_name, file_path = check_file_existence(file_name, file_path, PATH)     # Deals with duplicates by adding a 0 to front of filename
                move_file(file_name, extension, file_path, PATH)
        else:
            continue                                    # Ignores any extra folders that you've placed in your downloads folder
    except:
        pass
