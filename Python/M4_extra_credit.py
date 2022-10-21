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
    same_number = 'y'
    while response != 'n':
        answer = main_calculator()
        while True:
            response = input("Would you like to do another calcualtion?\n[Y|n]: ").lower()
            if response in ["y", ""]:
                while same_number != 'n':
                    same_number = input("Would you like to use the result for the new calculation?\n[Y|n]: ").lower()
                    if same_number in ['y', '']:
                        print("Temp")
                    elif same_number == 'n':
                        break
                    else:
                        print("Input error: Please use 'y' or 'n'.")
                        continue
            elif response == 'n':
                quit()
            else:
                print("Input error: Please use 'y' or 'n'.")


print("Welcome to the better calculator.")
loop()