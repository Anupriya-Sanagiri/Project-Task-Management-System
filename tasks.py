from database import connect


def create_task(project_id, title):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (project_id, title, status)
        VALUES (?, ?, ?)
    """, (project_id, title, "TODO"))

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Task created",
        "task_id": task_id,
        "status": "TODO"
    }


def get_all_tasks():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, project_id, title, status
        FROM tasks
    """)

    tasks = cursor.fetchall()

    conn.close()

    return {
        "tasks": tasks
    }


def update_task_status(task_id, status):

    allowed_status = [
        "TODO",
        "IN_PROGRESS",
        "REVIEW",
        "DONE"
    ]

    if status not in allowed_status:
        return {
            "message": "Invalid status",
            "allowed_status": allowed_status
        }

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (status, task_id))

    conn.commit()
    conn.close()

    return {
        "message": "Task status updated",
        "task_id": task_id,
        "status": status
    }
    
    
    def update_task_project(task_id, project_id):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE tasks
        SET project_id = ?
        WHERE id = ?
    """, (project_id, task_id))

    conn.commit()
    conn.close()

    return {
        "message": "Task project updated"
    }