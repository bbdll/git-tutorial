"""A small command-line task tracker."""

import sys

from storage import load_tasks, save_tasks


def add_task(title):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def list_tasks():
    """Print every task with its number."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


def complete_task(number):
    """Mark the task with the given number as done."""
    tasks = load_tasks()

    if number < 1 or number > len(tasks):
        print(f"There is no task number {number}.")
        return

    task = tasks[number - 1]
    task["done"] = True
    save_tasks(tasks)
    print(f"Completed: {task['title']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python tasks.py [add|list|done] ...")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        complete_task(int(sys.argv[2]))
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
