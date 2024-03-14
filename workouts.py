from connect import *

def add_workout(conn, user_id):
    exercise_name = input("Enter exercise name: ")
    repetitions = int(input("Enter repetitions: "))
    weight = float(input("Enter weight (decimal): "))

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Workouts (user_id, exercise_name, repetitions, weight) VALUES (?, ?, ?, ?)", (user_id, exercise_name, repetitions, weight))
    conn.commit()
    print("Workout added successfully!")

def view_workouts(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Workouts WHERE user_id = ?", (user_id,))
    workouts = cursor.fetchall()

    if not workouts:
        print("No workouts found for this user.")
    else:
        print("Your Workouts:")
        for workout in workouts:
            print(f"Exercise: {workout[2]} | Repetitions: {workout[3]} | Weight: {workout[4]}")

# ... Implement functions for updating and deleting workouts (optional)