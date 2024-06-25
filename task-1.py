import json
import os

# Load tasks from JSON file
def load_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    else:
        return []

# Save tasks to JSON file
def save_tasks(tasks, file_name):
    with open(file_name, 'w') as f:
        json.dump(tasks, f, indent=4)

# Create a new task
def create_task(tasks, task_name, due_date):
    task = {'name': task_name, 'due_date': due_date, 'completed': False}
    tasks.append(task)
    return tasks

# Update a task
def update_task(tasks, task_id, task_name=None, due_date=None, completed=None):
    task = tasks[task_id]
    if task_name:
        task['name'] = task_name
    if due_date:
        task['due_date'] = due_date
    if completed is not None:
        task['completed'] = completed
    return tasks

# Delete a task
def delete_task(tasks, task_id):
    del tasks[task_id]
    return tasks

# Mark a task as completed
def complete_task(tasks, task_id):
    tasks[task_id]['completed'] = True
    return tasks

# Print tasks
def print_tasks(tasks):
    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"{i+1}. {task['name']} - Due: {task['due_date']} - {status}")

def main():
    file_name = 'tasks.json'
    tasks = load_tasks(file_name)

    while True:
        print("\nTo-Do List:")
        print_tasks(tasks)
        print("\nOptions:")
        print("1. Create a new task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            tasks = create_task(tasks, task_name, due_date)
            save_tasks(tasks, file_name)
        elif choice == '2':
            task_id = int(input("Enter task ID: ")) - 1
            task_name = input("Enter new task name (or press Enter to skip): ")
            due_date = input("Enter new due date (or press Enter to skip): ")
            completed = input("Mark as completed? (y/n): ")
            tasks = update_task(tasks, task_id, task_name, due_date, completed.lower() == 'y')
            save_tasks(tasks, file_name)
        elif choice == '3':
            task_id = int(input("Enter task ID: ")) - 1
            tasks = delete_task(tasks, task_id)
            save_tasks(tasks, file_name)
        elif choice == '4':
            task_id = int(input("Enter task ID: ")) - 1
            tasks = complete_task(tasks, task_id)
            save_tasks(tasks, file_name)
        elif choice == '5':
            break
        else:
            print("Invalid option. Try again!")

if __name__ == '__main__':
    main()
