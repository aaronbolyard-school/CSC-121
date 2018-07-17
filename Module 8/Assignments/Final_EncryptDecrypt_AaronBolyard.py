# Aaron Bolyard
# 2018-07-16
# Encrypts and decrypts text using a user-specified ROT scheme.
# Final_EncryptDecrypt

import tkinter as tk
from tkinter import ttk

import Final_ROT_AaronBolyard as ROT

def main():
	root = tk.Tk()
	root.title("ROT Encrypt/Decrypt")
	root.geometry("300x200")

	frame = ttk.Frame(root, padding="10 10 10 10")
	frame.pack(fill=tk.BOTH, expand=True)

	shiftFrame = ttk.Frame(frame, padding="10 10 10 10")

	shiftLabel = ttk.Label(shiftFrame, text="ROT Shift")
	shiftLabel.grid(column=0, row=0)

	shiftValue = tk.IntVar()
	shiftValue.set(13)
	shiftEntry = ttk.Entry(shiftFrame, width=3, textvariable=shiftValue)
	shiftEntry.grid(column=1, row=0)

	shiftFrame.pack()

	inputValue = tk.StringVar()
	inputEntry = ttk.Entry(frame, width=100, textvariable=inputValue)
	inputEntry.pack()

	inputValue.set("Enter input text here.")

	outputValue = tk.StringVar()
	outputEntry = ttk.Entry(frame, width=100, textvariable=outputValue)
	outputEntry.pack()

	inputValue.set("This will contain the output.")

	def encode():
		shift = shiftValue.get()
		plaintext = inputValue.get()

		encodeTable, decodeTable = ROT.generate(shift)
		result = ROT.transform(encodeTable, plaintext)

		outputValue.set(result)

	def decode():
		shift = shiftValue.get()
		plaintext = inputValue.get()

		encodeTable, decodeTable = ROT.generate(shift)
		result = ROT.transform(decodeTable, plaintext)

		outputValue.set(result)

	def swap():
		plaintext = inputValue.get()
		encrypted = outputValue.get()

		outputValue.set(plaintext)
		inputValue.set(encrypted)

	buttonFrame = ttk.Frame(frame, padding="10 10 10 10")

	encodeButton = ttk.Button(buttonFrame, text="Encode", command=encode)
	encodeButton.grid(column=0, row=0)
	decodeButton = ttk.Button(buttonFrame, text="Decode", command=decode)
	decodeButton.grid(column=1, row=0)
	swapButton = ttk.Button(buttonFrame, text="Swap", command=swap)
	swapButton.grid(column=2, row=0)

	buttonFrame.pack(fill=tk.BOTH, expand=True)

	root.mainloop()

if __name__ == "__main__":
	main()
