from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    description: str
    type: str
    pet_name: str
    start_time: datetime
    duration_minutes: int
    priority: int
    is_done: bool = False
    recurrence: str = "none"

    def mark_complete(self) -> None:
        pass

# Task 1 = highest priority, 2 = medium, 3 = low
# recurrence: "none", "daily", or "weekly"
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


@dataclass
class Owner:
    name: str
    available_minutes_per_day: int
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_all_tasks(self) -> list[Task]:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_schedule(self) -> list[Task]:
        pass

    def detect_conflicts(self) -> list[tuple]:
        pass

    def get_pending_tasks(self) -> list[Task]:
        pass

    def handle_recurring(self, task: Task) -> Task:
        pass
