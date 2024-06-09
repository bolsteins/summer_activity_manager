class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added!")

    def remove_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def manage(self):
        while True:
            choice = int(input("1. Add task\n2. Remove task\n3. View tasks\n4. Back\nChoose an option: "))
            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.remove_task()
            elif choice == 3:
                self.view_tasks()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
