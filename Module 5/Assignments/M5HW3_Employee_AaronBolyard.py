# Aaron Bolyard
# 2018-07-15
# Employee class.
# M5HW3_Employee

class Employee:
	"""
	Represents an employee.
	"""

	def __init__(self, name, id, department, title):
		"""
		Constructs an employee.
		"""

		self.__name = name
		self.__id = id
		self.__department = department
		self.__title = title

	def get_name(self):
		"""
		Gets the name of the employee.
		"""

		return self.__name

	def set_name(value):
		"""
		Sets the name of the employee.
		"""

		self.__name = value

	def get_id(self):
		"""
		Gets the ID of the employee.
		"""

		return self.__id

	def set_id(value):
		"""
		Sets the ID of the employee.
		"""

		self.__id = value

	def get_department(self):
		"""
		Gets the department of the employee.
		"""

		return self.__department

	def set_department(value):
		"""
		Sets the department of the employee.
		"""

		self.__department = value

	def get_title(self):
		"""
		Gets the title of the employee."
		"""

		return self.__title

	def set_title(value):
		"""
		Sets the title of the employee.
		"""

		self.__title = value


	def print(self, column_width=15):
		"""
		Prints an employee's information to the screen.

		Information is fitted to columns 'column_width' wide.

		The order is the same as printed in print_columns.
		"""

		print(
			self.__name.ljust(column_width),
			str(self.__id).ljust(column_width),
			self.__department.ljust(column_width),
			self.__title.ljust(column_width))

	def print_columns(column_width=15):
		"""
		Prints the columns of the employee table.

		Information is fitted to columns 'column_width' wide.

		The order is (name, id, department, title).
		"""

		print(
			"Name".ljust(column_width),
			"ID Number".ljust(column_width),
			"Department".ljust(column_width),
			"Job Title".ljust(column_width))

