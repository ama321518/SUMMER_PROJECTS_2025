**To‑Do List App – My Key Learnings**

**1. Numbered list display with `enumerate(tasks, start=1)`**
This means that for each task in the list, I get a number starting from 1 (not 0), which matches how people naturally count.

* `i` is the task number that the user sees.
* `task` is the actual to-do text.
  So, `for i, task in enumerate(tasks, start=1):` lets me easily show:

1. Study Python  
2. Buy groceries

No need to track a separate counter variable.

**2. Confirming a valid task number with `if 1 <= task_number <= len(tasks):`**
This check makes sure that the number the user entered really points to an existing task.

* `1 <= task_number` ensures it’s not below the minimum.
* `task_number <= len(tasks)` ensures it’s not beyond the total number of tasks.
  If the user types `0`, `-1`, or `999`, this prevents the code from crashing or removing the wrong thing. It’s essential for safe user interaction.


**3. Removing the correct task using `tasks.pop(task_number - 1)`**
Because Python lists start at index 0, but we show numbers starting from 1, I subtract 1.

* If the user types `2`, we want to remove the item at index `1`.
  So `pop()` deletes that specific item and also returns it so I can print a message like:

Removed task: Buy groceries


This makes the deletion both functional and visible to the user.


**Additional Insight – Handling invalid input with `try/except`**
Whenever I ask for a number using `int(input(...))`, the user might type something that isn’t a number—like “hi” or leave it blank. That would crash the app.
So I wrap it in:

try:
    task_number = int(input(...))
    # remove logic
except ValueError:
    print("Invalid input. Please enter a number.")


This way, the app doesn’t crash—instead it tells the user what went wrong and keeps running smoothly.


**Summary:**
These three patterns—using `enumerate()` for numbering, validating input ranges, and translating the user’s number to a list index—are essential to building reliable list-based Python tools. Add the `try/except` around inputs and you have a user-friendly, crash-resistant app. Keep these patterns in your back pocket for any future mini projects.

