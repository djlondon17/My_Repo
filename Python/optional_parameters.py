from re import sub


def add(x, y):
    return x + y

#print(add(4, 5))

def subtraction(x, y=6):
    return x - y

#print(subtraction(5, 4))

def product(x=2, y=3):
    return x * y

print(product())
print(product(5, 8))