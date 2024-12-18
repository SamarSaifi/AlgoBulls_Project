import unittest
from datetime import datetime, timedelta
from models import Task, TaskStatus
from service import TodoService

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.service = TodoService()

    def test_create_task(self):
        task_id = self.service.create_task(
            title="Test Task",
            description="Test Description",
            due_date=datetime.now() + timedelta(days=1),
            tags=["test"]
        )
        self.assertEqual(task_id, 1)
        
        task = self.service.get_task(task_id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.tags, ["test"])
        self.assertEqual(task.status, TaskStatus.OPEN)

    def test_update_task(self):
        task_id = self.service.create_task(
            title="Original Title",
            description="Original Description"
        )
        
        self.service.update_task(
            task_id,
            title="Updated Title",
            status=TaskStatus.WORKING
        )
        
        task = self.service.get_task(task_id)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.status, TaskStatus.WORKING)

    def test_delete_task(self):
        task_id = self.service.create_task(
            title="Task to Delete",
            description="This task will be deleted"
        )
        
        self.assertTrue(self.service.delete_task(task_id))
        self.assertIsNone(self.service.get_task(task_id))

    def test_validation(self):
        # Test title length validation
        with self.assertRaises(ValueError):
            self.service.create_task(
                title="A" * 101,  # Title too long
                description="Test Description"
            )

        # Test description length validation
        with self.assertRaises(ValueError):
            self.service.create_task(
                title="Test Title",
                description="A" * 1001  # Description too long
            )

if __name__ == '__main__':
    unittest.main()