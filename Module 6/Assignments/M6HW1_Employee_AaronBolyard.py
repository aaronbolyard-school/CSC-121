# Aaron Bolyard
# 2018-07-16
# Employee classes.
# M6HW1_AaronBolyard

class Employee:
	def __init__(self, name="John Doe", number=0):
		self.__name = name
		self.__number = number

	def set_name(self, value):
		"""
		Sets the name of the employee.
		"""

		self.__name = value

	def get_name(self):
		"""
		Gets the name of the employee.
		"""

		return self.__name

	def set_number(self, value):
		"""
		Sets the number of the employee.
		"""

		self.__number = value

	def get_number(self):
		"""
		Gets the number of the employee.
		"""

		return self.__number

class ProductionWorker(Employee):
	DAY_SHIFT   = 1
	NIGHT_SHIFT = 2

	def __init__(self):
		Employee.__init__(self)
		self.__shift = 1
		self.__pay = 7.25

	def set_shift(self, value):
		"""
		Sets the number of the employee.
		"""

		self.__shift = value

	def get_shift(self):
		"""
		Gets the shift of the employee.
		"""

		return self.__shift

	def set_pay(self, value):
		"""
		Sets the number of the employee.
		"""
		self.__pay = value

	def get_pay(self):
		"""
		Gets the pay of the employee.
		"""

		return self.__pay
