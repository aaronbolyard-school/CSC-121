# Aaron Bolyard
# 2018-06-06
# Generates numbers. Prints the average of the numbers generated.
# X1

import random

MIN_NUMBER = 0
MAX_NUMBER = 100
NUMBER_COUNT = 50

def main():
	random.seed(None)

	total = 0
	with open("numbers.txt", "w") as file:
		for i in range(0, NUMBER_COUNT):
			value = random.randrange(MIN_NUMBER, MAX_NUMBER)
			total += value
			print(str.format("value: {0}, total: {1}", value, total))

			file.write(str(value))
			file.write("\n")
	average = total / NUMBER_COUNT
	print(str.format("average of {0} value(s): {1:.2f}", NUMBER_COUNT, average))

if __name__ == "__main__":
	main()
