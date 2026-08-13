import json
import csv
from datetime import datetime

FILENAME = "todos.json"

# --- STEP 1: App start hote hi JSON file se data load karna ---
TODOS = []
try:
    with open(FILENAME, "r") as f:
        TODOS = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    TODOS = []

print("------ ADVANCED TODOS APPLICATION ------")

# --- STEP 2: Main Procedural Loop ---
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task / Mark Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Sort Tasks")
    print("7. Export to CSV")
    print("8. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1': # ------------- Add Task
        task_name = input("Enter task name: ").strip()
        if not task_name:
            print("Error: Task name empty nahi ho sakta!")
            continue

        priority = input("Enter Priority (High/Medium/Low): ").strip().capitalize()
        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"

        due_date = input("Enter Due Date (YYYY-MM-DD) or press Enter to skip: ").strip()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Auto-increment ID logic
        new_id = str(len(TODOS) + 1)

        TODOS.append({
            "ID": new_id,
            "task": task_name,
            "priority": priority,
            "due_date": due_date if due_date else "N/A",
            "created_at": created_at,
            "is_completed": False
        })

        # Save to JSON file
        with open(FILENAME, "w") as f:
            json.dump(TODOS, f, indent=4)

        print("Task added successfully!")

    elif choice == '2': # ------------- View Tasks
        if not TODOS:
            print("Currently no tasks available.")
        else:
            print("\n--- YOUR TASK LIST ---")
            for item in TODOS:
                status = "Completed" if item["is_completed"] else "Pending"
                print(f"ID: {item['ID']} | Task: {item['task']} | Priority: {item['priority']} | Due: {item['due_date']} | Status: {status}")

    elif choice == '3': # ------------- Update Task / Status
        if not TODOS:
            print("No task available to update.")
        else:
            print("\n1. Edit Task Name\n2. Mark as Completed")
            sub_choice = input("Enter sub-choice: ").strip()
            task_id = input("Enter task ID: ").strip()
            is_found = False

            for item in TODOS:
                if item['ID'] == task_id:
                    is_found = True
                    if sub_choice == '1':
                        new_name = input("Enter new task name: ").strip()
                        if new_name:
                            item['task'] = new_name
                            print("Task updated!")
                        else:
                            print("Task name cannot be empty!")
                    elif sub_choice == '2':
                        item['is_completed'] = True
                        print("Task marked as completed!")
                    break

            if not is_found:
                print("Task ID not found!")
            else:
                with open(FILENAME, "w") as f:
                    json.dump(TODOS, f, indent=4)

    elif choice == '4': # ------------- Delete Task
        if not TODOS:
            print("No task available to delete.")
        else:
            task_id = input("Enter task ID to delete: ").strip()
            is_found = False
            for item in TODOS:
                if item['ID'] == task_id:
                    is_found = True
                    TODOS.remove(item)
                    print("Task deleted successfully!")
                    break

            if not is_found:
                print("Task ID not found!")
            else:
                with open(FILENAME, "w") as f:
                    json.dump(TODOS, f, indent=4)

    elif choice == '5': # ------------- Search Task
        query = input("Enter search keyword: ").lower().strip()
        results = [item for item in TODOS if query in item['task'].lower()]

        if results:
            print("\n--- SEARCH RESULTS ---")
            for item in results:
                status = "Completed" if item["is_completed"] else "Pending"
                print(f"ID: {item['ID']} | Task: {item['task']} | Status: {status}")
        else:
            print("No matching tasks found.")

    elif choice == '6': # ------------- Sort Tasks
        if not TODOS:
            print("No tasks to sort.")
        else:
            print("\nSort by: 1. Priority (High to Low) | 2. Completion Status")
            sort_choice = input("Enter option: ").strip()

            if sort_choice == '1':
                priority_order = {"High": 1, "Medium": 2, "Low": 3}
                sorted_list = sorted(TODOS, key=lambda x: priority_order.get(x['priority'], 4))
            elif sort_choice == '2':
                sorted_list = sorted(TODOS, key=lambda x: x['is_completed'], reverse=True)
            else:
                sorted_list = TODOS

            for item in sorted_list:
                status = "Completed" if item["is_completed"] else "Pending"
                print(f"ID: {item['ID']} | Priority: {item['priority']} | Task: {item['task']} | Status: {status}")

    elif choice == '7': # ------------- Export to CSV
        if not TODOS:
            print("No data to export.")
        else:
            try:
                with open("exported_todos.csv", "w", newline="") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=["ID", "task", "priority", "due_date", "created_at", "is_completed"])
                    writer.writeheader()
                    writer.writerows(TODOS)
                print("Data exported to 'exported_todos.csv' successfully!")
            except Exception as e:
                print(f"Export failed: {e}")

    elif choice == '8': # ------------- Exit
        print("Exiting application. Goodbye!")
        break

    else:
        print("Invalid choice, please select between 1-8.")