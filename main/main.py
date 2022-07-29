"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

With help from de333r.

---------------------------------------------------

Main file.

"""

#Import Libraries.
import tkinter as tk
import random as rand
import time as ti


print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^^ Main Program Start! ^^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


new_window = tk.Tk()

def kill_window(window_name):
    window_name.destroy()

def key_pressed(event):

    key = str.lower(event.char)

    if key == chr(27):
        kill_window(new_window)

new_window.bind("<Key>", key_pressed)

new_window.mainloop()