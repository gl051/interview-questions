import pytest
from pathlib import Path
import shutil
import archive_files

def test_not_existing_directory():
    assert(archive_files.archive_files("XYZ")) == archive_files.CODES.get("DIRECTORY_NOT_EXISTS",9999)

def test_move_files():
    p = Path().cwd() / 'tests' / 'tmp'
    p.mkdir(exist_ok=True)
    (p / "test_archive_files_file1.txt").touch()
    (p / "test_archive_files_file2.txt").touch()
    (p / "test_archive_files_file3.txt").touch()
    assert(archive_files.archive_files(str(p))) == archive_files.CODES.get("SUCCESS",9999)



    

    


