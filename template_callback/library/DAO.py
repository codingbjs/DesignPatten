import sqlite3


class DAO:
    def __init__(self, fn):
        self.get_connection = fn

    def create(self, sql):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
        finally:
            self.close(cursor, conn)

    def insert(self, sql, data):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            self.close(cursor, conn)

    def select(self, sql):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        finally:
            self.close(cursor, conn)

    def close(self, cursor, conn):
        cursor.close()
        conn.close()
