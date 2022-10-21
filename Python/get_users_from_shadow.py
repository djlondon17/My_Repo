def main():
    users = []
    shadows = []
    try:
        with open("shadow.csv", "r") as shadow:
            for line in shadow:
                #print(line)
                #seperated = line.split(",")
                #print(seperated)
                #users.append(seperated[0])
                #shadows.append(seperated[1].strip())
                users.append(line.split(",")[0])
                shadows.append(line.split(",")[1].strip())
    except FileNotFoundError:
        print("No shadow file found. Please run make_a_shadow_file.py")
    print(users, shadows)


if __name__ == '__main__':
    main()