def question_one():
    from random import shuffle as shuf
    score = 0
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is the color of the sky?")
    choices = ['Blue', 'Green', 'Red', 'Black']
    letters = ['A', 'B', 'C', 'D']
    shuf(choices)
    for letter, choice in zip(letters, choices):
        print(letter, choice)
    answer = input("Answer: ").upper()


    if answer in ['A', 'B', 'C', 'D']:
        if answer == 'A':
            if choices[0] == 'Blue':
                score += 1
        elif answer == 'B':
            if choices[1] == 'Blue':
                score =+ 1
        elif answer == 'C':
            if choices[2] == 'Blue':
                score += 1
        elif answer == 'D':
            if choices[3] == 'Blue':
                score += 1
    else:
        print("That is not a valid answer.")
    return score

def question_two():
    from random import shuffle as shuf
    score = 0
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is 10 * 10?")
    choices = ['100', '1000', '10', '1']
    letters = ['A', 'B', 'C', 'D']
    shuf(choices)
    for letter, choice in zip(letters, choices):
        print(letter, choice)
    answer = input("Answer: ").upper()


    if answer in ['A', 'B', 'C', 'D']:
        if answer == 'A':
            if choices[0] == '100':
                score += 1
        elif answer == 'B':
            if choices[1] == '100':
                score =+ 1
        elif answer == 'C':
            if choices[2] == '100':
                score += 1
        elif answer == 'D':
            if choices[3] == '100':
                score += 1
    else:
        print("That is not a valid answer.")
    return score

def question_three():
    from random import shuffle as shuf
    score = 0
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is the meaning of life?")
    choices = ['42', 'Family', 'Money', 'Fame']
    letters = ['A', 'B', 'C', 'D']
    shuf(choices)
    for letter, choice in zip(letters, choices):
        print(letter, choice)
    answer = input("Answer: ").upper()


    if answer in ['A', 'B', 'C', 'D']:
        if answer == 'A':
            if choices[0] == '42':
                score += 1
        elif answer == 'B':
            if choices[1] == '42':
                score =+ 1
        elif answer == 'C':
            if choices[2] == '42':
                score += 1
        elif answer == 'D':
            if choices[3] == '42':
                score += 1
    else:
        print("That is not a valid answer.")
    return score

def question_four():
    from random import shuffle as shuf
    score = 0
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is the capital of Indiana")
    choices = ['Indianapolis', 'Bloomington', 'Fort Wayne', 'Evansville']
    letters = ['A', 'B', 'C', 'D']
    shuf(choices)
    for letter, choice in zip(letters, choices):
        print(letter, choice)
    answer = input("Answer: ").upper()


    if answer in ['A', 'B', 'C', 'D']:
        if answer == 'A':
            if choices[0] == 'Indianapolis':
                score += 1
        elif answer == 'B':
            if choices[1] == 'Indianapolis':
                score =+ 1
        elif answer == 'C':
            if choices[2] == 'Indianapolis':
                score += 1
        elif answer == 'D':
            if choices[3] == 'Indianapolis':
                score += 1
    else:
        print("That is not a valid answer.")
    return score

def question_five():
    from random import shuffle as shuf
    score = 0
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is 108 in binary?")
    choices = ['01101100', '10011001', '01110000', '10101010']
    letters = ['A', 'B', 'C', 'D']
    shuf(choices)
    for letter, choice in zip(letters, choices):
        print(letter, choice)
    answer = input("Answer: ").upper()


    if answer in ['A', 'B', 'C', 'D']:
        if answer == 'A':
            if choices[0] == '01101100':
                score += 1
        elif answer == 'B':
            if choices[1] == '01101100':
                score =+ 1
        elif answer == 'C':
            if choices[2] == '01101100':
                score += 1
        elif answer == 'D':
            if choices[3] == '01101100':
                score += 1
    else:
        print("That is not a valid answer.")
    return score

def main():
    from random import shuffle as shuf
    score = 0
    question_list = [question_one(), question_two(), question_three(), question_four(), question_five()]
    shuf(question_list)
    for question in question_list:
        score += question

main()
