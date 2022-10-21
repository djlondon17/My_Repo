def my_func():
    print(__name__)
    while True:
        try:
            x = int(input("Give num or else: "))
            return x
        except ValueError:
            print("Nope")
            continue

if __name__ == "__main__":
    num1 = my_func()
    print(num1)