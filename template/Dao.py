import sqlite3


class Dao:
    def get_connection(self):
        return sqlite3.connect('template_method.db', isolation_level=None)

    def create(self, sql):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
        finally:
            self.close(cursor, conn)

    def close(self, cursor, conn):
        cursor.close()
        conn.close()
