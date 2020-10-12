import os
from datetime import datetime


"""
    Given a folder full path, provided as a parameter, 
    Then archive all the files contained in that folder,
    Using a new target directory named with the last modification time for the each file
"""


CODES = {
    'DIRECTORY_NOT_EXISTS' : 100,
    'ERROR_GENERIC': 1, 
    'SUCCESS' : 0 
}

def archive_files(dir_full_name):
    # Check if the folder exists
    if not os.path.exists(dir_full_name):
        print(f"Directory {dir_full_name} does not exist")
        return CODES.get('DIRECTORY_NOT_EXISTS', 9999)
    try:
        for file_name in os.listdir(dir_full_name):
            full_file_name = os.path.join(dir_full_name, file_name)
            if os.path.isfile(full_file_name):
                dt = datetime.fromtimestamp(os.path.getmtime(full_file_name))
                folder_name = '{0}{1}{2}'.format(dt.year, dt.month, dt.day)
                new_dir_full_name = os.path.join(dir_full_name, folder_name)
                if not os.path.exists(new_dir_full_name):
                    os.mkdir(new_dir_full_name)
                os.rename(full_file_name, os.path.join(new_dir_full_name,file_name))
                print(f"{os.path.join(new_dir_full_name,file_name)}")
        return CODES.get('SUCCESS')
    except Exception: 
        return CODES.get('ERROR_GENERIC')