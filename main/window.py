import handling
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()

base_dimensions_x = 161
base_dimensions_y = 91

multiplier = 10

mod_dimensions_x = base_dimensions_x * multiplier
mod_dimensions_y = base_dimensions_y * multiplier

geometry_string = str(mod_dimensions_x) + "x" + str(mod_dimensions_y)

root.geometry(geometry_string)

root.title("Game @ " + str(mod_dimensions_x) + "x" + str(mod_dimensions_y))





while True:
    pass





root.mainloop()