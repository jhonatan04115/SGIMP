import sqlite3
import os

def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database.sqlite')
    return db_path

def get_connection():
    return sqlite3.connect(get_db_path())

def init_db():
    conn = get_connection()
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
