## REQUIREMENTS
## Make a random number
## Gete user input: DONE
## make sure number is in range 1 to 100 from input: DONE
## make comparisons


from random import randint

def get_num():
    while True:
        try:
            x = int(input("Give a numbe between 1 and 100: "))
            if x < 1 or x > 100:
                print("Your number is outside the range.")
                continue
            else:
                break
        except ValueError:
            print("You did not enter a number.")
            continue
    return x

def play_again():
    while True:
        again = input("Would you like to play again? [Y|n]").lower()
        if again in ['y', '']:
            main()
        elif again == 'n':
            exit()
        else:
            print("please select 'y' for yes and 'n' for no")

def main():
    number = randint(1,100)
    count = 0
    while count < 5:
        guess = get_num()
        if number < guess:
            print("Your guess is too high.")
            count += 1
        elif number > guess:
            print("Your guess is too low.")
            count += 1
        else:
            print("You guess the number.")
            break
    if count == 5:
        print("You lose, the number was " + str(number))
    play_again()

main()