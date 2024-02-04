import portalocker
import os
import json

from constants import VISIBILITY

def acquire_file_lock(file_obj):
    print(f'Acquiring lock on {file_obj.name}...' if VISIBILITY else '')

    portalocker.lock(file_obj,portalocker.LOCK_EX)

    print(f'Lock acquired on {file_obj.name}!' if VISIBILITY else '')

def release_file_lock(file_obj):
    print(f'Releasing lock on {file_obj.name}...' if VISIBILITY else '')
    portalocker.unlock(file_obj)
    print(f'Lock released on {file_obj.name}!' if VISIBILITY else '')

def check_file_existence(file_name):
    if os.path.exists(file_name):
        print(f'{file_name} exists' if VISIBILITY else '')
        return True
    else:
        print(f'{file_name} does not exist' if VISIBILITY else '')
        return False

def safe_file_creation(file_path):
    try:
        with open(file_path, 'x') as f:
            print(f'File \'{file_path}\' created safely.' if VISIBILITY else '')
    except FileExistsError:
        print(f'The file \'{file_path}\' already exists.' if VISIBILITY else '')

def safe_file_read(file_name):
    contents = None

    if (check_file_existence(file_name)):
        f = open(file_name,'r+')
        try:
            acquire_file_lock(f)
            contents= f.read()
        finally:
            release_file_lock(f)
            f.close()
    
    return contents

def safe_file_write(file_name,contents):
    f = open(file_name,'r+')
    try:
        acquire_file_lock(f)
        contents= f.write(contents)
    finally:
        release_file_lock(f)
        f.close()