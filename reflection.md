# PawPal+ Project Reflection

## 1. System Design
Three core actions

1. The user can enter basic owner and pet information.
2. The user can add a task with a duration and a priority.
3. The user can generate and view a daily plan based on those tasks.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design consisted of four classes. Owner which held pets and available minutes per day.
Pet would hold its tasks. Task would have one care activity and the description, type, start time, duration, priority, done, recurrence. Scheduler takes an owner and organizes tasks across all pets. Tasks live on the Pet and the scheudler reads them through the owner so it doesn't duplicate data.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
I made a couple real changes during design implementation. First, Scheduler went from knowing everything to holding a reference to the Owner. I added pet_name to task so a schedule entry shows whose task it is. I moved all the reccurence to one place, mark_complete() only sets is_done and Scheduler.handle_recurring() creates the next task.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler consisders start time, then priority, plus today's date. So time goes first and then priorty breaks the tie. 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
Conflict detection only flags tasks with the exact same start time and ignores duration. So if there is a 30 minute task at 8:00 but another task at 8:15 it would not get flagged. This is reasonable because it keeps everything simple and avoids crashing. 
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used AI tools for the UML draft, the class skeleton, and reviewing the final diagram against the code. When giving AI my specific attributes and methods it tended to work better compared to when I would just say fix this or do this. 
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
When AI made the class skeleton it looked right but the dataclasses had no defaults. Therefore Pet.tasks and Owner.pets has no default.factory and is.done/reccurence had none either. I caught this by reading the code against my design and testing it. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tests mark_complete for the status, adding a task to increase the pet's count, sorting for chronological a daily task to create tomorrow's task, and conflict detection flags deuplicate times. 
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
For confidence I am at 4 stars out of 5. Some of the edge cases I did not test were overlapping durations, a pet with no tasks, tasks crossing midnight, a weekly task, two pets with the same name.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I really enjoyed the design process before coding like designing the classes.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would probably use duration minutes to improve the overlapping issue.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned is the AI can make code fast but you really find out what's wrong but testing it against your own design.