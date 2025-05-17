import sqlite3
DB_NAME = 'schedule.db'
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def get_schedule_for_day(day):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT time, subject FROM schedule WHERE day = ? ORDER BY time', (day,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_lesson(day, time, subject):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO schedule (day, time, subject) VALUES (?, ?, ?)', (day, time, subject))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
