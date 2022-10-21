def guessing_game():
    from random import randint as rand

    answer = rand(1,100) # randomly generates a number between 1-100
    attempts = 0

    print("You only have 5 attempts.")
  
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            while attempts < 5:  # limit of 5 tries
                if guess < 1 or guess > 100:  # allow no numbers less than 1 or greater than 100
                    print("That is not a valid answer. Guess a number between 1 and 100.")
                    break
                elif guess < answer:  # Lets user know if guess is too low
                    print("Too low. Guess again.")
                    attempts += 1
                    break
                elif guess > answer:  # Lets user know if guess is too high
                    print("Too high. Guess again.")
                    attempts += 1
                    break
                else:  # exits game with a win
                    print("You win!")
                    return
            if attempts == 5:
                print(f"Sorry, out of tries. The correct number was {answer}.")  # exits game when user is out of tries
                return 
        except ValueError:
            print("That is not a valid answer")
            continue

response = "y"

print("Welcome to the game!")

while response != "n":
    guessing_game()
    while True:
        response = input("Would you like to play again?\n[Y|n]: ") # asks user if they want to play again
        if response in ["y", "n", ""]:
            break
        else:
            print("Input error: Please use 'y' or 'n'.")
    