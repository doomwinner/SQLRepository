import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

cr.execute("""
           CREATE TABLE IF NOT EXISTS movies (
           id INTERGER PRIMARY KEY,
           title TEXT,
           director TEXT,
           year INTERGER,
           genre TEXT)
           """)