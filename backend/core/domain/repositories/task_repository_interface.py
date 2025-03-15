from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.task_entity import Task

class TaskRepositoryInterface(ABC):
    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks"""
        pass

    @abstractmethod
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID"""
        pass

    @abstractmethod
    def create_task(self, task: Task) -> Task:
        """Create a new task"""
        pass

    @abstractmethod
    def update_task(self, task: Task) -> Task:
        """Update an existing task"""
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID"""
        pass

    @abstractmethod
    def mark_task_as_completed(self, task_id: int) -> Optional[Task]:
        """Mark a task as completed"""
        pass

