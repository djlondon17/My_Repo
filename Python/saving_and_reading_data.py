## Author: David London
## Looked up information at www.w3schools.com

def main():
    import os

    os.system('cls' if os.name == 'nt' else 'clear') # Clears the screen
    
    try:
        with open("how_is_your_day.txt", 'r') as file:  # Opens the text file to be read from
            for line in file:
                if line in ['good', 'bad']:
                    print(f"You are having a {line} day.")
        os.remove("how_is_your_day.txt")  # Deletes the file from the computer
    except FileNotFoundError:   # Takes effect if the file does not exist
        with open('how_is_your_day.txt', 'w') as file:  # Opens the text file to be written over
            while True:
                answer = (input("Are you having a good or bad day? ")).lower()
                if answer in ['good', 'bad']:
                    file.write(answer)
                    break
                else:
                    print("That is not a valid answer")
                    continue

if __name__ == '__main__':  # Runs the program only if it is the main program
    main()