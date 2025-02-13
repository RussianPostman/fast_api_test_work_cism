from enum import Enum


class TaskStatusEnum(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
