import sqlite3 as sql

def db_access():
    """Establishes a connection to the database."""
    try:
        with sql.connect("Gym Progress App/Gym-Progress-Tracker/gymDB.db") as dbCon:
            # Return the connection object directly (not the cursor)
            return dbCon
    except sql.OperationalError as oe:
        print(f"Connection failed: {oe}")
        return None  # Return None on failure
