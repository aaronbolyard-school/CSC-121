# Aaron Bolyard
# 2018-07-04
# Common functions for M4AS1.
# M4AS1_Common

def wrap(value, minRange, maxRange):
	"""
	Wraps 'value' into [minRange, maxRange].

	Returns the wrapped value.
	"""
	before = value
	while value > maxRange:
		value -= maxRange
	while value < minRange:
		value += minRange
	return value

def generate(n):
	"""
	Generates a ROT table for N. All printable characters, excluding the space,
	are included in the space.

	For example, a ROT(1) table will make A -> B, while a ROT(13) will make A
	-> N.

	Returns two ROT tables; the first converts from ASCII to ROT(n), while the
	second converts from ROT(n) to ASCII.
	"""

	toROTn = {}
	fromROTn = {}

	# Only include printable ASCII characters, minus space.
	for character in range(33, 126):
		key = chr(character)
		value = chr(wrap(character + n, 33, 126))
		toROTn[key] = value
		fromROTn[value] = key

	return toROTn, fromROTn

def transform(table, text):
	"""
	Transforms text by a ROT(n) table, or something similiar.

	Any characters not found in the ROT(n) table are left untouched.

	Returns the transformed text.
	"""
	result = ""

	for character in text:
		result += table.get(character, character)

	return result
