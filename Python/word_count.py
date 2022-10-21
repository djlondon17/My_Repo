with open("saved_file.txt", 'r') as file:
    count = {}
    total = 0
    for i in file:
        count[i] = count.get(i, 0) + 1
    print(count)