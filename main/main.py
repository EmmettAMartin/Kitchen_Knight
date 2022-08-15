"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

With help from de333r.

v0.1.5

---------------------------------------------------

Main file.

Comments should be in all caps unless referencing names.

"""

#IMPORT LIBRARIES

#tkinter
import tkinter as tk

#random
import random as rand

#time
import time as ti

#operating system
import os

#messagebox and simpledialog; from tkinter (needs to be imported seperatly.)
from tkinter import messagebox, simpledialog


print("********************")
print("*Main Program Start*")
print("********************")

#MAIN WINDOW
main_window = tk.Tk()

#LOADING SCREEN
def loading_screen(window_address):
    background = tk.Canvas(width=mod_dimensions_x, height=mod_dimensions_y, bg="#000000", highlightthickness=0)
    background.pack()

    
#CONSTRUCT WINDOW
def construct_window(window_address):
    pass


#RESIZE WINDOW
def configure_window(window_address, x, y, multiplier, window_name, default_zero_operation):

    global mod_dimensions_x
    global mod_dimensions_y

    try:
        if multiplier == 0 and default_zero_operation == False:
            messagebox.showerror("ERROR","IntentionalError: Cannot make window with multiplier value 0")
            kill_window(main_window)
            quit()

        elif multiplier == 0 and default_zero_operation == True:
            messagebox.showwarning("WARNING","Warning: An error occurred and was fixed automatically. If this continues to happen, please contact our support.")
            multiplier = 1

    
        mod_dimensions_x = x * multiplier
        mod_dimensions_y = y * multiplier

        geometry_string = str(mod_dimensions_x)+"x"+str(mod_dimensions_y)

        window_address.geometry(geometry_string)

        window_address.title(window_name + " - " + str(mod_dimensions_x) + "x" + str(mod_dimensions_y))

    except tk.TclError:
        pass


#KILL WINDOW
def kill_window(window_address):
    window_address.destroy()


#KEY PRESS HANDLER
def key_pressed(event):

    key = str.lower(event.char)

    if key == chr(27):
        kill_window(main_window)

    if key == chr(13):
        run_game()



#FUNCTION TO RUN GAME
def run_game():
    configure_window(main_window, 189, 63, 0, "Game", True)
    loading_screen(main_window)


run_game()

main_window.bind("<Key>", key_pressed)

main_window.mainloop()