import sqlite3


class SQLiteDataExtractor:

    def __init__(self, filepath):
        self.db = sqlite3.connect(filepath)

    @property
    def parsed_data(self):
        return self.db
