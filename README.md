# Task Tracker

A Python command-line task tracker for Git practice. Tasks are saved in `tasks.json`, which Git ignores.

## Git practice

The commit history includes feature branches, merges, a merge conflict resolution,
the `v1.0` tag, and a reverted change.

## Usage

```sh
python3 tasks.py add "Buy milk"           # add a task
python3 tasks.py add "Call the bank" high # add a high priority task
python3 tasks.py list                     # show all tasks
python3 tasks.py done 1                   # mark task 1 as completed
```

Use `high` or `low` to set a priority. The default is `normal`.
`done` takes the task number shown by `list`.
