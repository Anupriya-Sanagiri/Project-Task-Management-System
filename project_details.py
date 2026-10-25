from database import connect


def get_project_details():

    conn = connect()
    cursor = conn.cursor()

    # Old combined data delete
    cursor.execute("""
        DELETE FROM project_details
    """)

    # Project Details ID reset
    cursor.execute("""
        DELETE FROM sqlite_sequence
        WHERE name = 'project_details'
    """)

    # Fresh combined data insert
    cursor.execute("""
        INSERT INTO project_details
        (
            user_name,
            project_name,
            description,
            task_title,
            status
        )
        SELECT
            users.User_Name,
            projects.name,
            projects.description,
            tasks.title,
            tasks.status
        FROM users
        INNER JOIN projects
            ON users.Id_No = projects.user_id
        INNER JOIN tasks
            ON projects.id = tasks.project_id
    """)

    conn.commit()

    cursor.execute("""
        SELECT
            id,
            user_name,
            project_name,
            description,
            task_title,
            status
        FROM project_details
        ORDER BY id
    """)

    details = cursor.fetchall()

    conn.close()

    return {
        "project_details": details
    }