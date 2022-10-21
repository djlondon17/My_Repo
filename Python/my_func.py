def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            print("You did not enter a number.")
            continue