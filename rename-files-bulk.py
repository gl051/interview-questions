#!/usr/bin/python

"""
    Rename files in a folder using to all lower case and replace spaces with
    the underscore:
    File1 --> file1
    FileAbc --> file_abc
    aBc --> a_bc
    _AbcDef -->_abc_def
    - skip if is a directory
"""

import os

def rename_files(folder_path):
    # list directory content and look for files only
    for entry in os.listdir(folder_path):
        old_filename = os.path.join(folder_path,entry)
        if os.path.isfile(old_filename):
            new_entry = get_new_filename(entry)
            new_filename = os.path.join(folder_path, new_entry)
            os.rename(old_filename, new_filename)

def get_new_filename(old_filename):
    # do not consider the extension
    old_name= os.path.splitext(old_filename)[0]
    # first character remains the same, just goes lowercase
    new_name = list(old_name[0].lower())
    # for the other charactes if is upper, alpha and comes after another character
    # then put separator '_', otherwise just lowecase the character
    for c in old_name[1:]:
        if c.isalpha and c.isupper() and new_name[-1] != '_':
            new_name.append('_')
        if c == '-':
            new_name.append('_')
            continue
        new_name.append(c.lower())
    tmp_filename = ''.join(new_name)
    ext = os.path.splitext(old_filename)[1]
    return tmp_filename + ext
