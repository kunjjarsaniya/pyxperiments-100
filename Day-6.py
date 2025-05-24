# -----------------------------------------------
# Simple CLI To-Do List App
# -----------------------------------------------

# Description: This is a simple command-line based To-Do List application in Python.

# List to store all tasks
todo_list = []

# Function to display menu options
def show_menu():
    print("\n========== TO-DO LIST MENU ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    print("=====================================")

# Function to display all tasks
def view_tasks():
    if not todo_list:
        print("\n📭 Your to-do list is empty!")
    else:
        print("\n📝 Your Tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{index}. {task['title']} [{status}]")

# Function to add a new task
def add_task():
    task_title = input("\n➕ Enter the task: ").strip()
    if task_title:
        todo_list.append({"title": task_title, "done": False})
        print(f"✅ Task '{task_title}' added successfully!")
    else:
        print("⚠️ Task title cannot be empty!")

# Function to remove a task
def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\n🗑️ Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"🗑️ Task '{removed_task['title']}' removed!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")

# Function to mark a task as done
def mark_task_done():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\n✔️ Enter the task number to mark as done: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]['done'] = True
                print(f"🎉 Task '{todo_list[task_num - 1]['title']}' marked as done!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")

# Main program loop
def main():
    print("📋 Welcome to the Simple CLI To-Do List App!")

    while True:
        show_menu()
        choice = input("👉 Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_done()
        elif choice == '5':
            print("👋 Goodbye! Happy Productivity!")
            break
        else:
            print("⚠️ Invalid option. Please choose a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
