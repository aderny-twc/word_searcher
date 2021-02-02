import sqlite3

class UseDataSqlite:
    """
    A minimal sqlite3 context handler. 
    """

    def __init__(self, path: Path='vsearchDB.db'):
        self.path = path

    def __enter__(self):
        try:
            self.conn = sqlite.connect(self.path)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as err:
            print('Some error:', str(err))
    
    def __exit__(self, exc_type, exc_val, exc_tb)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
