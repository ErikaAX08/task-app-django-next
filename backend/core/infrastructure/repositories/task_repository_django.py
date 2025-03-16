from typing import List, Optional
from ...domain.entities.task_entity import Task
from ...domain.repositories.task_repository_interface import TaskRepositoryInterface
from core.infrastructure.models import TaskModel


class TaskRepositoryDjango(TaskRepositoryInterface):
    def get_all_tasks(self) -> List[Task]:
        task_models = TaskModel.objects.all()
        return [self._to_entity(task_model) for task_model in task_models]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        try:
            task_model = TaskModel.objects.get(id=task_id)
            return self._to_entity(task_model)
        except TaskModel.DoesNotExist:
            return None

    def create_task(self, task: Task) -> Task:
        task_model = TaskModel(
            title=task.title,
            description=task.description,
            completed=task.completed
        )
        task_model.save()
        return self._to_entity(task_model)

    def update_task(self, task: Task) -> Task:
        task_model = TaskModel.objects.get(id=task.id)
        task_model.title = task.title
        task_model.description = task.description
        task_model.completed = task.completed
        task_model.save()
        return self._to_entity(task_model)

    def delete_task(self, task_id: int) -> bool:
        try:
            task_model = TaskModel.objects.get(id=task_id)
            task_model.delete()
            return True
        except TaskModel.DoesNotExist:
            return False

    def mark_task_as_completed(self, task_id: int) -> Optional[Task]:
        try:
            task_model = TaskModel.objects.get(id=task_id)
            task_model.completed = True
            task_model.save()
            return self._to_entity(task_model)
        except TaskModel.DoesNotExist:
            return None

    def _to_entity(self, task_model: TaskModel) -> Task:
        return Task(
            id=task_model.id,
            title=task_model.title,
            description=task_model.description,
            completed=task_model.completed,
            created_at=task_model.created_at,
            updated_at=task_model.updated_at
        )
