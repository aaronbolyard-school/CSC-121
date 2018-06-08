# Aaron Bolyard
# 2018-06-04
# This program utilizes multiple files to calculate grades.
# AS1

import bolyard_grade_functions as Grader

def main():
	"""
	Main function. Performs program logic: getting input, computing grade, and then
	displaying grade.
	"""

	# Get the number of grades.
	num_grades = Grader.get_input()

	# Compute the average.
	average = Grader.get_average(num_grades)

	# Determine the letter grade.
	letter_grade = Grader.get_letter_grade(average)

	# Display the results.
	Grader.display_grade(average, letter_grade)

if __name__ == '__main__':
	main()
