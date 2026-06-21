import sqlite3


def create_connection():
    conn = sqlite3.connect("database/phishshield.db")
    return conn


def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        sender TEXT,

        risk_level TEXT,

        risk_score INTEGER
    )
    """)

    conn.commit()
    conn.close()

def save_scan(sender, risk_level, risk_score):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scan_history
    (sender, risk_level, risk_score)
    VALUES (?, ?, ?)
    """,
    (sender, risk_level, risk_score))

    conn.commit()
    conn.close()