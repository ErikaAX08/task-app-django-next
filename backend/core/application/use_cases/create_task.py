from dataclasses import dataclass
from ...domain.entities.task_entity import Task
from ...domain.repositories.task_repository_interface import TaskRepositoryInterface

@dataclass
class CreateTaskInputDTO:
    title: str
    description: str

@dataclass
class CreateTaskOutputDTO:
    id: int
    title: str
    description: str
    completed: bool

class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepositoryInterface):
        self._task_repository = task_repository

    def execute(self, input_dto: CreateTaskInputDTO) -> CreateTaskOutputDTO:
        # Create a new task entity
        task = Task.create(
            title=input_dto.title,
            description=input_dto.description
        )

        # Save it using the repository
        created_task = self._task_repository.create_task(task)

        # Return the output DTO
        return CreateTaskOutputDTO(
            id=created_task.id,
            title=created_task.title,
            description=created_task.description,
            completed=created_task.completed
        )

