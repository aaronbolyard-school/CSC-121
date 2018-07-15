# Aaron Bolyard
# 2018-07-11
# Pet class definition.
# M5HW1

class Pet:
	__name = ""
	__type = ""
	__age = 0

	def __init__(self, name, type, age):
		self.set_name(name)
		self.set_animal_type(type)
		self.set_age(age)

	def get_name(self):
		"""
		Gets the pet's name.
		"""
		return self.__name

	def set_name(self, value):
		"""
		Sets the name of the pet.
		"""
		self.__name = value

	def get_animal_type(self):
		"""
		Gets the pet's type (species or breed).
		"""
		return self.__type

	def set_animal_type(self, value):
		"""
		Sets the pet's type.
		"""
		self.__type = value

	def get_age(self):
		"""
		Gets the age, in years, of the pet.
		"""
		return self.__age

	def set_age(self, value):
		"""
		Sets the age of the pet.

		The age should be greater than or equal to zero.
		"""
		if value <= 0:
			raise ValueError("Age must be greater than zero")

		self.__age = value
