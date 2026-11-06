# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
=== Today's Schedule ===
08:00 AM  Max: Breakfast (10 min)
08:00 AM  Luna: Medication (5 min)
02:00 PM  Luna: Vet appointment (45 min)
06:00 PM  Max: Evening walk (30 min)

=== Warnings ===
Conflict: 'Breakfast' (Max) and 'Medication' (Luna) both start at 08:00 AM

Next breakfast scheduled: Sat 08:00 AM
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest
```

Sample test output:

```
collected 5 items
tests\test_pawpal.py .....                                  [100%]
5 passed in 0.13s
```

Confidence level: ★★★★☆ (4/5)

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts by start time, then priority (1 = high) |
| Filtering | `Scheduler.filter_tasks()`, `Scheduler.get_pending_tasks()` | By pet name and/or completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Flags tasks with the exact same start time; returns warning messages instead of crashing |
| Recurring tasks | `Scheduler.handle_recurring()` | Daily is +1 day, weekly is +7 days; returns None for non-repeating tasks, and the caller adds the new task to the pet |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Run `streamlit run app.py` to open the app in your browser.
2. Enter an owner name, a pet name, species and age, then click **Add pet**.
3. Choose the pet, set a task title, start time, duration, priority and repeat, then click **Add task**. Add two tasks at the same start time.
4. Click **Generate schedule** to see today's tasks sorted by time, then priority.
5. A yellow warning appears for the two tasks that start at the same time.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
