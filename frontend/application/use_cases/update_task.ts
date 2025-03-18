import {Task} from "@/domain/entities/task_entity";
import {TaskRepositoryInterface} from "@/domain/repositories/task_repository_interface";

export class UpdateTaskUseCase {
    constructor(private readonly repository: TaskRepositoryInterface) {
    }

    async execute(task: Task): Promise<Task> {
        return await this.repository.updateTask(task);
    }
}
