tasks = []
def addTask(value):
    tasks.append(value)
def removeTask(value):
    if value in tasks:
        tasks.remove(value)
    else:
        print("Task not in to-do list")
def markComplete():
    pass
def printTasks():
    print("To-Do List:")
    for item in tasks:
        print("\t- "+item+"\n")
while True:
    print("\nMake a to-do list!")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Complete")
    print("4. Save Tasks")
    print("0. Exit")
    choice = input("Enter a number: ")
    if (choice=="1"):
        print("Item Entry Mode")
        while True:
            task = input("Enter task to add (enter \"stop\" to stop): ")
            if (task!="stop"):
                addTask(task)
            else:
                printTasks()
                break
    elif choice=="2":
        print("Item Removal Mode")
        while True:
            task = input("Enter task to remove (enter \"stop\" to stop): ")
            if (task!="stop"):
                removeTask(task)
            else:
                printTasks()
                break
    elif choice=="3":
        pass
    elif choice=="4":
        pass
    elif choice=="0":
        break
    else:
        print("Invalid")
