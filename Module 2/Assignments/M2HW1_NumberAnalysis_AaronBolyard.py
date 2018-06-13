# Aaron Bolyard
# 2018-06-13
# Provides some information about numbers entered by user.
# M2HW1

import math

# How many numbers the user should enter.
# This is specified by assignment, but in the future could be requested
# from the user.
COUNT = 20

def get_integer(prompt, filter=None):
	"""
	Gets an integer from the user after presenting a prompt.

	Input is validated. A space is automatically appened to the end
	of the prompt.
	"""

	line = input(prompt + " ")
	try:
		value = int(line)

		if filter != None and not filter(value):
			print("Input value not valid; please try again.")
			return get_integer(prompt, filter)

		return value
	except ValueError:
		print("Input not an integer; please try again.")
		return get_integer(prompt, filter)

def main():
	numbers = []

	print(str.format("This program will print some information about {0} number(s).", COUNT))
	for i in range(0, COUNT):
		value = get_integer("Enter a number:")
		numbers.append(value)

	print("Max:", max(numbers))
	print("Min:", min(numbers))
	print("Sum:", sum(numbers))
	print("Average:", math.floor(sum(numbers) / len(numbers)))

if __name__ == "__main__":
	main()
