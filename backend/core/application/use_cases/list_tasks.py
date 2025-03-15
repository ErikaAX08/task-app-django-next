from dataclasses import dataclass
from typing import List
from ...domain.repositories.task_repository_interface import TaskRepositoryInterface

@dataclass
class TaskDTO:
    id: int
    title: str
    description: str
    completed: bool

class ListTasksUseCase:
    def __init__(self, task_repository: TaskRepositoryInterface):
        self._task_repository = task_repository

    def execute(self) -> List[TaskDTO]:
        tasks = self._task_repository.get_all_tasks()
        return [
            TaskDTO(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=task.completed
            )
            for task in tasks
        ]

