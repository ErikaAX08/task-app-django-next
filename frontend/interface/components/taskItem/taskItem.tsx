"use client";

import React, {useState} from "react";
import styles from "./taskItem.module.css";

interface TaskItemProps {
    title: string;
    description: string;
    completed?: boolean;
    onComplete?: () => void;
}

export function TaskItem({title, description, completed = false, onComplete}: TaskItemProps) {
    const [isCompleted, setIsCompleted] = useState<boolean>(completed);

    const onChangeHandler = () => {
        setIsCompleted(!isCompleted);
        onComplete && onComplete();
    }

    return (
        <div className={styles.card} onClick={onChangeHandler}>
            <input
                type="checkbox"
                checked={isCompleted}
                className={styles.checkbox}
                onChange={onChangeHandler}
            />

            <div className={styles.info}>
                <h3 className={styles.title} style={
                    (isCompleted) ? {textDecoration: "line-through"} : {textDecoration: "none"}
                }>{title}</h3>
                <p className={styles.description}>{description}</p>
            </div>
        </div>
    );
}
