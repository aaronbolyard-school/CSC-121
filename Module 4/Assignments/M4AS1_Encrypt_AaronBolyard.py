# Aaron Bolyard
# 2018-07-04
# Encrypts a file using ROT13.
# M4AS1_Encrypt

import M4AS1_Common as ROT
import sys

def main():
	filename = "test.txt"
	if len(sys.argv) > 1: 
		filename = sys.argv[1]

	toROT13, fromROT13 = ROT.generate(13)
	with open(filename) as file:
		result = ROT.transform(toROT13, file.read())

		with open(filename + ".enc", 'w') as output:
			output.write(result)

if __name__ == "__main__":
	main()
