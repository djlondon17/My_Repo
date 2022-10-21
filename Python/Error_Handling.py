# x = int(input("Give me that number!!! "))
# print(x)

while True:
    try:
        x = int(input("Give me that number: "))
        break
    except ValueError:
        print("You did not give me that number.")
        continue

print(x)