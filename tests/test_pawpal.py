from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def make_setup():
    owner = Owner("Sam", 120)
    pet = Pet("Max", "dog", 3)
    owner.add_pet(pet)
    return owner, pet, Scheduler(owner)


def test_mark_complete_changes_status():
    task = Task("Walk", "walk", "", datetime.now(), 30, 1)
    task.mark_complete()
    assert task.is_done == True         


def test_add_task_increases_count():
    owner, pet, _ = make_setup()
    before = len(pet.get_tasks())
    pet.add_task(Task("Walk", "walk", "", datetime.now(), 30, 1))
    assert len(pet.get_tasks()) == before + 1  


def test_sorting_is_chronological():
    owner, pet, sched = make_setup()
    now = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    pet.add_task(Task("Late", "walk", "", now + timedelta(hours=4), 30, 1))
    pet.add_task(Task("Early", "feed", "", now, 10, 1))
    names = [t.description for t in sched.sort_by_time(owner.get_all_tasks())]
    assert names == ["Early", "Late"]         


def test_daily_recurrence_creates_next_day_task():
    owner, pet, sched = make_setup()
    start = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    task = Task("Feed", "feed", "", start, 10, 1, recurrence="daily")
    pet.add_task(task)
    task.mark_complete()
    nxt = sched.handle_recurring(task)
    assert nxt is not None
    assert nxt.start_time == start + timedelta(days=1)  
    assert nxt.is_done == False


def test_conflict_detection_flags_duplicate_times():
    owner, pet, sched = make_setup()
    t = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    pet.add_task(Task("A", "walk", "", t, 30, 1))
    pet.add_task(Task("B", "feed", "", t, 10, 2))
    assert len(sched.detect_conflicts()) == 1       