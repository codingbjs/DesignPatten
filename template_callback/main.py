import sqlite3

from strategy.library.DAO import DAO

if __name__ == '__main__':
    dao = DAO(lambda: sqlite3.connect('template_method.db', isolation_level=None))
    # dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [
        ("hmd", 73),
        ("cyy", 12),
        ("hol", 48),
        ("htg", 87)
    ]

    # dao.insert('INSERT INTO users (name, age) VALUES (?, ?)', users)
