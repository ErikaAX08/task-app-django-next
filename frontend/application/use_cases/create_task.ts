import {Task} from "@/domain/entities/task_entity";
import {TaskRepositoryInterface} from "@/domain/repositories/task_repository_interface";

export class CreateTaskUseCase {
    constructor(private readonly repository: TaskRepositoryInterface) {
    }

    async execute(title: string, description: string): Promise<Task> {
        return await this.repository.createTask(title, description);
    }
}
