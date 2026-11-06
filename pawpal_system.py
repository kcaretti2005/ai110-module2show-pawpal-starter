from dataclasses import dataclass, field
from datetime import datetime, timedelta

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
    
# priority: 1 = high, 2 = medium, 3 = low
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

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        return sorted(tasks, key=lambda t: (t.start_time, t.priority))

    def get_todays_schedule(self) -> list[Task]:
        today = datetime.now().date()
        todays = [t for t in self.owner.get_all_tasks()
            if t.start_time.date() == today]
        return self.sort_by_time(todays)

    def detect_conflicts(self) -> list[str]:
        warnings = []
        tasks = self.sort_by_time(self.owner.get_all_tasks())
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                a, b = tasks[i], tasks[j]
                if a.start_time == b.start_time:
                    warnings.append(
                        f"Conflict: '{a.description}' ({a.pet_name}) and "
                        f"'{b.description}' ({b.pet_name}) both start at "
                        f"{a.start_time:%I:%M %p}")
        return warnings

    def get_pending_tasks(self) -> list[Task]:
        return [t for t in self.owner.get_all_tasks() if not t.is_done]

    def handle_recurring(self, task: Task) -> Task | None:
        if task.recurrence == "daily":
            delta = timedelta(days=1)
        elif task.recurrence == "weekly":
            delta = timedelta(weeks=1)
        else:
            return None
        next_task = Task(task.description, task.type, task.pet_name,
                     task.start_time + delta, task.duration_minutes,
                     task.priority, False, task.recurrence)
        return next_task
    
    def filter_tasks(self, pet_name: str | None = None,
                 is_done: bool | None = None) -> list[Task]:
        tasks = self.owner.get_all_tasks()
        if pet_name is not None:
            tasks = [t for t in tasks if t.pet_name == pet_name]
        if is_done is not None:
            tasks = [t for t in tasks if t.is_done == is_done]
        return tasks
