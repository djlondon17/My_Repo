## REQUIREMENTS
## Take numbers from the user and store them as variables: Done
## Not Crash if strings are entered when numbers are expected: Done
## Choice of addition, subtraction, multiplication, and division: Done
## The program should not crash if an error happens during math type selection: Done
## The program should not crash from a division by zero error: Done

## Extra Credit

## The program does all of the above: Done
## The program allows for continus calculations untill the user wants to 'quit': Done
## The program takes the output from the first calculation, uses that as the input for the first number for the second calculation

def Get_Number():
    while True:    
        try:
            number = float(input("Give me a number: "))
            break
        except ValueError:
            print("That is not a number.")
            continue
    return number

def main_calculator():
    first_number = Get_Number()
    while True:    
        try:
            operator = int(input("What math operator do you want to use?\nType '1' for addition.\nType '2' for subtraction.\nType '3' for multiplication\nType '4' for division.\n"))
            if operator > 4 or operator < 1:
                print("That is not a valid answer")
                continue
            elif operator == 1:
                second_number = Get_Number()
                answer = first_number + second_number
                print(answer)
            elif operator == 2:
                second_number = Get_Number()
                answer = first_number - second_number
                print(answer)
            elif operator == 3:
                second_number = Get_Number()
                answer = first_number * second_number
                print(answer)
            elif operator == 4:
                while True:
                    try:
                        second_number = Get_Number()
                        answer = first_number / second_number
                        print(answer)
                        break
                    except ZeroDivisionError:
                        print("You can't divide by zero.")
                        continue
            break
        except ValueError:
            print("That is not a valid answer.")
            continue
    return answer

def loop():
    response = 'y'
    while response != 'n':
        main_calculator()
        while True:
            response = input("Would you like to do another calcualtion?\n[Y|n]: ").lower()
            if response in ["y", "n", ""]:
                break
            else:
                print("Input error: Please use 'y' or 'n'.")

print("Welcome to the better calculator!")
loop()