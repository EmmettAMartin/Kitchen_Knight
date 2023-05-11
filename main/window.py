import tkinter as tk

class Window:
    def __init__(self, base_dimension_x, base_dimension_y, multiplier, mod_dimension_x, mod_dimension_y):

        self.base_dimension_x = base_dimension_x
        self.base_dimension_y = base_dimension_y
        self.multiplier = multiplier
        self.mod_dimension_x =  mod_dimension_x
        self.mod_dimension_y = mod_dimension_y

    def declare_dimensions(self):
        pass