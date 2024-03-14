from connect import *

def add_workout(conn, user_id):
    exercise_name = input("Enter exercise name: ")
    repetitions = int(input("Enter repetitions: "))
    weight = float(input("Enter weight in KG: "))


    #print(f"user_id: {user_id}, exercise_name: {exercise_name}, repetitions: {repetitions}, weight: {weight}")
        
    cursor = conn
    cursor.execute("INSERT INTO Workouts (user_id, exercise_name, repetitions, weight) VALUES (?, ?, ?, ?)", (user_id, exercise_name, repetitions, weight))
    conn.commit()
    print("Workout added successfully!")


def view_workouts(conn, user_id):
    """Views all workouts for the given user."""

    cursor = conn.cursor()
    cursor.execute("SELECT workout_id, exercise_name, repetitions, weight FROM Workouts WHERE user_id = ?", (user_id,))
    workouts = cursor.fetchall()  # Fetch all workout data

    if not workouts:
        print("You don't have any recorded workouts yet!")
    else:
        print("Your Workout History:")
        for workout in workouts:
            # Access data using column names (assuming correct order)
            workout_id, exercise_name, repetitions, weight = workout
            print(f"Number: {workout_id} | Exercise: {exercise_name} | Repetitions: {repetitions} | Weight: {weight}")



def delete_workout(conn, user_id):
    """Deletes a workout from the database."""

    try:
        # Assuming you use prepared statements
        cursor = conn.cursor()

        workout_id = int(input("Enter the Number of the workout to delete: "))

        # Double-check query selection (assuming user_id is for filtering)
        cursor.execute("SELECT exercise_name FROM Workouts WHERE workout_id = ? AND user_id = ?", (workout_id, user_id,))
        exercise_name = cursor.fetchone()  # Fetch only the exercise name

        if exercise_name is None:
            print(f"No workout with ID {workout_id} exists.")
        else:
            # Display exercise name in confirmation message
            confirmation = input(f"Are you sure you want to delete the workout '{exercise_name[0]}' (y/n)? ")

            if confirmation.lower() == 'y':
                cursor.execute("DELETE FROM Workouts WHERE workout_id = ? AND user_id = ?", (workout_id, user_id,))
                conn.commit()
                print(f"Workout '{exercise_name[0]}' (Number: {workout_id}) has been deleted.")
            else:
                print("Deletion cancelled.")

    except sql.OperationalError as oe:
        print(f"Error due to: {oe}")


