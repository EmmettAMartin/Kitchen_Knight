import tkinter as tk
import random as rand
import time as ti
import threading as thr
import os
import sys


global money
global score
global health
global player_x
global player_y
global player_1_frame
global platfrom1
global player_start_y
global platfrom_1_height
global can_jump
global obstacle_1
global obstacle_list_x
global obstacle_list_y

root = tk.Tk()

base_dimensions_x = 160
base_dimensions_y = 90

multiplier = 8

mod_dimensions_x = base_dimensions_x * multiplier
mod_dimensions_y = base_dimensions_y * multiplier

geometry_string = str(mod_dimensions_x)+"x"+str(mod_dimensions_y)

root.geometry(geometry_string)

root.title("Kitchen Knight vALPHA11")

############################################################
#main game code.                                           #
############################################################

#quit function
def quit_game(k=""):
    root.destroy()

#main function to initialize the game.
def game_start():
    global obstacle1_height
    global obstacle1_width
    global money
    global score
    global health
    global player_x
    global player_y
    global player_1_frame
    global platfrom1
    global player_start_y
    global platfrom_1_height
    global can_jump
    global obstacle_1
    global obstacle_list_x_start
    global obstacle_list_x_end
    global obstacle_list_y
    global background1

    start_background.pack_forget()
    start_button.place_forget()

    money = 0
    score = 0
    health = 100
    player_start_y = (((mod_dimensions_y/2)+40)-10) # mod_dimensions_y is the height of the window, divided by 2, adding 40 to correctly place, then subtracting 10 for finer adjustments. 
    #player_start_y =  ((mod_dimensions_y/2)+30) simpler version.
    player_x = 100
    player_y = player_start_y
    can_jump = True
     
    """ Yes, yes, I know it's better if I do +30 with no -10, but it's for clarity. Without it it's just a number,
    and idk what it means. With the -10 I know for a fact that now the player will show 100%. """

    background1 = tk.Canvas(width=mod_dimensions_x,height=mod_dimensions_y, bg="#35baf8", highlightthickness=0)

    info_container = tk.Frame(background1, height=80,width=160,bg="white",highlightbackground="black",highlightthickness=2)

    health_counter = tk.Label(info_container, text=("Hit Points: "+str(health)), bg="white", font=("Kitchen Knight",12))
    score_counter = tk.Label(info_container, text=("Score: "+str(score)), bg="white", font=("Kitchen Knight",12))
    money_counter = tk.Label(info_container, text=("Money: "+str(money)), bg="white", font=("Kitchen Knight",12))
    info2 = background1.create_text(((mod_dimensions_x-100),10), text="Press the Escape key to quit.", font=("Kitchen Knight",12))

    player_1_frame = tk.Frame(background1, height=10,width=10,highlightthickness=0, bg="black")
    
    background1.pack()
    info_container.place(x=0,y=0)
    health_counter.place(x=0,y=0)
    score_counter.place(x=0,y=20)
    money_counter.place(x=0,y=40)
    player_1_frame.place(x=player_x,y=player_start_y)

    #LET'S DO THIS
    platfrom_1_height = ((mod_dimensions_y/2)-40)
    
    platfrom1 = tk.Frame(width=mod_dimensions_x,height=platfrom_1_height, bg="sienna4")
    platfrom1.place(x=0,y=(mod_dimensions_y-platfrom_1_height))

    #YAY COMPLICATED STUFF
    #TODO: Do obstacle checking
    #TODO: get frame positions into obstacle_list
    #TODO: Append the positions of the obstacles/platforms into the obstacle_list; no idea how to do.
    place_obstacles()


def place_obstacles():
    global obstacle1_height
    global obstacle1_width
    global money
    global score
    global health
    global player_x
    global player_y
    global player_1_frame
    global platfrom1
    global player_start_y
    global platfrom_1_height
    global can_jump
    global obstacle_1
    global obstacle_list_x_start
    global obstacle_list_x_end
    global obstacle_list_y
    global background1

    obstacle_list_x_start = []
    obstacle_list_x_end = []
    obstacle_list_y = []

    obstacle1_width = 30
    obstacle1_height = 10
    obstacle_1x_start = 150
    obstacle_1y_start = player_start_y
    obstacle_1x_end = obstacle_1x_start + obstacle1_width - 10

    obstacle_1 = tk.Frame(background1,width=obstacle1_width,height=obstacle1_height,bg="sienna4")
    obstacle_1.place(x=obstacle_1x_start,y=obstacle_1y_start)

    obstacle_list_x_start.append(obstacle_1x_start)
    obstacle_list_x_end.append(obstacle_1x_end)
    obstacle_list_y.append(obstacle_1y_start)
    print(obstacle_list_x_start)
    print(obstacle_list_x_end)


def gravity():
    try:
        global player_y
        global player_x
        global player_1_frame
        global can_jump
        if (player_y + 10) < (mod_dimensions_y - platfrom_1_height):
            player_y = player_y + 10
            player_1_frame.place(x=player_x,y=player_y)
            root.after(150, gravity)
        else:
            can_jump = True
    except NameError:
        pass

def move_player(event):
    try:
        global player_x
        global player_y
        global can_jump

        k = str.lower(event.char)

        if k == "a" and ((player_x > 0) and (((player_x-10) in obstacle_list_x_end) == False) and ((player_y in obstacle_list_y) == True) or ((player_y in obstacle_list_y) == False)):
            player_x = player_x - 10

        if k == "d" and (player_x < (mod_dimensions_x-10) and (((player_x+10) in obstacle_list_x_start) == False) and ((player_y in obstacle_list_y) == True) or ((player_y in obstacle_list_y) == False)):
            player_x = player_x + 10

        if k == " " and can_jump == True:
            can_jump = False
            player_y = player_y - 30

        """TODO: Modify the method of checking whether gravity should be called or not, by checking whether
        or the player is on a platform; do once the obstacle list is implemented."""
        if can_jump == False and ((player_y) in obstacle_list_y) == False:
            root.after(250, gravity)
        else:
            pass
        player_1_frame.place(x=player_x,y=player_y)
    except NameError:
        pass

#Start screen
start_background = tk.Canvas(width=mod_dimensions_x,height=mod_dimensions_y,bg="#888888",highlightthickness=0)
start_button = tk.Button(start_background,text="Start Game",fg="blue",command=game_start, font=("Kitchen Knight",12))
info1 = tk.Label(start_background,text="To quit the game, press the Escape key.",fg="blue",bg="#888888", font=("Kitchen Knight",12))

start_background.pack()
start_button.place(x=(mod_dimensions_x/2),y=(mod_dimensions_y/2))
info1.place(x=(mod_dimensions_y/2),y=((mod_dimensions_y/2)))

root.bind("<Escape>", quit_game)
root.bind("<Key>", move_player)
root.protocol("WM_DELETE_WINDOW", quit_game)

############################################################
#always ends with this.                                    #
############################################################

root.mainloop()