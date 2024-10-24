import datetime


class Task:
    def __init__(self, task_id, description, status="todo"):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at

    def mark_in_progress(self):
        self.status = "in progress"
        self.updated_at = datetime.datetime.now().isoformat()

    def mark_done(self):
        self.status = "done"
        self.updated_at = datetime.datetime.now().isoformat()

    def update_description(self, new_description):
        self.description = new_description
        self.updated_at = datetime.datetime.now().isoformat()
