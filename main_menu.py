from connect import *
from user_management import register_user, login_user  # Import functions

def main():
    """Manages the main menu for the gym progress app."""

    # Connect to the database
    conn = sql.connect("Gym Progress App/Gym-Progress-Tracker/gymDB.db")  # Replace with your desired database name

    logged_in_user = None
    while True:
        print("\nMain Menu:")
        if not logged_in_user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                register_user(conn)  # Call register_user function
            elif choice == '2':
                logged_in_user = login_user(conn)  # Call login_user and store user ID
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

        else:
            # User is logged in, display options for workouts
            print("\nLogged in user:", logged_in_user)  # Show logged-in user ID (optional)
            print("1. Add Workout")
            print("2. View Workouts")
            print("3. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Add workout functionality (assuming in a separate file)
                print("** Feature not yet implemented. Coming soon!**")
            elif choice == '2':
                # View workout functionality (assuming in a separate file)
                print("** Feature not yet implemented. Coming soon!**")
            elif choice == '3':
                logged_in_user = None  # Reset logged_in_user for login again
                print("Logged out.")
            else:
                print("Invalid choice. Please try again.")

    conn.close()  # Close the database connection

if __name__ == "__main__":
    main()
