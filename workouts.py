from connect import *

def add_workout(conn, user_id):
    exercise_name = input("Enter exercise name: ")
    repetitions = int(input("Enter repetitions: "))
    weight = float(input("Enter weight in KG: "))


    print(f"user_id: {user_id}, exercise_name: {exercise_name}, repetitions: {repetitions}, weight: {weight}")
        
    cursor = conn
    cursor.execute("INSERT INTO Workouts (user_id, exercise_name, repetitions, weight) VALUES (?, ?, ?, ?)", (user_id, exercise_name, repetitions, weight))
    conn.commit()
    print("Workout added successfully!")

def view_workouts(conn, user_id):
    """Views all workouts for the given user."""

    cursor = conn.cursor()
    cursor.execute("SELECT exercise_name, repetitions, weight FROM Workouts WHERE user_id = ?", (user_id,))
    workouts = cursor.fetchall()  # Fetch all workout data

    if not workouts:
        print("You don't have any recorded workouts yet!")
    else:
        print("Your Workout History:")
        for workout in workouts:
            print(f"Exercise: {workout[0]} | Repetitions: {workout[1]} | Weight: {workout[2]}")
