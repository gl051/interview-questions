#!/usr/bin/env python

"""
    Archive all the files in a folder provided as parameter, make a directory
    based on the last modification time for the file.
"""

import os
from datetime import datetime

def archive_files(dir_full_name):
    # Check if the folder exists
    if not os.path.exists(dir_full_name):
        print 'Directory {0} does not exist'.format(dir_full_name)
        return

    for file_name in os.listdir(dir_full_name):
        full_file_name = os.path.join(dir_full_name, file_name)
        if os.path.isfile(full_file_name):
            dt = datetime.fromtimestamp(os.path.getmtime(full_file_name))
            folder_name = '{0}{1}{2}'.format(dt.year, dt.month, dt.day)
            new_dir_full_name = os.path.join(dir_full_name, folder_name)
            if not os.path.exists(new_dir_full_name):
                os.mkdir(new_dir_full_name)
            os.rename(full_file_name, os.path.join(new_dir_full_name,file_name))
            print os.path.join(new_dir_full_name,file_name)


archive_files('/Users/Gianluca/Desktop/TMP/pytest')
