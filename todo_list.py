tasks = []
def addTask(value):
    tasks.append(value)
def removeTask(value):
    tasks.remove(value)
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
            task = input("Enter task (enter \"stop\" to stop): ")
            if (task!="stop"):
                addTask(task)
            else:
                printTasks()
                break
    elif choice=="2":
        pass
    elif choice=="3":
        pass
    elif choice=="4":
        pass
    elif choice=="0":
        break
    else:
        print("Invalid")
