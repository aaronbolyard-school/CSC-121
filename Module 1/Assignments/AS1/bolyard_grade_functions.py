# Aaron Bolyard
# 2018-06-04
# This module exposes multiple functions to calculate grades.
# AS1

"""
This module exposes methods to retrieve and compute grades, including
letter point average.
"""

def get_input():
    """
    Gets the input from the user. Returns an integer.
    """

    num_grades = int(input("How many grades do you want to input? "))
    return num_grades

def get_average(num_grades):
    """
    Asks the user for 'num_grades' grades and returns the average.
    """

    total = 0
    for x in range (num_grades):
        grade = float(input("Enter a grade: "))
        total = grade + total
        
    average = total / num_grades
    return average

def get_letter_grade(average):
    """
    Gets the letter of 'average', using a 10 point scale from A-F.
    """

    grade = ""

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

def display_grade(average, letter_grade):
    """
    Displays the average, 'average', and letter grade, 'letter_grade'.
    """

    # print uses ' ' (space) as sep by default so no need to add space in string
    print("Your average is", average, "which is a letter grade of", letter_grade)
