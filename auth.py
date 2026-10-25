from database import connect


def register_user(User_Name, Password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (User_Name, Password)
        VALUES (?, ?) """, (User_Name, Password))

    conn.commit()
    conn.close()

    return { "message": "Registration successful" }


def login_user(User_Name, Password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Id_No
        FROM users
        WHERE User_Name = ? AND Password = ? """, (User_Name, Password))

    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            "message": "Login successful",
            "user_id": user[0]
        }

    return {
        "message": "Invalid username or Password"
    }




def logout_user():

    return {
        "message": "Logout successful"
    }