import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Project & Task Management",
    page_icon="📋"
)

st.title("📋 Project & Task Management")


# ==========================================
# LOGIN SESSION
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""


# ==========================================
# MENU
# ==========================================

if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Menu",
        ["Register", "Login"]
    )

else:

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Create Project",
            "Create Task",
            "Projects",
            "Tasks",
            "Update Task Status",
            "Project Details",
            "Logout"
        ]
    )


# ==========================================
# REGISTER
# ==========================================

if menu == "Register":

    st.header("Register")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if username and password:

            response = requests.post(
                f"{API_URL}/register",
                params={
                    "User_Name": username,
                    "Password": password
                }
            )

            if response.status_code == 200:

                st.success(
                    "Registration successful"
                )

            else:

                st.error(response.text)

        else:

            st.warning(
                "Please enter username and password"
            )


# ==========================================
# LOGIN
# ==========================================

elif menu == "Login":

    st.header("Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        response = requests.post(
            f"{API_URL}/login",
            params={
                "User_Name": username,
                "Password": password
            }
        )

        data = response.json()

        if "user_id" in data:

            st.session_state.logged_in = True

            st.session_state.user_id = data["user_id"]

            st.session_state.username = username

            st.success("Login successful")

            st.rerun()

        else:

            st.error(
                "Invalid username or password"
            )


# ==========================================
# CREATE PROJECT
# ==========================================

elif menu == "Create Project":

    st.header("Create Project")

    name = st.text_input("Project Name")

    description = st.text_area("Project Description")

    if st.button("Create Project"):

        response = requests.post(
            f"{API_URL}/projects",
            params={
                "user_id": st.session_state.user_id,
                "name": name,
                "description": description
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.success(
                f"Project created successfully. ID: {data['project_id']}"
            )

        else:

            st.error(
                f"Error: {response.status_code}"
            )

            st.error(
                response.text
            )


# ==========================================
# CREATE TASK
# ==========================================

elif menu == "Create Task":

    st.header("Create Task")

    project_id = st.number_input(
        "Project ID",
        min_value=1,
        step=1
    )

    title = st.text_input("Task Title")

    if st.button("Create Task"):

        response = requests.post(
            f"{API_URL}/tasks",
            params={
                "project_id": project_id,
                "title": title
            }
        )

        data = response.json()

        if response.status_code == 200:

            st.success(
                f"Task created successfully. ID: {data['task_id']}"
            )

            st.info("Status: TODO")

        else:

            st.error(response.text)


# ==========================================
# VIEW PROJECTS
# ==========================================

elif menu == "Projects":

    st.header("Projects")

    response = requests.get(
        f"{API_URL}/projects"
    )

    data = response.json()

    projects = data.get("projects", [])

    if projects:

        for project in projects:

            st.write(
                f"**Project ID:** {project[0]}"
            )

            st.write(
                f"**Project:** {project[1]}"
            )

            st.write(
                f"**Description:** {project[2]}"
            )

            st.divider()

    else:

        st.info("No projects found")


# ==========================================
# VIEW TASKS
# ==========================================

elif menu == "Tasks":

    st.header("Tasks")

    response = requests.get(
        f"{API_URL}/tasks"
    )

    data = response.json()

    tasks = data.get("tasks", [])

    if tasks:

        for task in tasks:

            st.write(
                f"**Task ID:** {task[0]}"
            )

            st.write(
                f"**Project ID:** {task[1]}"
            )

            st.write(
                f"**Task:** {task[2]}"
            )

            st.write(
                f"**Status:** {task[3]}"
            )

            st.divider()

    else:

        st.info("No tasks found")


# ==========================================
# UPDATE TASK STATUS
# ==========================================

elif menu == "Update Task Status":

    st.header("Update Task Status")

    task_id = st.number_input(
        "Task ID",
        min_value=1,
        step=1
    )

    status = st.selectbox(
        "Select Status",
        [
            "TODO",
            "IN_PROGRESS",
            "REVIEW",
            "DONE"
        ]
    )

    if st.button("Update Status"):

        response = requests.put(
            f"{API_URL}/tasks/{task_id}",
            params={
                "status": status
            }
        )

        data = response.json()

        if response.status_code == 200:

            st.success(
                f"Task {task_id} status updated to {status}"
            )

        else:

            st.error(response.text)


# ==========================================
# PROJECT DETAILS
# ==========================================

elif menu == "Project Details":

    st.header("Project Details")

    response = requests.get(
        f"{API_URL}/project-details"
    )

    data = response.json()

    details = data.get(
        "project_details",
        []
    )

    if details:

        for row in details:

            st.write(
                f"**ID:** {row[0]}"
            )

            st.write(
                f"**User:** {row[1]}"
            )

            st.write(
                f"**Project:** {row[2]}"
            )

            st.write(
                f"**Description:** {row[3]}"
            )

            st.write(
                f"**Task:** {row[4]}"
            )

            st.write(
                f"**Status:** {row[5]}"
            )

            st.divider()

    else:

        st.info(
            "No project details found"
        )


# ==========================================
# LOGOUT
# ==========================================

elif menu == "Logout":

    st.header("Logout")

    if st.button("Logout"):

        requests.post(
            f"{API_URL}/logout"
        )

        st.session_state.logged_in = False

        st.session_state.user_id = None

        st.session_state.username = ""

        st.success(
            "Logout successful"
        )

        st.rerun()