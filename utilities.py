import os
# You can add folders or add to individual file types.
# If adding new folder, add list of file extensions

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
        os.replace(original_file_path, f'{path}/{FOLDERS[-1]}/{file}')
    except:
        pass


def check_file_existence(file, file_path, path):
    directory = os.listdir(path)
    new_path = file_path
    new_file = file

    for each in FOLDERS:    # If folder doesn't exist, create folder
        if not os.path.isdir(f'{path}/{each}'): os.mkdir(f'{path}/{each}')

    for each in directory:
        if os.path.exists(f'{path}/{each}/{file}'):
            new_file = '0' + new_file
            new_path = f'{path}/{new_file}'

            os.rename(file_path, new_path)
            (new_file, new_path) = check_file_existence(new_file, new_path, path)

    return new_file, new_path
