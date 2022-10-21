## REQUIREMENTS:
## Get the name of a person: DONE
## Get the price of their meal: DONE
## Find the total price of all food: DONE
## Find the number of items added: DONE
## Find the average: DONE
## Output results



def get_price():
    while True:
        try:
            x = float(input("Enter the price of the meal: "))
            if x < 0:
                print("Please don't use negative numbers.")
                continue
            else:
                break
        except ValueError:
            print("Please use a number.")
            continue
    return x

def main():
    name_list = []
    price_list = []
    go_again = 'y'

    while go_again != 'n':
        name_list.append(input("Who ate a meal: "))
        price_list.append(get_price())
        while True:
            go_again = input("Do you have more people to add? [Y|n]: ").lower()
            if go_again in ['y', '', 'n']:
                break
            else:
                print("Please use a 'y' for yes or a 'n' for no.")
    total = sum(price_list)
    items_in_list = len(price_list)
    average = total / items_in_list
    for person, price in zip(name_list, price_list):
        diff = average - price
        if diff < 0:
            diff = abs(diff)
            print(person, "paid $", diff, "above the average.")
        else:
            print(person, "paid $", diff, "below the average.")





main()