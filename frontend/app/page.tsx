"use client";

import styles from "./page.module.css";
import {TaskItem} from "@/interface/components/taskItem/taskItem";
import {useTasks} from "@/interface/hooks/useTasks";
import {useState} from "react";
import {Task} from "@/domain/entities/task_entity";

export default function Home() {
    const {tasks, loading, addTask, updateTask} = useTasks()
    const [taskName, setTaskName] = useState<string>("");
    const [taskDescription, setTaskDescription] = useState<string>("");

    if (loading) return <p>Loading...</p>

    const onSubmitHandler = (e) => {
        e.preventDefault()

        addTask(taskName, taskDescription).then(() => {
                setTaskName("")
                setTaskDescription("")
            }
        )
    }

    const onCompletedHandler = (task: Task) => {
        const updatedTask = {...task, completed: !task.completed};
        updateTask(updatedTask).then(() => {
            console.log("Tarea actualizada con éxito");
        });
    }
    return (
        <div className={styles.page}>
            <main className={styles.main}>
                <h1 className={styles.title}>#MyTaskApp</h1>
                <form onSubmit={onSubmitHandler} action="" className={styles.form}>
                    <input className={`${styles.input} ${styles.input_name}`} value={taskName} type="text"
                           placeholder="Task Name"
                           required onChange={(e) => setTaskName(e.target.value)}/>
                    <input className={`${styles.input} ${styles.input_description}`} value={taskDescription} type="text"
                           placeholder="Task Description" onChange={(e) => setTaskDescription(e.target.value)}
                           required/>
                    <input className={styles.button_form} type="submit" value="Add Task"/>
                </form>
                <div className={styles.task_container}>
                    {
                        tasks.map((task) =>
                            <TaskItem key={task.id} title={task.title} description={task.description}
                                      completed={task.completed} onComplete={() => onCompletedHandler(task)}/>
                        )
                    }
                </div>
            </main>
        </div>
    );
}
