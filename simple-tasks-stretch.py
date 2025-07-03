print("(A)dd task\n(D)elete task\n(C)omplete task\n(V)iew tasks\n(E)mpty completed tasks\n(Q)uit")
tasks = []
completed_tasks = []
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    tasks = [] # ChatGPT
task_number = 1
completed_task_number = 1

while True:
    choice = input("What would you like to do?").lower().strip()
    if choice == "a":
        add_task = input("What task would you like to add? ")
        tasks.append(add_task)
        print("Task added.")

    elif choice == "d":
        while True:
            try:
                if len(tasks) == 0:
                    print("You do not have any tasks. Please add one.")
                    break
                delete_task = int(input("What task number would you like to delete? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if delete_task in range(1, len(tasks) + 1): # autofilled
                del tasks[delete_task - 1] # ChatGPT
                print("Task deleted.")
                break
            else:
                print("Task not found.")
                continue

    elif choice == "c": # entire section autofilled
        while True:
            try:
                if len(tasks) == 0:
                    print("You do not have any tasks. Please add one.")
                    break
                complete_task = int(input("What task number would you like to complete? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if complete_task in range(1, len(tasks) + 1):
                completed_tasks.append(tasks[complete_task - 1])
                del tasks[complete_task - 1]
                print("Task completed.")
                break
            else:
                print("Task not found.")
                continue

    elif choice == "e":
        completed_tasks.clear()
        print("Completed tasks cleared.")

    elif choice == "v":
        if len(tasks) == 0:
            print("You do not have any tasks.")
        else:
            print("These are your tasks:")
            for task in tasks:
                print(f"{task_number}: {task}")
                task_number += 1
            task_number = 1
        if len(completed_tasks) == 0: # autofilled
            print("You do not have any completed tasks.")
        else:
            print("These are your completed tasks:")
            for completed_task in completed_tasks:
                print(f"{completed_task_number}: {completed_task}")
                completed_task_number += 1
            completed_task_number = 1 
        
    elif choice == "q":
        print("Goodbye!")
        with open("tasks.txt", "w") as file: # autofilled/ChatGPT
            for task in tasks:
                file.write(task + "\n")
        with open("completed_tasks.txt", "w") as file:
            for task in completed_tasks:
                file.write(task + "\n")
        break
    
    else:
        print("Invalid choice. Please try again.")