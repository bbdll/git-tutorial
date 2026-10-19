"""Reading and writing the task list to disk."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    """Return the saved tasks, or an empty list if there is no data yet."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the task list back to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
