names = []
price = []
question = "y"
total = 0

while question != "n":
    names.append(input("What is your name?\n"))
    while True:
        try:
            price.append(float(input("How much is your food?\n")))
            while True:
                question = input("Would you like to add another?\n[Y|n]: ")
                if question in ["y", "n", ""]:
                    break
                else:
                    print("Input error: Please use 'y' or 'n'.")
            break
        except ValueError:
            print("That is not a valid answer.")

for i in range(0, len(price)):
    total = total + price[i]

average_price = total / len(price)

for j, k in zip(names, price):
    if k > average_price:
        print(f"{j}'s price is {round(k - average_price, 2)} above the average price")
    elif k < average_price:
        print(f"{j}'s price is {round(average_price - k, 2)} below the average price")