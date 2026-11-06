from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, timedelta

# --- setup ---
owner = Owner("Sam", 120)
dog = Pet("Max", "dog", 3)
cat = Pet("Luna", "cat", 2)
owner.add_pet(dog)
owner.add_pet(cat)

base = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

# --- tasks (add them OUT of order, the page asks for that) ---
dog.add_task(Task("Evening walk", "walk", "", base + timedelta(hours=10), 30, 2))
dog.add_task(Task("Breakfast", "feeding", "", base, 10, 1, recurrence="daily"))
cat.add_task(Task("Medication", "medication", "", base, 5, 1)) 
cat.add_task(Task("Vet appointment", "appointment", "", base + timedelta(hours=6), 45, 1)) 

scheduler = Scheduler(owner)

# --- print today's schedule ---
print("=== Today's Schedule ===")
for t in scheduler.get_todays_schedule():
    print(f"{t.start_time:%I:%M %p}  {t.pet_name}: {t.description} ({t.duration_minutes} min)")

# --- conflicts ---
print("\n=== Warnings ===")
for w in scheduler.detect_conflicts():   
    print(w)

# --- recurring demo ---
breakfast = dog.get_tasks()[1]
breakfast.mark_complete()
next_one = scheduler.handle_recurring(breakfast)
if next_one:
    dog.add_task(next_one)
    print(f"\nNext breakfast scheduled: {next_one.start_time:%a %I:%M %p}")