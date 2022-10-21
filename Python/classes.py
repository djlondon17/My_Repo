class Pet():
    def __init__(self, name, species, breed, color, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.age = age

def get_age(name):
    while True:
        try:
            x = int(input(f"Enter {name}'s age: "))
            if x > 0:
                return x
            else:
                print("You need to have a positive value.")
        except ValueError:
            print("You need to enter a number.")

def main():
    pets= []
    add_another = 'y'
    while add_another != 'n':
        name = input("Enter your pet's name: ")
        species = input(f"Enter {name}'s species: ")
        breed = input(f"Enter {name}'s breed: ")
        color = input(f"Enter {name}'s color: ")
        age = get_age(name)
        pets.append(Pet(name, species, breed, color, age))
        while True:
            add_another = input("Do you have another pet?\n[Y|n]: ").lower()
            if add_another in ['y', 'n', '']:
                break
            else:
                print("You need to use 'y' for yes and 'n' for no.")
    for pet in pets:
        print(f"{pet.name} is a {pet.age} year old {pet.species} and is a {pet.color} {pet.breed}.")

if __name__ == '__main__':
    main()