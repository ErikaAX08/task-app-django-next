from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def create(cls, title: str, description: str) -> 'Task':
        return cls(
            id=None,
            title=title,
            description=description,
            completed=False,
            created_at=None,
            updated_at=None
        )

    def mark_as_completed(self) -> None:
        self.completed = True
        self.updated_at = datetime.now()

    def update(self, title: str = None, description: str = None) -> None:
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()

