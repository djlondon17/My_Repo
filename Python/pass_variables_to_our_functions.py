import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_num(question, q2):
    while True:
        try:
            x = int(input(question))
            y = int(input(q2))
            return x, y
        except ValueError:
            print("That is not a number.")
            continue   

clear()
dogs, age = get_num("How many dogs do you have: ", "How old is the oldest you have? ")
print(f"You have {dogs} dogs, and the oldest is {age}.")