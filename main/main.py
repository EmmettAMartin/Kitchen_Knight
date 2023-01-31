#!/usr/bin/env python3
"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made July 10th, author: Emmett of Hats Off Studios.

v0.1.5

---------------------------------------------------

Main file.

Comments should be in all caps unless referencing names.

"""

# IMPORT LIBRARIES

# tkinter
import tkinter as tk

# random
import random as rand

# time
import time as ti

# operating system
import os

# messagebox and simpledialog; from tkinter (needs to be imported separately.)
from tkinter import messagebox, simpledialog

# PIL for images
# import PIL as pil

from PIL import Image, ImageEnhance, ImageTk

global background


def print_beginning_text():
    print("********************")
    print("*Main Program Start*")
    print("********************")


# MAIN WINDOW
main_window = tk.Tk()


# LOADING SCREEN
def loading_screen(window_address):
    global hos_logo
    global background

    background = tk.Canvas(
        width=mod_dimensions_x, height=mod_dimensions_y, bg="#000000", highlightthickness=0)

    hos_logo_pil = Image.open("images/HatsOff_Studios2.png")

    hos_logo_pil_width = hos_logo_pil.width
    hos_logo_pil_height = hos_logo_pil.height

    brightness_enhancer = ImageEnhance.Brightness(hos_logo_pil)

    hos_enhance = brightness_enhancer.enhance(0)

    hos_logo = ImageTk.PhotoImage(hos_enhance)

    image_label = tk.Label(background, image=hos_logo, anchor="center")

    background.pack()
    image_label.place(x=(mod_dimensions_x / 2) - (hos_logo_pil_width / 2),
                      y=(mod_dimensions_y / 2) - (hos_logo_pil_height / 2))

    increase_val = 0.01
    inc_prev_num = 0

    while True:
        if inc_prev_num >= 1:
            break
        inc_prev_num += increase_val
        hos_enhance = brightness_enhancer.enhance(inc_prev_num)
        hos_logo = ImageTk.PhotoImage(hos_enhance)

        image_label.configure(image=hos_logo)
        main_window.update()
        main_window.after(10)

    while True:
        if inc_prev_num <= 0:
            break
        inc_prev_num -= increase_val
        hos_enhance = brightness_enhancer.enhance(inc_prev_num)
        hos_logo = ImageTk.PhotoImage(hos_enhance)

        image_label.configure(image=hos_logo)
        main_window.update()
        main_window.after(10)

    image_label.place_forget()
    main_menu()
    """ Theory: have a while true loop that runs til the brightness = 1, then have a second one that goes to 0 
    Practice: 2 loops, 1 increasing 1 decreasing, use place_forget() and place() to hide and show the image 
    respectively. """


# # CONSTRUCT WINDOW
# def construct_window(window_address):
#     pass


def main_menu():
    load_btn = tk.Button(background, text="Load world")
    load_btn.place(x=100, y=100)
    start_btn = tk.Button(background, text="Start")


# RESIZE WINDOW
def configure_window(window_address, x, y, multiplier, window_name, default_zero_operation):
    global mod_dimensions_x
    global mod_dimensions_y

    try:
        if multiplier == 0 and default_zero_operation == False:
            messagebox.showerror("ERROR", "IntentionalError: Cannot make window with multiplier value 0")
            kill_window(main_window)
            quit()

        elif multiplier == 0 and default_zero_operation == True:
            messagebox.showwarning("WARNING",
                                   "Warning: An error occurred and was fixed automatically. If this continues to "
                                   "happen, please contact our support.")
            multiplier = 1

        mod_dimensions_x = x * multiplier
        mod_dimensions_y = y * multiplier

        geometry_string = str(mod_dimensions_x) + "x" + str(mod_dimensions_y)

        window_address.geometry(geometry_string)

        window_address.title(window_name + " - " + str(mod_dimensions_x) + "x" + str(mod_dimensions_y))

    except tk.TclError:
        pass


# KILL WINDOW
def kill_window(window_address):
    window_address.destroy()


# KEY PRESS HANDLER
def key_pressed(event):
    key = str.lower(event.char)

    if key == chr(27):
        kill_window(main_window)

    if key == chr(13):
        run_game()


# FUNCTION TO RUN GAME
def run_game():
    print_beginning_text()
    configure_window(main_window, 161, 91, 10, "Game", True)
    loading_screen(main_window)


run_game()

main_window.bind("<Key>", key_pressed)

main_window.mainloop()
