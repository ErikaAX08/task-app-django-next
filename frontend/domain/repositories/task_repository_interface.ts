import {Task} from "../entities/task_entity";

export interface TaskRepositoryInterface {
    listTasks(): Promise<Task[]>;

    createTask(title: string, description: string): Promise<Task>;

    updateTask(task: Task): Promise<Task>;
}
