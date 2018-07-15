# Aaron Bolyard
# 2018-07-15
# Car class usage.
# M5HW2

import M5HW2_Car_AaronBolyard as Car
from datetime import date

def get_integer(prompt, filter=None):
	"""
	Gets an integer from the user after presenting a prompt.

	Input is validated. A space is automatically appended to the end
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

def get_string(prompt, filter=None):
	"""
	Gets a string. Ignores emptry strings.

	An empty string is considered a string with no printable or escape
	characters; e.g., all whitespace or just a 0 length string.
	"""
	result = input(prompt + " ")

	if result.strip() == "":
		print("Please enter a value.")
		return get_string(prompt, filter)
	elif filter != None and not filter(value):
		print("Input value not valid; please try again.")
		return get_string(prompt, filter)

	return result

def validate_year(year):
	"""
	Validates a year within the possible times a car could be built.
	"""

	CAR_INVENTION_YEAR = 1885
	today = date.today()

	return year >= CAR_INVENTION_YEAR and year <= today.year + 1

def main():
	# Clamp year to the year the first car was invented to the current year.
	year = get_integer("Enter the year of the car:", validate_year)
	make = get_string("Enter the make of the car:").upper().strip()
	model = get_string("Enter the model of the car:").upper().strip()

	yearMake = str.format("{0} {1}", year, make)
	car = Car.Car(yearMake, model)

	for i in range(5):
		car.accelerate()
		message = str.format(
			"The {0} {1} has accelerated! Its speed is now {2} MPH.",
			car.get_year_model(), car.get_make(),
			car.get_speed())
		print(message)

	for i in range(5):
		car.brake()
		message = str.format(
			"The {0} {1} has braked! Its speed is now {2} MPH.",
			car.get_year_model(), car.get_make(),
			car.get_speed())
		print(message)

if __name__ == "__main__":
	main()
