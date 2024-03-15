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
        cursor = conn.cursor()
        workout_id = int(input("Enter the Number of the workout to delete: "))

        # Double-check query selection
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
        
        

def update_workout(conn, user_id):
    """Updates an existing workout in the database."""

    try:
        cursor = conn.cursor()

        workout_id = int(input("Enter the Number of the workout to update: "))

        # Check if the workout exists before updating
        cursor.execute("SELECT * FROM Workouts WHERE workout_id = ? AND user_id = ?", (workout_id, user_id,))
        row = cursor.fetchone()

        if not row:  # Check if row is empty (no record found)
            raise ValueError(f"Workout with ID {workout_id} not found.")
        
        # Field choices for update (modify as needed)
        field_choices = {
            "1": "exercise_name",
            "2": "repetitions",
            "3": "weight",
        }

        choice = input(f"Update (Exercise Name, Repetitions, Weight) (1/2/3): ")

        if choice in field_choices:
            new_value = input(f"Enter new {field_choices[choice]}: ")
            # Update query using chosen field and user ID filter
            cursor.execute(
                f"UPDATE Workouts SET {field_choices[choice]} = ? WHERE workout_id = ? AND user_id = ?",
                (new_value, workout_id, user_id),
            )
            conn.commit()
            print("Workout information updated successfully.")
        else:
            print("Invalid choice. Please try again.")

    except (ValueError, sql.OperationalError) as oe:
        print(f"Error: {oe}")