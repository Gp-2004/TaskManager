
import json
import os
import unittest
import zipfile

FILE = "tasks.json"


# ---------- TASK MANAGER ----------
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f'ID: {task["id"]} | '
            f'Title: {task["title"]} | '
            f'Completed: {task["completed"]}'
        )


def update_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Enter new title: ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return

    print("Task not found.")


def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
            return

    print("Task not found.")


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task not found.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


# ---------- UNIT TESTS ----------
class TaskManagerTests(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        tasks.append({
            "id": 1,
            "title": "Study Python",
            "completed": False
        })
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Study Python")

    def test_update_task(self):
        tasks = [{
            "id": 1,
            "title": "Old task",
            "completed": False
        }]
        tasks[0]["title"] = "New task"
        self.assertEqual(tasks[0]["title"], "New task")

    def test_delete_task(self):
        tasks = [{
            "id": 1,
            "title": "Study Python",
            "completed": False
        }]
        tasks = [t for t in tasks if t["id"] != 1]
        self.assertEqual(len(tasks), 0)

    def test_complete_task(self):
        tasks = [{
            "id": 1,
            "title": "Study Python",
            "completed": False
        }]
        tasks[0]["completed"] = True
        self.assertTrue(tasks[0]["completed"])


if __name__ == "__main__":
    unittest.main()
