from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers.task_serializer import TaskSerializer, CreateTaskSerializer, UpdateTaskSerializer
from ....application.use_cases.create_task import CreateTaskUseCase, CreateTaskInputDTO
from ....application.use_cases.list_tasks import ListTasksUseCase
from ....infrastructure.repositories.task_repository_django import TaskRepositoryDjango

class TaskViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_repository = TaskRepositoryDjango()
        self.create_task_use_case = CreateTaskUseCase(self.task_repository)
        self.list_tasks_use_case = ListTasksUseCase(self.task_repository)

    def list(self, request):
        tasks = self.list_tasks_use_case.execute()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        input_dto = CreateTaskInputDTO(
            title=serializer.validated_data['title'],
            description=serializer.validated_data['description']
        )
        
        task = self.create_task_use_case.execute(input_dto)
        response_serializer = TaskSerializer(task)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        task = self.task_repository.get_task_by_id(int(pk))
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = UpdateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        task = self.task_repository.get_task_by_id(int(pk))
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if 'title' in serializer.validated_data:
            task.title = serializer.validated_data['title']
        if 'description' in serializer.validated_data:
            task.description = serializer.validated_data['description']
        if 'completed' in serializer.validated_data:
            task.completed = serializer.validated_data['completed']

        updated_task = self.task_repository.update_task(task)
        response_serializer = TaskSerializer(updated_task)
        return Response(response_serializer.data)

    def destroy(self, request, pk=None):
        success = self.task_repository.delete_task(int(pk))
        if not success:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.task_repository.mark_task_as_completed(int(pk))
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

