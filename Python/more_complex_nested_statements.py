my_list = []
question = "y"

while question != "n":
    my_list.append(input("Give me an item name: "))
    while True:
        question = input("Would you like to add another?\n[Y|n]: ")
        if question in ["y", "n", ""]:
            break
        else:
            print("Input error: Please use 'y' or 'n'.")

print(my_list)