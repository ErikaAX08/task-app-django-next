"use client";  // si vas a usarlo en un Client Component de Next 13

import {useState, useEffect} from "react";
import {Task} from "@/domain/entities/task_entity";
import {TaskRepositoryAPI} from "@/infrastructure/repositories/task_repository_api";
import {ListTasksUseCase} from "@/application/use_cases/list_tasks";
import {CreateTaskUseCase} from "@/application/use_cases/create_task";
import {UpdateTaskUseCase} from "@/application/use_cases/update_task";

export const useTasks = () => {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const repo = new TaskRepositoryAPI();
    const listTasksUseCase = new ListTasksUseCase(repo);
    const createTaskUseCase = new CreateTaskUseCase(repo);
    const updateTaskUseCase = new UpdateTaskUseCase(repo);

    const fetchTasks = async () => {
        setLoading(true);
        setError(null);
        try {
            const tasksList = await listTasksUseCase.execute();
            setTasks(tasksList);
        } catch (err) {
            setError("Error fetching tasks");
        } finally {
            setLoading(false);
        }
    };

    const addTask = async (title: string, description: string) => {
        try {
            const newTask = await createTaskUseCase.execute(title, description);
            setTasks((prev) => [...prev, newTask]);
        } catch (err) {
            setError("Error creating task");
        }
    };

    const updateTask = async (task: Task) => {
        setLoading(true);
        setError(null);
        try {
            const updatedTask = await updateTaskUseCase.execute(task);
            setTasks(prevTasks =>
                prevTasks.map(t => t.id === task.id ? updatedTask : t)
            );
            return updatedTask;
        } catch (err) {
            setError("Error updating task");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchTasks();
    }, []);

    return {
        tasks,
        loading,
        error,
        addTask,
        updateTask
    };
};
