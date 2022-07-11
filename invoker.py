"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

---------------------------------------------------

Invoker file.

"""

#Import Libraries.
import tkinter as tk
import random as rand
import time as ti
import window as win
import world as wld

main_window = win.Window(90,160)

world1 = wld.World(0,0)
world1.generate_world(main_window.width, main_window.height)


main_window.initialize_window()