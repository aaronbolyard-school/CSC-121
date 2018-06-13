# Aaron Bolyard
# 2018-06-13
# Informs the user of the number of times a team won.
# M2HW2

def getTeams():
	"""
	Returns an array of winners from the file 'WorldSeriesWinners.txt'.

	If the file is not found or could not be read, returns an empty list.
	"""

	result = []

	try:
		with open("WorldSeriesWinners.txt") as file:
			for team in file:
				result.append(team.strip())
	except:
		print("File 'WorldSeriesWinners.txt' is either missing or has bad permissions.")

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

def getNumWins(teams, query):
	"""
	Searches 'teams' for 'query'.

	Returns the number of times 'query' is in 'teams'. Case is ignored.
	Whitespace is trimmed.
	"""

	count = 0
	for team in teams:
		if team.lower() == query.strip().lower():
			count += 1
	return count

def prettifyTeamName(team):
	"""
	Prettifies a team name.

	Converts a name into the form where each word ('term') starts with a capital
	letter (and the remainder are lower-case); and there is a single space between
	each term.
	"""

	name = team.strip().split()
	prettyName = ""
	for term in name:
		prettyName += term[0:1].upper()
		prettyName += term[1:].lower()
		prettyName += " "

	# Final strip to remove extra " ".
	# The logic above would give the name "Boston Red Sox ", but that's incorrect.
	return prettyName.strip()

def main():
	running = True
	teams = getTeams()
	while running:
		team = prettifyTeamName(input("Enter a team name: "))
		count = getNumWins(teams, team)
		print(str.format("'{0}' won the World Series {1} time(s).", team, count))

		running = getShouldContinue()

if __name__ == "__main__":
	main()
