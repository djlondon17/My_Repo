# Author: David London

currency = {"Hundreds":100, "Fifties":50, "Twenties":20, "Tens":10, "Fives":5, "Ones":1, "Quarters":0.25, "Dimes":0.10, "Nickels":0.05, "Pennies":0.01}

def get_value(size):  # Function to get the number of bills/coins per value
    while True:
        try:
            number_of_currency = int(input(f"Enter the number of {size}: "))
            if number_of_currency < 0:  # Ensures the entry is a positive number
                print("Enter a positive value.")
            else:
                return number_of_currency
        except ValueError:  # Ensures that only a whole number is entered
            print("Enter a whole number.")

def main():
    grand_total = 0
    add_another = 'y'
    store_names = []
    store_totals = []
    while add_another != 'n':
        store_total = 0
        store_names.append(input("Enter the name or location of the store: "))   # Adds the name of the store to a list
        for size, value in currency.items():
            store_total += (get_value(size) * value)
        store_totals.append(store_total)     # Adds the total money of the store to a list
        grand_total += store_total  # Keeps a running grand total from all the stores
        while True:
            add_another = input("Do you have another store to add?\n[Y|n]: ").lower()  # After finishing with a store, asks the usere if they want to add another
            if add_another in ['y', 'n', '']:
                break
            else:
                print("You need to use 'y' for yes and 'n' for no.")
    
    while True:
        text_file = input("Would you like to save this information to a text file?\n[Y|n]: ").lower()
        if text_file in ['y', '']:
            with open('Store_Totals.txt', 'w') as file:   # Opens/Creates a text file to save the inputted information
                file.write("Store Totals:\n")
                for name, total in zip(store_names, store_totals):  # Ties the two created list together 
                    file.write(f"{name}: ${total:.2f}\n")           # Writes the information from the lists to the file
                file.write(f"Grand Total: ${grand_total:.2f}")
                break
        elif text_file == 'n':
            break
        else:
            print("You need to use 'y' for yes and 'n' for no.")
    
    print("Store Totals:")
    for name, total in zip(store_names, store_totals):
        print(f"{name}: ${total:.2f}")

    print(f"Grand Total: ${grand_total:.2f}")

if __name__ == '__main__':  # Makes sure the program only runs if it is the main program
    main()
