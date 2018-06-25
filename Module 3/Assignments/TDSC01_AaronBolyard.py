# Aaron Bolyard
# 2018-06-18
# Generates a report.
# TDSC01

def parseInteger(string, start, stop):
	return int(string[start:stop])

class Row:
	storeNumber = 0
	itemID = 0
	customerName = "N/A"
	itemDescription = "N/A"
	price = 0.00

	def __init__(self, line):
		self.extractStoreNumber( line)
		self.extractItemID( line)
		self.extractCustomer( line)
		self.extractItemDescription( line)
		self.extractPrice( line)

	def extractStoreNumber(self, line):
		START = 0
		STOP  = 2
		try:
			self.storeNumber = parseInteger(line, START, STOP)
		except:
			print("Store number invalid; expected integer.")
			return 0

	def extractItemID(self, line):
		START = 7
		STOP  = 13
		self.itemID = line[START:STOP]

	def extractCustomer(self, line):
		START = 13
		STOP  = 33
		self.customerName = line[START:STOP].strip()

	def extractItemDescription(self, line):
		START = 33
		STOP  = 48
		self.itemDescription = line[START:STOP].strip()

	def extractPrice(self, line):
		START = 75
		STOP  = 80
		try:
			self.price = parseInteger(line, START, STOP) / 100
		except:
			print("Price invalid; expected fixed-point value.")

def main():
	rows = []

	with open("tdsc01.txt", 'r') as file:
		for line in file:
			rows.append(Row(line))

	print(str.format(
		"{0:7} {1:20} {2:15} {3:6}",
		"ItemID",
		"Buyer",
		"Item Name",
		"Price"))

	for row in rows:
		line = str.format(
			"{0:3}-{1:3} {2:20} {3:15} ${4:7}",
			row.itemID[0:3], str(row.itemID)[3:6],
			row.customerName,
			row.itemDescription,
			str(format(row.price, ".2f").rjust(6, "0")))
		print(line)

	print()
	print("SUMMARY")
	print()

	total = 0
	for row in rows:
		total += row.price

	print(str.format("Total Sales: {0}", len(rows)))
	print(str.format("Total Sales Value: ${0:,.2f}", total))
	print(str.format("Average Sale Value: ${0:,.2f}", total / len(rows)))

if __name__ == "__main__":
	main()
