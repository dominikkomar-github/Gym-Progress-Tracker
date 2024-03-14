import addrecord, readrecords, updaterecord, deleterecord, report

def read_file(file_path):
    try: 
        with open(file_path) as open_file:
            rf = open_file.read()
            return rf
    
    except FileNotFoundError as not_found:
        print(f"File not found {not_found}")
        

def songs_menu():
    option = 0
    options_list = ["1", "2", "3", "4", "5", "6"]
    menu_choices = read_file("Exercises/Week2/Python-Database-CRUD/dbMenu.txt")
    
    while option not in options_list:
        print(menu_choices)
        option = input("Enter a choice from the menu: ")
        
        if option not in options_list:
            print(f"{option} not a valid choice.")
            
    return option

main_program = True

while main_program:
    menu_options = songs_menu()
    
    if menu_options == "1":
        readrecords.read_all_songs()
        
    elif menu_options == "2":
        addrecord.insert_record()
        
    elif menu_options == "3":
        updaterecord.update_record()
        
    elif menu_options == "4":
        deleterecord.delete_song()
        
    elif menu_options == "5":
        report.report()
        
    else:
        main_program = False