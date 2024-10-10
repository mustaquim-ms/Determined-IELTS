import sqlite3

class Vocabulary:
    def __init__(self):
        self.conn = sqlite3.connect('vocabulary.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vocabulary
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          english TEXT,
                          bangla_unicode TEXT)''')
        self.conn.commit()

    def add_vocabulary(self, english, bangla_unicode):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO vocabulary (english, bangla_unicode) VALUES (?, ?)", (english, bangla_unicode))
        self.conn.commit()

    def get_all_vocabulary(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM vocabulary")
        rows = cursor.fetchall()
        return rows

    def get_vocabulary_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM vocabulary WHERE id = ?", (id,))
        row = cursor.fetchone()
        return row

    def update_vocabulary(self, id, english, bangla_unicode):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE vocabulary SET english=?, bangla_unicode=? WHERE id=?", (english, bangla_unicode, id))
        self.conn.commit()

    def delete_vocabulary(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM vocabulary WHERE id=?", (id,))
        self.conn.commit()
