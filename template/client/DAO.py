import sqlite3

from template.library.AbstractDAO import AbstractDAO


class DAO(AbstractDAO):
    def get_connection(self):
        return sqlite3.connect('template_method.db', isolation_level=None)