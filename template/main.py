from Dao import *

if __name__ == '__main__':
    dao = Dao()
    dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
