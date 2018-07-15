# Aaron Bolyard
# 2018-07-11
# Uses the pet class.
# M5HW1

import M5HW1_Pet_AaronBolyard as Pet

def prettifyName(name):
	"""
	Prettifies a name.

	Converts a name into the form where each word ('term') starts with a capital
	letter (and the remainder are lower-case); and there is a single space between
	each term.
	"""

	name = name.strip().split()
	prettyName = ""
	for term in name:
		prettyName += term[0:1].upper()
		prettyName += term[1:].lower()
		prettyName += " "

	# Final strip to remove extra " ".
	# The logic above would give the name "Boston Red Sox ", but that's incorrect.
	return prettyName.strip()

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
	name = prettifyName(input("What is the name of the pet? ").strip())
	type = prettifyName(input(str.format("What is {0}'s species? ", name)).strip())
	age = get_integer(str.format("What is {0}'s age?", name))

	try:
		pet = Pet.Pet(name, type, age)

		print(str.format("The pet, {0}, is a(n) {1} year(s) old {2}.", pet.get_name(), pet.get_age(), pet.get_animal_type().lower()))
	except ValueError as error:
		print("Oops:", error)
	except Exception as error:
		print("Unknown error ocurred.", error)

if __name__ == "__main__":
	main()
