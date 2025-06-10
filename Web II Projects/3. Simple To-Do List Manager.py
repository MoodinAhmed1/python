# Build a command-line to-do list application that: - Adds tasks - Views tasks - Deletes tasks - Marks tasks as completed 
# Use lists, loops, and conditionals. 

to_do_list = []

def display_task():
    global to_do_list
    
    for index, toDo in enumerate(to_do_list):
        print(f"{index + 1}. {toDo['name']} - {toDo['status']}")
        
def add_task(task):
    global to_do_list
    
    task = {
        "name" : task,
        "status" : "pending"
    }
    
    to_do_list.append(task)
    print(f"{task['name']} has been added")
    
def delete_task(index):
    global to_do_list

    task_name = to_do_list[index]['name']
    to_do_list = to_do_list[:index] + to_do_list[index + 1:]
    print(f"{task_name} has been deleted")
    
def mark_as_done(index):
    global to_do_list

    to_do_list[index]["status"] = "completed"
    print(f"{to_do_list[index]['name']} has been marked done")
    
def start_program():
    print("1. Adds tasks")
    print("2. Views tasks")
    print("3. Deletes tasks")
    print("4. Mark tasks as completed")
    print("5. Exit")
        
    while True:
        userInput = input("\nEnter a number : ")
        
        if userInput == "1" :
            task = input("add task : ")
            add_task(task)
            
        elif userInput == "2" : 
            print(display_task())
            
        elif userInput == "3" : 
            index = int(input("remove task (enter number) : "))
            delete_task(index - 1)
        
        elif userInput == "4" :
            index = int(input("mark as complete (enter number) : "))
            mark_as_done(index - 1)
        
        elif userInput == "5":
            return

        else: 
            print("enter a valid number!")


start_program()