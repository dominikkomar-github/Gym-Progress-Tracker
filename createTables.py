from connect import *


def create_tbls():
    dbCon, dbCursor = db_access()

    dbCursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(255) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        """)

    # Create Workouts table (if not already existing)
    dbCursor.execute("""
        CREATE TABLE IF NOT EXISTS Workouts (
            workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            exercise_name VARCHAR(255) NOT NULL,
            repetitions INTEGER,
            weight DECIMAL(10,2),
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        );
        """)

if __name__ == "__main__":
    create_tbls()
    print("Tables created successfully!")
