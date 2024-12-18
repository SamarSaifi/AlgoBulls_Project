from datetime import datetime
from enum import Enum
from typing import List, Optional

class TaskStatus(Enum):
    OPEN = "OPEN"
    WORKING = "WORKING"
    PENDING_REVIEW = "PENDING_REVIEW"
    COMPLETED = "COMPLETED"
    OVERDUE = "OVERDUE"
    CANCELLED = "CANCELLED"

class Task:
    def __init__(
        self,
        title: str,
        description: str,
        due_date: Optional[datetime] = None,
        tags: Optional[List[str]] = None
    ):
        if len(title) > 100:
            raise ValueError("Title must be less than 100 characters")
        if len(description) > 1000:
            raise ValueError("Description must be less than 1000 characters")
        
        self.timestamp = datetime.now()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tags = list(set(tags)) if tags else []  # Ensure unique tags
        self.status = TaskStatus.OPEN

    def update(self, title: str = None, description: str = None, 
               due_date: datetime = None, tags: List[str] = None,
               status: TaskStatus = None) -> None:
        if title is not None:
            if len(title) > 100:
                raise ValueError("Title must be less than 100 characters")
            self.title = title
        
        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description must be less than 1000 characters")
            self.description = description
        
        if due_date is not None:
            if due_date < self.timestamp:
                raise ValueError("Due date cannot be before creation timestamp")
            self.due_date = due_date
        
        if tags is not None:
            self.tags = list(set(tags))  # Ensure unique tags
        
        if status is not None:
            if not isinstance(status, TaskStatus):
                raise ValueError("Invalid status")
            self.status = status