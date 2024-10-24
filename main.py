import sys
from TaskManager import TaskManager

def main():
    task_manager = TaskManager()

    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
        else:
            description = " ".join(sys.argv[2:])
            task_manager.add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <task_id> <new_description>")
        else:
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            task_manager.update_task(task_id, new_description)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <task_id>")
        else:
            task_id = int(sys.argv[2])
            task_manager.delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <task_id>")
        else:
            task_id = int(sys.argv[2])
            task_manager.mark_in_progress(task_id)

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <task_id>")
        else:
            task_id = int(sys.argv[2])
            task_manager.mark_done(task_id)

    elif command == "list":
        if len(sys.argv) == 3:
            status = sys.argv[2]
            task_manager.list_tasks(status)
        else:
            task_manager.list_tasks()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
