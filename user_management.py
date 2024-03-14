from connect import *
import getpass
import bcrypt  # For secure password hashing

def register_user(conn):
    """Registers a new user in the database."""

    username = input("Enter username: ")
    email = input("Enter email address: ")  # Added line to get email
    password = getpass.getpass("Enter password: ")

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor = conn.cursor()  # Create a cursor object using the connection
    cursor.execute("INSERT INTO Users (username, hashed_password, email) VALUES (?, ?, ?)", (username, hashed_password, email))
    conn.commit()
    print("User registered successfully!")


def login_user(cursor):
    """Logs in a user and returns their user ID if successful."""

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Use the cursor object passed as an argument
    cursor.execute("SELECT user_id, hashed_password FROM Users WHERE username = ?", (username,))
    user_data = cursor.fetchone()

    if not user_data:
        print("Invalid username or password.")
        return None  # Return None on failed login

    # Verify password hash using bcrypt
    if bcrypt.checkpw(password.encode('utf-8'), user_data[1]):
        print("Login successful!")
        return user_data[0]  # Return user ID on successful login
    else:
        print("Invalid password.")
        return None  # Return None on failed password verification
