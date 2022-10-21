def my_func():
    while True:
        try:
            x = int(input("Give me that number: "))
            break
        except ValueError:
            print("That not be a number.")
            continue
    return x

num1 = my_func()
print(num1)