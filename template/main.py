from Dao import *

if __name__ == '__main__':
    dao = Dao()
    # dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [
        ("hmd", 73),
        ("cyy", 12),
        ("hol", 48),
        ("htg", 87)
    ]

    # dao.insert('INSERT INTO users (name, age) VALUES (?, ?)', users)