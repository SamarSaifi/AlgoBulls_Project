from datetime import datetime, timedelta
from models import TaskStatus
from service import TodoService

def main():
    # Create a new TodoService instance
    todo_service = TodoService()

    # Create some sample tasks
    task_id1 = todo_service.create_task(
        title="Complete Python Project",
        description="Implement a Todo List application using Python",
        due_date=datetime.now() + timedelta(days=3),
        tags=["python", "project"]
    )

    task_id2 = todo_service.create_task(
        title="Write Documentation",
        description="Create comprehensive documentation for the Todo List app",
        due_date=datetime.now() + timedelta(days=1),
        tags=["docs", "writing"]
    )

    # Get and print all tasks
    print("\nAll Tasks:")
    for task in todo_service.get_all_tasks():
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {task.status.value}")
        print(f"Due Date: {task.due_date}")
        print(f"Tags: {', '.join(task.tags)}")
        print("-" * 50)

    # Update a task
    todo_service.update_task(
        task_id1,
        status=TaskStatus.WORKING,
        tags=["python", "project", "in-progress"]
    )

    # Get and print a specific task
    task = todo_service.get_task(task_id1)
    if task:
        print("\nUpdated Task:")
        print(f"Title: {task.title}")
        print(f"Status: {task.status.value}")
        print(f"Tags: {', '.join(task.tags)}")

    # Delete a task
    todo_service.delete_task(task_id2)

if __name__ == "__main__":
    main()