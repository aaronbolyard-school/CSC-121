# Aaron Bolyard
# 2018-07-09
# Sets operations on a file.
# M4AS2

def onlyAlpha(text):
	"""
	Extracts only alpha characters from 'text'.
	"""
	result = ""
	for character in text:
		if character.isalpha():
			result += character
	return result.lower()

def readWords(filename):
	"""
	Reads all the words from the file and returns a set of all unique files.
	"""
	result = set()

	with open(filename, 'r') as file:
		words = file.read().split()
		for word in words:
			result.add(onlyAlpha(word))

	return result


def main():
	setA = readWords("first_file.txt")
	setB = readWords("second_file.txt")

	print("unique words in first file:")
	print("\t", setA)

	print("unique words in second file:")
	print("\t", setB)

	print("words in first file but not second:")
	print("\t", setA - setB)

	print("words in the second file but not the first:")
	print("\t", setB - setA)

	print("words in first or second but not both:")
	print("\t", setA ^ setB)

if __name__ == '__main__':
	main()
