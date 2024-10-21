# Use a JSON file to store the tasks in the current directory.
# The JSON file should be created if it does not exist.
# Use the native file system module of your programming language to interact with the JSON file.
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
# Use positional arguments in command line to accept user inputs.
# Do not use any external libraries or frameworks to build this project.
# Ensure to handle errors and edge cases gracefully.

tasks = [{'desc':'hacer tarea','status':'done'},{'desc':'hacer tareilla','status':'In progress'}]

#TODO: sin parametros listar todas, optional params: done (filtra dones), todo, in-progress.
def list_all_tasks():
    return tasks

def add_task(task):
    tasks.append(task)
    print(f'Task {task['desc']} added successfully')

def update_task(index,newTask):
    try:
        tasks[index] = newTask
    except:
        print("There's Any task at that index")

def mark_in_progress(index):
    try:
        tasks[index]["status"] = "in-progress"
    except:
        print("index don't found")

def mark_done(index):
    try:
        tasks[index]["status"] = "done"
    except:
        print("index don't found")

def delete_task(index):
    try:
        tasks.pop(index)
    except:
        print("There's any task with that index")

