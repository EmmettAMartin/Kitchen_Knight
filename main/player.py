"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

---------------------------------------------------

Player class.

Comments should be in all caps unless referencing names.

"""

# IMPORT LIBRARIES
import tkinter as tk
import random as rand
import time as ti


class Player:
    def __init__(self, curr_x, curr_y, player_y, player_x):
        self.curr_x = curr_x
        self.curr_y = curr_y
        self.player_x = player_x
        self.player_y = player_y
