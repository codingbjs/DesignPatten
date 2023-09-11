import sqlite3

from strategy.library.AbstractConnectionCreator import AbstractConnectionCreator


class ConnectionCreator(AbstractConnectionCreator):
    def get_connection(self):
        return sqlite3.connect('template_method.db', isolation_level=None)
