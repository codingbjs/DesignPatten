from strategy.client.ConnectionCreator import ConnectionCreator
from strategy.library.DAO import DAO

if __name__ == '__main__':
    conn = ConnectionCreator()
    dao = DAO(conn)
    # dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [
        ("hmd", 73),
        ("cyy", 12),
        ("hol", 48),
        ("htg", 87)
    ]

    # dao.insert('INSERT INTO users (name, age) VALUES (?, ?)', users)
