# Aaron Bolyard
# 2018-06-18
# Generates an FTCC username and email from text file.
# M3P1

class Row:
	"""
	Stores a row from the accounts CSV.

	A row is in the form (first name, last name, student id).
	"""
	firstName = ""
	lastName = ""
	studentID = 0

	COLUMN_FIRST_NAME = 0
	COLUMN_LAST_NAME  = 1
	COLUMN_STUDENT_ID = 2

	def __init__(self, line):
		columns = line.split(",")

		self.firstName = columns[self.COLUMN_FIRST_NAME].strip()
		self.lastName = columns[self.COLUMN_LAST_NAME].strip()
		self.studentID = int(columns[self.COLUMN_STUDENT_ID].strip())

	def readRows(filename):
		"""
		Reads a list of rows from 'filename' and returns it.
		"""

		result = []

		try:
			lineNumber = 1
			with open(filename, 'r') as file:
				for line in file:
					try:
						result.append(Row(line))
					except ValueError:
						print(str.format("line {0}: Student ID invalid.", lineNumber))
					except IndexError:
						print(str.format("line {0}: Missing column.", lineNumber))
					except:
						print(str.format("line {0}: Unknown error.", lineNumber))

					lineNumber += 1
		except IOError:
			print(str.format("Couldn't open '{0}'; file not found or bad permissions.", filename))
		except:
			print("Unknown error.")

		return result

def formatUsername(firstName, lastName, studentID):
	f = firstName[0:1].lower()
	l = lastName[0:7].lower()
	i = str(studentID)[0:7].rjust(7, "0")[3:7]

	return str.format("{0}{1}{2}", l, f, i)

def formatEmail(username):
	return str.format("{0}@student.faytechcc.edu", username)

def main():
	rows = Row.readRows("accounts.csv")
	
	header = str.format(
		"{0:7} {1:10} {2:10} {3:12} {4}",
		"ID", "FirstName", "LastName", "Username", "Email")
	print(header)

	for row in rows:
		username = formatUsername(row.firstName, row.lastName, row.studentID)
		email = formatEmail(username)

		result = str.format(
			"{0:7} {1:10} {2:10} {3:12} {4}",
			str(row.studentID).rjust(7, "0"),
			row.firstName,
			row.lastName,
			username,
			email)
		print(result)

if __name__ == "__main__":
	main()
