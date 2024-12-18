from datetime import datetime
from typing import List, Optional
from models import Task, TaskStatus
from repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def create_task(self, title: str, description: str, 
                    due_date: Optional[datetime] = None,
                    tags: Optional[List[str]] = None) -> int:
        task = Task(title, description, due_date, tags)
        return self.repository.create(task)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repository.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all()

    def update_task(self, task_id: int, title: str = None, 
                    description: str = None, due_date: datetime = None,
                    tags: List[str] = None, status: TaskStatus = None) -> bool:
        task = self.repository.get(task_id)
        if task:
            task.update(title, description, due_date, tags, status)
            return self.repository.update(task_id, task)
        return False

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)