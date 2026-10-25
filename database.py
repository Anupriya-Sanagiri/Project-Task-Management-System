import sqlite3


DATABASE_NAME = "Project.db"


def connect():
    return sqlite3.connect(DATABASE_NAME, timeout=30)


def create_tables():

    conn = connect()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            Id_No INTEGER PRIMARY KEY AUTOINCREMENT,
            User_Name TEXT UNIQUE NOT NULL,
            Password TEXT NOT NULL
        )
    """)

    # Projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            description TEXT
        )
    """)

    # Tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'TODO'
        )
    """)

    # Combined project details table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            project_name TEXT,
            description TEXT,
            task_title TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()