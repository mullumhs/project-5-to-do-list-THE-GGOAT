"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
task_list = ["Kwila"]
def get_number():
    while True:
        num = input
        try:
            int(num)
            is_dig = True
            return int(num)
        except ValueError:
            is_dig = False
            print("Invaild try again?")

def add_task():
    print_list()
    task_list.append(input("Enter a task: "))

def remove_task():
    print_list()
    try: 
        remove = get_number("Remove a task: ")
        task_list.pop(remove)
    except:
       ("ENter vaild choice") 

def print_list():
    for task in task_list:
        print(task)

def menu():
        print_list()
        print("1. Add to list\n2. Remove from list\n3. Print list\n4. Edit task")
        while True: 
            choice = input("What function would you like to run: ")
            
            if choice == "1":
                add_task()

            elif choice == "2":
                remove_task()

            elif choice == "3":
                print_list()
            
            elif choice == "4":
                edit_task()

def edit_task():
    print_list()
    var = input("what task to edit: ")
    var_num = task_list.index(var)
    change = input("Enter edited task:")
    try:
        task_list[var_num] = change
        print_list()
    except:
        print("Invaild Input, try again")


while True:
    menu()
