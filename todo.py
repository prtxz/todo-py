import csv

# File where tasks will be stored
FILE_NAME = "tasks.csv"

# Function to load tasks from CSV
def load_tasks():
    try:
        with open(FILE_NAME, newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Function to save tasks to CSV
def save_tasks(tasks):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        print("\nTo-Do List:")
        for i, (task, status) in enumerate(tasks, 1):
            print(f"{i}. {task} - {'Done' if status == '1' else 'Pending'}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append([task, '0'])  # '0' means task is pending
    save_tasks(tasks)
    print("Task added successfully!")

# Function to mark a task as done
def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index][1] = '1'  # Mark as done
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: 1. View  2. Add  3. Mark Done  4. Delete  5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
