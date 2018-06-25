# Aaron Bolyard
# 2018-06-18
# Generates a user CSV.
# X_GenerateUsers

import random

COUNT = 10

def getNames(filename):
	result = []

	with open(filename, 'r') as file:
		for line in file:
			names = line.split(",")
			for name in names:
				result.append(name.strip())

	return result

def generateStudentID():
	return random.randrange(200, 900) * 1000 + random.randrange(1000, 4000)

def main():
	firstNames = getNames("X_FirstNames.csv")
	lastNames = getNames("X_LastNames.csv")

	with open("accounts.csv", "w") as file:
		file.write("Aaron,Bolyard,3209132\n") # Include me!

		for i in range(COUNT):
			firstName = firstNames[random.randrange(0, len(firstNames))]
			lastName = lastNames[random.randrange(0, len(lastNames))]
			studentID = str(generateStudentID()).rjust(7, "0")

			file.write(str.format("{0},{1},{2}\n", firstName, lastName, studentID))

if __name__ == "__main__":
	main()
