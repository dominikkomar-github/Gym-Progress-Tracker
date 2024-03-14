from connect import *
from user_management import register_user, login_user
from workouts import add_workout, view_workouts, delete_workout

def main():
    """Manages the main menu of the Gym Progress App."""

    print("Welcome to the Gym Progress App!")

    while True:
        choice = input("""
        1. Register
        2. Login
        3. Exit
        """)

        if choice == '1':
            # Registration functionality
            conn = db_access()  # Establish database connection
            register_user(conn)  # Call register_user function
            conn.close()  # Close the connection after registration

        elif choice == '2':
            # Login functionality
            conn = db_access()  # Establish database connection
            cursor = conn.cursor()  # Create a cursor object
            logged_in_user = login_user(cursor)  # Call login_user and pass cursor

            if logged_in_user:
                # User successfully logged in
                while True:
                    sub_choice = input("""
                    Logged in as User ID: {}
                    1. View Workouts
                    2. Add Workout
                    3. Update Workout
                    4. Delete Workout
                    5. Logout
                    """.format(logged_in_user))

                    if sub_choice == '1':
                        view_workouts(conn, logged_in_user)  # View workouts

                    elif sub_choice == '2':
                        add_workout(conn, logged_in_user)  # Add workout
                        
                    elif sub_choice == '3':
                        add_workout(conn, logged_in_user)  # Update workout
                    
                    elif sub_choice == '4':
                        delete_workout(conn, logged_in_user)  # Delete workout

                    elif sub_choice == '5':
                        print("Logged out successfully!")
                        break  # Exit inner loop (logout)

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Login failed. Please try again.")

            cursor.close()  # Close the cursor after login flow
            conn.close()  # Close the connection after login flow

        elif choice == '3':
            print("Exiting the Gym Progress App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
