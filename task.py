from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} - {self.description} - Due: {self.deadline} - Status: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return [str(task) for task in self.tasks]

    def get_upcoming_tasks(self):
        today = datetime.now()
        upcoming_tasks = [task for task in self.tasks if task.deadline >= today and not task.completed]
        return [str(task) for task in upcoming_tasks]

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Management Application")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Upcoming Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline_str = input("Enter deadline (YYYY-MM-DD): ")
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
            task = Task(title, description, deadline)
            manager.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            tasks = manager.view_tasks()
            for task in tasks:
                print(task)

        elif choice == '3':
            upcoming_tasks = manager.get_upcoming_tasks()
            for task in upcoming_tasks:
                print(task)

        elif choice == '4':
            task_title = input("Enter the title of the task to mark as complete: ")
            for task in manager.tasks:
                if task.title == task_title:
                    task.mark_as_complete()
                    print(f"Task '{task_title}' marked as complete.")
                    break
            else:
                print("Task not found.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()