import sqlite3 as sql

# create a function to that creates a database file
def db_access():
    try:  # try and execute the code within the try block
        # use context manager to access and automatically tear down resource(s)
        # invoke/call the sqlite connect function
        # create db file if it does not exist(use db if exist)
        with sql.connect("Gym Progress App/Gym-Progress-Tracker/gymDB.db") as dbCon:

            # create a variable called dbCursor and initialise with cursor() method from the connect function
            dbCursor = dbCon.cursor()  # cursor() method is used to cal the execute method

            return dbCon, dbCursor
    except sql.OperationalError as oe:  # raise sql error
        # use the error raise to handle the exception/error
        print(f"Connection failed: {oe}")


# if this is the main file 'connect.py' run the function,
# but if this file is imported in another don't automaticallly run the function
if __name__ == "__main__":
    db_access()

