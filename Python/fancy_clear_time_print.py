import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("The screen will clear again in\n3 ", end='', flush=True)
time.sleep(1)
print("2 ", end='', flush=True)
time.sleep(1)
print("1")
time.sleep(1)
clear()