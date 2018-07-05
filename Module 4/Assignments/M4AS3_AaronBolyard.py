# Aaron Bolyard
# 2018-07-04
# World Series Winners redux.
# M4AS3

def getTeams():
	"""
	Returns an array of winners from the file 'WorldSeriesWinners.txt'.

	If the file is not found or could not be read, returns an empty list.
	"""

	result = []

	try:
		with open("WorldSeriesWinners.txt", 'r') as file:
			for team in file:
				result.append(team.strip())
	except:
		print("File 'WorldSeriesWinners.txt' is either missing or has bad permissions.")

	return result

def generateWinnersDictionary(teams):
	"""
	Generates a dictionary of winners, where the key is the team and the value
	is the number of times the team won the world series.
	"""

	result = {}

	for team in teams:
		result[team] = result.get(team, 0) + 1

	return result

def generateYearsDictionary(teams):
	"""
	Generates a dictionary mapping years (key) to the team that won (value).
	"""

	START_YEAR = 1903

	result = {}
	currentYear = START_YEAR
	for team in teams:
		result[currentYear] = team
		currentYear += 1

	return result

def getShouldContinue():
	"""
	Returns true if the enter wants to continue, false otherwise.

	To continue, the user must enter 'y' or 'yes'. Similarly, to quit,
	the user must enter 'n' or 'no'. Any other values result in an error.
	"""

	result = None
	while result == None:
		answer = input("Continue? Enter y(es) or n(o): ").strip().lower()

		if answer == "y" or answer == "yes":
			result = True
		elif answer == "n" or answer == "no":
			result = False
		else:
			print("Please enter yes or no.")

	return result

def getYear():
	"""
	Prompts the user for a year. Clamps the year between 1903 and 2009.

	Returns a valid year.
	"""
	while True:
		value = input("What year should we check? ")

		try:
			integerValue = int(value)

			if integerValue < 1903:
				print("Please enter a year greater than or equal to 1903.")
			elif integerValue > 2009:
				print("Please enter a year less than or equal to 2009.")
			else:
				return integerValue
		except ValueError:
			print("Please enter a year as a whole integer.")
		except:
			print("An error ocurred. Please try again.")

def main():
	running = True
	teams = getTeams()
	winners = generateWinnersDictionary(teams)
	years = generateYearsDictionary(teams)
	while running:
		year = getYear()
		team = years.get(year, None)
		if team == None:
			print(str.format("Could not find team for year {0}.", year))
		else:
			print(str.format("'{0}' won the World Series in {1}.", team, year))

			count = winners.get(team, 1)
			print(str.format("They won the World Series {0} time(s) in total.", count))

		running = getShouldContinue()

if __name__ == "__main__":
	main()
