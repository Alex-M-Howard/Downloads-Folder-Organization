import os
# If adding new folder 
#    -add folder name to FOLDERS
#    -add the folder name as a key to FILE_TYPES and add list of file extensions to the key
#    -Leave last index of FOLDERS as the 'Other' folder for file extensions that aren't specified elsewhere.

FOLDERS = ['Audacity', 'Audio', 'Code', 'Documents', 'Images', 'Installers', 'PDFs', 'Videos', 'Zipped', 'Other']
FILE_TYPES = {
    'Audacity': ['aup3'],
    'Audio': ['mp3', 'wav', 'aac', 'flac', 'ogg'],
    'Code': ['py', 'css', 'html', 'js', 'cpp', 'php', 'sh', 'vb', 'java', 'cs', 'c'],
    'Documents': ['csv', 'xls', 'xlsm', 'xlsx', 'doc', 'docx', 'rtf', 'txt', 'pps', 'ppt', 'pptx'],
    'Images': ['bmp', 'jpg', 'jpeg', 'tif', 'eps', 'png', 'gif', 'img'],
    'Installers': ['exe', 'msi', 'bat'],
    'PDFs': ['pdf'],
    'Videos': ['mp4', 'mov', 'wmv', 'avi', 'mkv', 'webm'],
    'Zipped': ['rar', '7z', 'zip', 'tar'],
}


def move_file(file, extension, original_file_path, path):
    try:
        for key in FILE_TYPES:
            if extension in FILE_TYPES[key]:
                os.replace(original_file_path, f'{path}/{key}/{file}')
        os.replace(original_file_path, f'{path}/{FOLDERS[-1]}/{file}')        # File extension not found in FILE_TYPES - sends to 'Other'
    except:
        pass


def check_file_existence(file, file_path, path):
    directory = os.listdir(path)
    new_path = file_path
    new_file = file

    for each in FOLDERS:    
        if not os.path.isdir(f'{path}/{each}'): os.mkdir(f'{path}/{each}')    # If folder in FOLDERS doesn't exist, create folder         

    for each in directory:
        if os.path.exists(f'{path}/{each}/{file}'):
            new_file = '0' + new_file
            new_path = f'{path}/{new_file}'

            os.rename(file_path, new_path)
            (new_file, new_path) = check_file_existence(new_file, new_path, path)  # Recursion UNTIL unique file name created

    return new_file, new_path
