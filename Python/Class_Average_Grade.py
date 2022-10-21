def Get_Student_Grade():
    while True:
        student_grade = input("Please give the grade of the student (A, B, C, D, or F): ").upper()
        if student_grade in ['A', 'B', 'C', 'D', 'F']:
            break
        else:
            print("That is not a valid entry.")
            continue
    return student_grade

def class_grades():
    student_name = []
    student_grade = []
    go_again = 'y'
    total_grade = 0

    class_name = input("What is the name of the class?: ")
    while go_again != 'n':
            student_name.append(input("Please give me the name of a student: ")) ## Adds the student's name to the list
            student_grade.append(Get_Student_Grade()) ## Adds the student's grade to the list
            while True:
                go_again = input("Do you have another student to add? [Y|n]: ").lower()  ## Ask the user if they want to add more students to the list
                if go_again in ['y', '', 'n']:
                    break
                else:
                    print("Please use a 'y' for yes or a 'n' for no.")

    for grade in student_grade: ## Adds up the total value of the students grades
        if grade == 'A':
            total_grade += 4
        if grade == 'B':
            total_grade += 3
        if grade == 'C':
            total_grade += 2
        if grade == 'D':
            total_grade += 1
        if grade == 'F':
            total_grade += 0

    average_grade = total_grade / len(student_grade) ## Calculates the class average on a 4.0 scale
   
    print(f"For the {class_name} class:")

    for name, grade in zip(student_name, student_grade):
        print(f"{name} received a(n) {grade} for the class.")

    print(f"The class average on a 4 point scale is {average_grade:.1f}")

def main():
    response = 'y'
    while response != 'n':
        class_grades()
        while True:
            response = input("Would you like to add another class?\n[Y|n]: ").lower()
            if response in ["y", "n", ""]:
                break
            else:
                print("Input error: Please use 'y' or 'n'.")




main()