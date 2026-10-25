from fastapi import FastAPI

from database import create_tables

from auth import register_user
from auth import login_user
from auth import logout_user

from projects import create_project
from projects import get_all_projects

from tasks import create_task
from tasks import get_all_tasks
from tasks import update_task_status

from project_details import get_project_details


app = FastAPI(title="Project & Task Management API")


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

create_tables()


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Project Management API"
    }


# ==========================================
# REGISTER
# ==========================================

@app.post("/register")
def register(User_Name: str, Password: str):

    return register_user(User_Name, Password)


# ==========================================
# LOGIN
# ==========================================

@app.post("/login")
def login(User_Name: str, Password: str):

    return login_user(User_Name, Password)


# ==========================================
# CREATE PROJECT
# ==========================================

@app.post("/projects")
def project_create(
    user_id: int,
    name: str,
    description: str = ""
):

    return create_project(
        user_id,
        name,
        description
    )


# ==========================================
# VIEW PROJECTS
# ==========================================

@app.get("/projects")
def projects():

    return get_all_projects()


# ==========================================
# CREATE TASK
# ==========================================

@app.post("/tasks")
def task_create(
    project_id: int,
    title: str
):

    return create_task(
        project_id,
        title
    )


# ==========================================
# VIEW TASKS
# ==========================================

@app.get("/tasks")
def tasks():

    return get_all_tasks()


# ==========================================
# UPDATE TASK STATUS
# ==========================================

@app.put("/tasks/{task_id}")
def task_update(
    task_id: int,
    status: str
):

    return update_task_status(
        task_id,
        status
    )


# ==========================================
# LOGOUT
# ==========================================

@app.post("/logout")
def logout():

    return logout_user()


# ==========================================
# PROJECT DETAILS
# ==========================================

@app.get("/project-details")
def project_details():

    return get_project_details()