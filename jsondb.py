import portalocker
import os
import json

from constants import VISIBILITY

from utils import acquire_file_lock, release_file_lock,safe_file_write,safe_file_read, check_file_existence, safe_file_creation

def initialize_database(database):
    empty_database = {}

    f = open(database,'r+')
    try:
        acquire_file_lock(f)
        json_string = json.dumps(empty_database)
        f.seek(0)
        f.truncate()
        f.write(json_string)
    finally:
        release_file_lock(f)
        f.close()

def get(database,key):
    key = str(key)
    db=None
    record = None
    f = open(database,'r+')
    try:
        acquire_file_lock(f)
        db = json.loads(f.read())
        print(f'Database contents are {db}' if VISIBILITY else '')
        if key in db.keys():
            record =  db[key]
            print(f'Got value {record} against key {key}' if VISIBILITY else '')
        else:
            print(f'Key {key} not present' if VISIBILITY else '')
        
    finally:
        release_file_lock(f)
        f.close()

    return record

def put(database,key,value):
    key = str(key)
    db=None
    f = open(database,'r+')
    try:
        acquire_file_lock(f)
        db = json.loads(f.read())

        print(f'Database contents are {db}' if VISIBILITY else '')

        db[key] = value

        print(f'Put value {value} against key {key} into database' if VISIBILITY else '')

        json_string = json.dumps(db)
        f.seek(0)
        f.truncate()
        f.write(json_string)
        
    finally:
        release_file_lock(f)
        f.close()

def delete(database,key):
    key = str(key)
    f = open(database,'r+')

    try:
        acquire_file_lock(f)
        db = json.loads(f.read())

        if key in db.keys():
            print(f'Deleted key {key} in database' if VISIBILITY else '')
            del db[key]
        else:
            print(f'Key {key} not present in database' if VISIBILITY else '')


        json_string = json.dumps(db)
        f.seek(0)
        f.truncate()
        f.write(json_string)
        
    finally:
        release_file_lock(f)
        f.close()

def spin_up_database(database):
    if check_file_existence(database):
        print(f'Database {database} already exists' if VISIBILITY else '')
    else:
        safe_file_creation(database)
        initialize_database(database)
        print(f'Database {database} created' if VISIBILITY else '')