# Aaron Bolyard
# 2018-07-04
# Decrypts a file using ROT13.
# M4AS1_Decrypt

import M4AS1_Common as ROT
import sys

def main():
	filename = "test.txt.enc"
	if len(sys.argv) > 1: 
		filename = sys.argv[1]

	toROT13, fromROT13 = ROT.generate(13)
	with open(filename) as file:
		result = ROT.transform(fromROT13, file.read())
		print(result)

if __name__ == "__main__":
	main()
