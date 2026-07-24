tasks = []
def printTasks():
    print("To-Do List:")
    for item in tasks:
        if item["completed"]==True:
            print(str(tasks.index(item)+1)+". [✓] "+item["task"])
        else:
            print(str(tasks.index(item)+1)+". [ ] "+item["task"])
def addTask(value):
    tasks.append({"task" : value, "completed" : False})
def markComplete(value):
    if ((int(value))<=len(tasks)):
        tasks[int(value)-1]["completed"]=True
    else:
        print("Task not in to-do list")
def removeTask(value):
    if ((int(value))<=len(tasks)):
        del tasks[int(value)-1]
    else:
        print("Task not in to-do list")
def saveTasks():
    pass
def loadTasks():
    pass
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
    elif choice=="3":
        print("Item Completion Mode")
        printTasks()
        while True:
            task = input("Enter the number of the task to mark complete (enter \"stop\" to stop): ")
            if (task!="stop"):
                markComplete(task)
            else:
                break
    elif choice=="4":
        print("Item Removal Mode")
        printTasks()
        while True:
            task = input("Enter the number of the task to remove (enter \"stop\" to stop): ")
            if (task!="stop"):
                removeTask(task)
            else:
                break
    elif choice=="4":
        pass
    elif choice=="0":
        break
    else:
        print("Invalid")
