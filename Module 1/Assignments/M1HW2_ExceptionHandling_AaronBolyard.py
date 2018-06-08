# Aaron Bolyard
# 2018-06-06
# Calculates the average of numbers from a file. Handles exceptions.
# M1HW2

def main():
	"""
	Calculates the average of numbers from 'numbers.txt'.

	Empty lines are ignored. Input is validated:
	  * Handles garbage lines by ignoring the value.
	  * Handles file errors by... not reading the file.
	  * Handles empty set (i.e., division by zero) properly.

	Prints a useful prompt when encountering an error.

	Prints the average and number of values at the end.
	"""

	total      = 0 # The sum of all valid values (lines with integers) in the file.
	num_values = 0 # The number of valid values in the file. This is not the same as line count.
	average    = 0 # The average (total / num_values) of the values in the file.

	try:
		# Keep track of line number for error messages.
		# Unlike num_values, there may be more lines than values.
		#
		# For example, a file with 3 integers, 1 text string, and 10 empty lines would have...
		#  num_values = 3
		#  line_number = 14
		# ...by program termination.
		line_number = 1

		with open("numbers.txt", "r") as file:
			for line in file:
				# Strip line to eliminate unnecessary whitespace.
				# For example, the newline character is included in the input.
				stripped_line = line.strip()

				# Ignore empty lines. By stripping all whitespace, we handle any empty line;
				# in other words, a line with all whitespace.
				if stripped_line.strip() != "":
					try:
						value = int(stripped_line)
						total += value
						num_values += 1
					except ValueError:
						print(str.format("Line {0} has invalid value ('{1}'); expected integer.", line_number, stripped_line))
					except:
						# What monsters have stirred?
						print("Unknown error occurred while reading numbers (line {0}).", line_number)
				line_number += 1
	except IOError:
		print("Could not open 'numbers.txt' for reading.")
		print("Does the file exist or are the permissions valid?")
	except:
		# What sort of ghosts are in the machine?
		print("Unknown error occurred.")

	try:
		average = total / num_values
		print(str.format("Average of {1} numbers: {0:.2f}", average, num_values))
	except ZeroDivisionError:
		# We could also just see of num_values == 0 but this is more consistent.
		print("No values to average; attempted to divide by zero.")

if __name__ == "__main__":
	main()
