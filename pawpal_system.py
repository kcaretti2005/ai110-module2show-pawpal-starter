from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    description: str
    type: str
    pet_name: str
    start_time: datetime
    duration_minutes: int
    priority: int
    is_done: bool
    recurrence: str

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task]

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


@dataclass
class Owner:
    name: str
    pets: list[Pet]
    available_minutes_per_day: int

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
