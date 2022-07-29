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

class Window:

    #Assign window properties.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def destroy_window(self):
        global new_window
        new_window.destroy()

    #Initialize window.
    def initialize_window(self):
        #Create window.
        global new_window
        new_window = tk.Tk()

        #Create string for geometry
        geometry_string = str(self.width)+"x"+str(self.height)

        #Insert variable "geometry_string" into ".geometry" function to resize window.
        new_window.geometry(geometry_string)

        #LET IT LIVE!!!!!!!!!
        new_window.mainloop()

class World:

    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def generate_world(self, world_width, world_height):
        obstacle_list_x = []

        for i in range(int(world_width/10)):
            pass
        #TODO make world generation by accessing window.