import sys
import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date):
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
        print("Task added successfully!")

    def remove_task(self, index):
        try:
            del self.tasks[index]
            print("Task removed successfully!")
        except IndexError:
            print("Task index out of range!")

    def mark_completed(self, index):
        try:
            self.tasks[index]["completed"] = True
            print("Task marked as completed!")
        except IndexError:
            print("Task index out of range!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i + 1}. Task: {task['task']} | Priority: {task['priority']} | Due Date: {task['due_date']} | Status: {status}")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)
        print("Tasks saved successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found.")

def main():
    todo_list = ToDoList()

    # Load tasks from file if available
    filename = "tasks.json"
    todo_list.load_tasks(filename)

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Save Tasks\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(task, priority, due_date)
        elif choice == '2':
            index = int(input("Enter index of task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter index of task to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            todo_list.save_tasks(filename)
        elif choice == '6':
            print("Exiting program...")
            todo_list.save_tasks(filename)  # Save tasks before exiting
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
