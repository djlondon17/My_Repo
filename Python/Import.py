'''
import random

flip = random.randint(1,2)
if flip == 1:
    print("Heads")
else:
    print("Tails")
'''

from random import randint as rand

flip = rand(1,2)
if flip == 1:
    print("Tails")
else:
    print("Heads")