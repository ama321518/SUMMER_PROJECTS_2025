What was my goal?
E.g., “ To build a command-line to-do app with add/view/remove/exit”

What key decisions did I make?
Use a while True loop so the user can control quitting

Separate command input (add/view/remove/exit) from task input

Use enumerate to number tasks clearly(number -task)

Wrap int(input()) in try/except to handle bad input(so apart from lower handling case sensitive the ValueError looks at if the user did something like put in like punctuations,symbols anything other than task number)

What corner cases did I solve?

Adding empty task list — view and remove should warn user

Removing invalid or non-numeric input — use validation

What was the hardest part, and how did I solve it?
E.g., “I forgot to subtract 1 for the index; I realized it when remove didn’t work”



What would I improve next time?
using tkinker for a GUI more lively i guess
