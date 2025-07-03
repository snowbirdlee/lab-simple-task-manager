print("(A)dd task\n(D)elete task\n(V)iew tasks\n(Q)uit")
tasks = []
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    tasks = [] # ChatGPT
task_number = 1

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
    elif choice == "v":
        print("These are your tasks:")
        for task in tasks:
            print(f"{task_number}: {task}")
            task_number += 1
        task_number = 1
    elif choice == "q":
        print("Goodbye!")
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n") # ChatGPT
        break
    else:
        print("Invalid choice. Please try again.")