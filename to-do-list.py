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
    remove = get_number("Remove a task: ")
    try: 
        task_list.pop(remove)
    except IndexError:

def print_list():
    for task in task_list:
        print(task)

def menu():
        print("1. Add to list\n2. Remove from list\n3. Print list")
        while True: 
            choice = input("What function would you like to run: ")
            
            if choice == "1":
                add_task()

            elif choice == "2":
                remove_task()

            elif choice == "3":
                print_list()


while True:
    menu()

