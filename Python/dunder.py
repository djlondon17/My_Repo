import func1

def potato():
    print("Hello Dunder!")
    print(__name__)
    x = func1.my_func()
    print(x)

if __name__ == "__main__":
    potato()