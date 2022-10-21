counter = 10
while True:
    print(counter)
    counter -= 1
    if counter == 0:
        print("Loop be gone!")
        print(counter)
        break
    else:
        continue