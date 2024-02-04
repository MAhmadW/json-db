from jsondb import spin_up_database, get, put, delete

DATABASE = 'example'

def main():
    spin_up_database(DATABASE)
    put(DATABASE,1,123)
    get(DATABASE,1)
    delete(DATABASE,'1') # Understand that JSON always stores keys as string, so 1 and "1" are the same
    put(DATABASE,1,456)
    get(DATABASE,1)
    put(DATABASE,2,'a')
    put(DATABASE,3,'b')


if __name__=="__main__":
    main()