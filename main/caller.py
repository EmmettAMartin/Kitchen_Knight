#!/usr/bin/env python3
"""

2022 Hats Off Studios.
Emmett, Doran, Ty, Eliot.
Made August 6th, author: Emmett of Hats Off Studios.

v0.1.5

---------------------------------------------------

Caller file.

Comments should be in all caps unless referencing names.

"""

import os
import platform

try:
    operating_system = platform.system().lower()

    if operating_system == "darwin":
        try:
            os.chdir("Desktop/Kitchen_Knight/main")
        except FileNotFoundError:
            pass
        
        os.system("read -p \"Hit ENTER to begin\"; python3 main.py; read -p \"Hit ENTER to exit\"")
        quit()

    if operating_system == "windows":
        try:
            os.chdir("Desktop\\Kitchen_Knight\\main")
        except FileNotFoundError:
            pass
        
        os.system("read -p \"Hit ENTER to begin\"; python3 main.py; read -p \"Hit ENTER to exit\"")
        quit()

    else:
        raise Exception ("ERROR")

except Exception:
    print("We're sorry, there's been a problem. Contact our support if there are more issues.")