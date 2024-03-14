This is a gym tracking application. It is used to keep track of your gym progress, you can input the exercise name, the reps, and the weight used. 

Before you can add anything, you need to make an account or login as prompted. Once you're logged in, all the data from the workouts and all the changes to your data will be saved ONLY for your account. 

There is no "I forgot the password" solution as it's only using SQLITE so... don't forget your login/password.

Features:

- Register
- Login
- Add a workout
- View Workouts
- Update Workouts
- Delete Workouts

Password Hashing:

To make it seem secure even when someone has access to the database file, the password is hashed using "bcrypt".


TO-DO:

- Make a GUI
- Possibly host the database online so it's not local
- Make it run from a single .exe file once GUI is implemented
