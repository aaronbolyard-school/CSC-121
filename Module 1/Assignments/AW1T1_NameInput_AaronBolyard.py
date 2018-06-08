# Aaron Bolyard
# 2018-06-06
# Writes my name to a file.
# AW1T1

def main():
	"""
	Creates a file, 'my_name.txt', and writes my name to it.
	"""

	with open("my_name.txt", "w") as file:
		file.write("Aaron Bolyard")

if __name__ == "__main__":
	main()
