import json
import os

from Task import Task


class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.tasks = []
        self.file_path = file_path
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_id=task_data['id'],
                        description=task_data['description'],
                        status=task_data['status']
                    )
                    task.created_at = task_data['createdAt']
                    task.updated_at = task_data['updatedAt']
                    self.tasks.append(task)
        else:
            self.save_tasks()

    def save_tasks(self):
        tasks_data = []
        for task in self.tasks:
            tasks_data.append({
                'id': task.id,
                'description': task.description,
                'status': task.status,
                'createdAt': task.created_at,
                'updatedAt': task.updated_at
            })
        with open(self.file_path, 'w') as file:
            json.dump(tasks_data, file, indent=4)

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id, new_description):
        task = self.get_task_by_id(task_id)
        if task:
            task.update_description(new_description)
            self.save_tasks()
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Task {task_id} not found")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task {task_id} not found")

    def mark_in_progress(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_in_progress()
            self.save_tasks()
            print(f"Task {task_id} marked as in progress")
        else:
            print(f"Task {task_id} not found")

    def mark_done(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_done()
            self.save_tasks()
            print(f"Task {task_id} marked as done")
        else:
            print(f"Task {task_id} not found")

    def list_tasks(self, status=None):
        if status:
            filtered_tasks = [task for task in self.tasks if task.status == status]
            self.print_tasks(filtered_tasks)
        else:
            self.print_tasks(self.tasks)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def print_tasks(self, tasks):
        if tasks:
            for task in tasks:
                print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.created_at}, Updated At: {task.updated_at}")
        else:
            print("No tasks found")
