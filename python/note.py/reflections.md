# Reflection – Note Taking App

**What was my goal?**
I wanted to build a small desktop note-taking app using Python and Tkinter. The app should let me type notes, save them to a file, open notes from a file, clear the text box, and exit.

**What key decisions did I make?**

* I used Tkinter because it is simple and comes with Python.
* I added buttons for **Open**, **Save**, **Clear**, and **Exit** to make it easy to use.
* I made the window size bigger (400x600) so typing feels more natural.
* I set a clean white background and a bigger font for readability.

**What problems did I solve?**

* Made sure the app could open text files and show the content in the text area.
* Handled saving so it writes what I typed into a `.txt` file.
* Added a clear button so I can quickly remove all notes if needed.

**What was the hardest part, and how did I solve it?**

* The file dialogs (`asksaveasfile`, `askopenfile`) were confusing at first. I fixed it by carefully checking if the file is `None` before trying to read or write.
* Making the buttons work required linking each one to the right function (`command=openFile`, `command=saveFile`, etc). I learned to test them one at a time.
* Understanding how to place the widgets (pack vs frame) was tricky, but breaking it into top frame + text area made it work.

**What would I improve next time?**

* Make it more usable by letting users open **any file type** (not only `.txt`).
* Add a confirmation pop-up before clearing or exiting so notes are not lost by mistake.
* Add simple formatting (bold, italic, colors) to make it feel closer to a real notepad.
* Save automatically every few minutes so I don’t lose work.