"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

With help from de333r.

v0.1.4

---------------------------------------------------

Main file.

"""

#Import Libraries.
import tkinter as tk
import random as rand
import time as ti


print("********************")
print("*Main Program Start*")
print("********************")


main_window = tk.Tk()


def resize_window(window_name, x, y, multiplier):

    if multiplier == 0:
        kill_window(main_window)
        
        print("Error: Cannot make window with multiplier value 0\nIntentionalError")

        quit()

    try:
        mod_dimensions_x = x * multiplier
        mod_dimensions_y = y * multiplier

        geometry_string = str(mod_dimensions_x)+"x"+str(mod_dimensions_y)

        window_name.geometry(geometry_string)
    except tk.TclError:

        pass


def kill_window(window_name):
    window_name.destroy()

def key_pressed(event):

    key = str.lower(event.char)

    if key == chr(27):
        kill_window(main_window)

resize_window(main_window, 189, 63, 8)

main_window.bind("<Key>", key_pressed)

main_window.mainloop()