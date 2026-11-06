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
        self.is_done = True
    
# Task 1 = highest priority, 2 = medium, 3 = low
# recurrence: "none", "daily", or "weekly"
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        task.pet_name = self.name
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list[Task]:
        return list(self.tasks)


@dataclass
class Owner:
    name: str
    available_minutes_per_day: int
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


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

