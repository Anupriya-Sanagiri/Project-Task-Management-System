from database import connect


def create_project(user_id, name, description=""):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO projects
        (user_id, name, description)
        VALUES (?, ?, ?)
    """, (user_id, name, description))

    conn.commit()

    project_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Project created",
        "project_id": project_id
    }


def get_all_projects():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, description
        FROM projects
    """)

    projects = cursor.fetchall()

    conn.close()

    return {
        "projects": projects
    }