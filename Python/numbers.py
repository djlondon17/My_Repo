'''
num1 = 0.1
num2 = 0.8
num3 = float(input("Give me a number with a decimal: "))

num4 = int(input("Give me a whole number: "))

num1 = int(num1)
print(num1, num2, num3, num4)


num1 = 0.1
num2 = 0.8

print(round(num1))
print(int(num1))
print(round(num2))
print(int(num2))
'''

num1 = 0.1187694857
num2 = 0.8349835972

print(round(num1, 2))
print(round(num2, 2))

print(f"${round(num1, 2)}")