# Aaron Bolyard
# 2018-06-06
# Calculates the average of numbers from a file.
# M1HW1

def main():
	"""
	Calculates the average of numbers from 'numbers.txt'.

	Empty lines are ignored. Input is not otherwise validated.

	Prints the average and number of values at the end.
	"""

	total      = 0 # The sum of all valid values (lines with integers) in the file.
	num_values = 0 # The number of valid values in the file. This is not the same as line count.
	average    = 0 # The average (total / num_values) of the values in the file.

	with open("numbers.txt", "r") as file:
		for line in file:
			# Strip line to eliminate unnecessary whitespace.
			# For example, the newline character is included in the input.
			stripped_line = line.strip()

			# Ignore empty lines. By stripping all whitespace, we handle any empty line;
			# in other words, a line with all whitespace.
			if stripped_line != "":
				value = int(stripped_line)
				total += value
				num_values += 1

	average = total / num_values

	print(str.format("Average of {1} numbers: {0:.2f}", average, num_values))

if __name__ == "__main__":
	main()
