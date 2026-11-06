import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, time

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.caption("A pet care planner that sorts your day and flags conflicts.")

st.subheader("Owner & Pets")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", 120)
owner = st.session_state.owner
owner.name = st.text_input("Owner name", value=owner.name)

col_a, col_b, col_c = st.columns(3)
with col_a:
    pet_name = st.text_input("Pet name", value="Mochi")
with col_b:
    species = st.selectbox("Species", ["dog", "cat", "other"])
with col_c:
    age = st.number_input("Age", min_value=0, max_value=30, value=2)

if st.button("Add pet"):
    owner.add_pet(Pet(pet_name, species, int(age)))
    st.success(f"Added {pet_name}!")

st.write("Your pets:", ", ".join(p.name for p in owner.pets) or "none yet")

st.divider()
st.subheader("Tasks")

PRIORITY_MAP = {"high": 1, "medium": 2, "low": 3}  

if not owner.pets:
    st.info("Add a pet first.")
else:
    pet_choice = st.selectbox("Pet", [p.name for p in owner.pets])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        start = st.time_input("Start time", value=time(8, 0))
    with col3:
        duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    with col4:
        priority = st.selectbox("Priority", ["high", "medium", "low"])
    recurrence = st.selectbox("Repeats", ["none", "daily", "weekly"])

    if st.button("Add task"):
        pet = next(p for p in owner.pets if p.name == pet_choice)
        start_dt = datetime.combine(datetime.now().date(), start)
        pet.add_task(Task(task_title, "general", "", start_dt, int(duration),
                          PRIORITY_MAP[priority], recurrence=recurrence))
        st.success(f"Added '{task_title}' for {pet_choice}")

st.divider()
st.subheader("Today's Schedule")

scheduler = Scheduler(owner)
if st.button("Generate schedule"):
    schedule = scheduler.get_todays_schedule()
    if not schedule:
        st.info("No tasks scheduled for today.")
    else:
        st.table([
            {"Time": f"{t.start_time:%I:%M %p}", "Pet": t.pet_name,
             "Task": t.description, "Duration": f"{t.duration_minutes} min",
             "Priority": t.priority}
            for t in schedule
        ])
    for warning in scheduler.detect_conflicts():
        st.warning(warning)