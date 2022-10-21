class Pet:
    def __init__(self, breed, color, species, name):
        self.breed = breed
        self.color = color
        self.species = species
        self.name = name

def main():
    breed = input("What breed is your pet? ")
    color = input("What color is your pet? ")
    species = input("What species is your pet? ")
    name = input("What is your pet's name? ")
    pet1 = Pet(breed, color, species, name)
    print(f"{pet1.name} is a {pet1.species}, and it is a {pet1.color} {pet1.breed}")

if __name__ == "__main__":
    main()