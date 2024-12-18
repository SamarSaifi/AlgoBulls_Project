from typing import List, Optional
from models import Task

class TodoRepository:
    def __init__(self):
        self.tasks: List[Task] = []
        self._counter = 0

    def create(self, task: Task) -> int:
        self._counter += 1
        self.tasks.append(task)
        return self._counter

    def get(self, task_id: int) -> Optional[Task]:
        if 0 < task_id <= len(self.tasks):
            return self.tasks[task_id - 1]
        return None

    def get_all(self) -> List[Task]:
        return self.tasks.copy()

    def update(self, task_id: int, task: Task) -> bool:
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1] = task
            return True
        return False

    def delete(self, task_id: int) -> bool:
        if 0 < task_id <= len(self.tasks):
            self.tasks.pop(task_id - 1)
            return True
        return False