import {Task} from "@/domain/entities/task_entity";
import {TaskRepositoryInterface} from "@/domain/repositories/task_repository_interface";

export class TaskRepositoryAPI implements TaskRepositoryInterface {
    private baseUrl = "http://127.0.0.1:8000/api/tasks/";

    async listTasks(): Promise<Task[]> {
        const response = await fetch(this.baseUrl);
        if (!response.ok) {
            throw new Error("Error fetching tasks");
        }
        return response.json();
    }

    async createTask(title: string, description: string): Promise<Task> {
        const response = await fetch(this.baseUrl, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({title, description}),
        });
        if (!response.ok) {
            throw new Error("Error creating task");
        }
        return response.json();
    }

    async updateTask(task: Task): Promise<Task> {
        const response = await fetch(`${this.baseUrl}${task.id}/`, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(task),
        });
        if (!response.ok) {
            throw new Error("Error updating task");
        }
        return response.json();
    }
}
