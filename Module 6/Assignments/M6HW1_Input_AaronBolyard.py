# Aaron Bolyard
# 2018-07-16
# Common input methods.
# M6HW1_Input_AaronBolyard

def prettify_name(name):
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
	elif filter != None and not filter(result):
		print("Input value not valid; please try again.")
		return get_string(prompt, filter)

	return result

def get_float(prompt, filter=None):
	"""
	Gets an float from the user after presenting a prompt.

	Input is validated. A space is automatically appened to the end
	of the prompt.
	"""

	line = input(prompt + " ")
	try:
		value = float(line)

		if filter != None and not filter(value):
			print("Input value not valid; please try again.")
			return get_float(prompt, filter)

		return value
	except ValueError:
		print("Input not a number; please try again.")
		return get_float(prompt, filter)

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