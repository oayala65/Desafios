import os
import time

def borrar():
    if os.name == "posix":
        os.system("clear")        
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

borrar()
