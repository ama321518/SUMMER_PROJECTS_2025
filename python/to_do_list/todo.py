print("To-Do App starting..")

tasks =[]
while True:
    input_text = input("Enter a task to add/view/exit/remove:")
    if input_text.lower() == "exit":
        print("Exiting the To-Do App.")
        break
    elif input_text.lower() == "add":
        task_to_add = input("Enter the task you want to add: ")
        tasks.append(task_to_add)
        print("Task added:", task_to_add)
    elif input_text.lower() == "view":
        if tasks == []:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, '.', task)
    elif input_text.lower() == "remove":
        if not tasks:
            print("No tasks available to remove.")
            continue
        print("Available tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, '.', task)
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Removed task:", removed_task)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# This helps exit,add,view tasks ,lower case insensitive



            




