import {Task} from "@/domain/entities/task_entity";
import {TaskRepositoryInterface} from "@/domain/repositories/task_repository_interface";

export class ListTasksUseCase {
    constructor(private readonly repository: TaskRepositoryInterface) {
    }

    async execute(): Promise<Task[]> {
        return await this.repository.listTasks();
    }
}
