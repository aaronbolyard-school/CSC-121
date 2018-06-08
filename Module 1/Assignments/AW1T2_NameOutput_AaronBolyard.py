# Aaron Bolyard
# 2018-06-06
# Reads a name from a file.
# AW1T2

def main():
	"""
	Opens a file, 'my_name.txt', and reads a name from it.
	Prints said name to console.
	"""

	with open("my_name.txt", "r") as file:
		line = file.readline()
		print("Name:", line.rstrip())

if __name__ == "__main__":
	main()
