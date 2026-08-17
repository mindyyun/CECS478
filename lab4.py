# Emma Tu, Mindy Yun
# Contributions: Emma - 50%, Mindy - 50%

import platform
import os

# Identify OS information   
print("Operating System: ", platform.system())
print("System release information: ", platform.release())

# File and directory information about current file (lab 4)
print("Read access: ", os.access('lab4.py', os.R_OK))
print("Execute access: ", os.access('lab4.py', os.X_OK))

# User and process information
print("Current User: ", os.getlogin())
print("Process ID: ", os.getpid())
