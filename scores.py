import sqlite3

class CvScores:
    def __init__(self):
        self.conn = sqlite3.connect('covid-scores.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS scores (date TEXT, name TEXT, score INTEGER)''')
        self.conn.commit()

    def get_scores(self, limit):
        c = self.conn.cursor()
        c.execute("""SELECT name, score FROM scores ORDER BY score DESC LIMIT ?""", (limit,))
        records = c.fetchall()
        scores = []
        for row in records:
            scores.append([row[0], row[1]])
        return scores


    def append_score(self, name, score):
        c = self.conn.cursor()
        c.execute('''INSERT INTO scores VALUES (DATETIME('now'), ?, ?)''', (name, score))
        self.conn.commit()

    def quit(self):
        self.conn.close()


if __name__ == "__main__":
    scores_db = CvScores()
    scores = scores_db.get_scores(2)
    print(scores)

    scores_db.quit()
