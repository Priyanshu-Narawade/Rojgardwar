import sqlite3

def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT UNIQUE,
            village TEXT,
            education TEXT,
            interests TEXT,
            job_type TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()
