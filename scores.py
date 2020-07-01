import sqlite3

class CvScores:
    def __init__(self):
        self.conn = sqlite3.connect('covid-scores.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS scores (date TEXT, name TEXT, score INTEGER)''')
        self.conn.commit()

    def append_score(self, name, score):
        c = self.conn.cursor()
        c.execute('''INSERT INTO scores VALUES (DATETIME('now'), ?, ?)''', (name, score))
        self.conn.commit()

    def quit(self):
        self.conn.close()


if __name__ == "__main__":
    scores_db = CvScores()
    scores_db.append_score("APG", 3000)
    scores_db.quit()
