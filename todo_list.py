tasks = []
def printTasks():
    print("To-Do List:")
    #for i in range(1,len(tasks)):
    for item in tasks:
        print(str(tasks.index(item)+1)+". [ ] "+item["task"])
def addTask(value):
    tasks.append({"task" : value, "completed" : False})
def removeTask(value):
    if value in tasks:
        tasks.remove(value)
    else:
        print("Task not in to-do list")
def markComplete(value):
    if value in tasks:
        pass
    else:
        print("Task not in to-do list")
while True:
    print("\nMake a to-do list!")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Save")
    print("6. Load")
    print("0. Exit")
    choice = input("Enter a number: ")
    if choice=="1":
        printTasks()
    elif (choice=="2"):
        print("Item Entry Mode")
        while True:
            task = input("Enter task to add (enter \"stop\" to stop): ")
            if (task!="stop"):
                addTask(task)
            else:
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
        print("Item Completion Mode")
        while True:
            task = input("Enter task to mark complete (enter \"stop\" to stop): ")
            if (task!="stop"):
                #for item in tasks:
                    #if item==task:
                        #item=markComplete(task)
                markComplete(task)
            else:
                printTasks()
                break
    elif choice=="4":
        pass
    elif choice=="0":
        break
    else:
        print("Invalid")
