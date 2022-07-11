"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

---------------------------------------------------

Window Class.

"""

#Import Libraries.
import tkinter as tk
import random as rand
import time as ti

#Create class for window.
class Window:

    #Assign window properties.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    #Initialize window.
    def initialize_window(self):
        #Create window.
        new_window = tk.Tk()

        #Create string for geometry
        geometry_string = str(self.width)+"x"+str(self.height)

        #Insert variable "geometry_string" into ".geometry" function to resize window.
        new_window.geometry(geometry_string)

        #LET IT LIVE!!!!!!!!!
        new_window.mainloop()