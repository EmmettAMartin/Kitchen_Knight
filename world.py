"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 11th, author: Emmett of Hats Off Studios.

---------------------------------------------------

World Generation class.

"""

import tkinter as tk
import random as rand
import time as ti
import window as win

class World:

    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def generate_world(self, world_width, world_height):
        obstacle_list_x = []

        for i in range(int(world_width/10)):
            pass

