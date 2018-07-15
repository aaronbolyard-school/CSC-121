# Aaron Bolyard
# 2018-07-15
# Car class.
# M5HW2_Car

class Car:
	"""
	Represents a car.
	"""

	def __init__(self, yearModel, make):
		"""
		Constructs a stopped car (get_speed() will return 0).

		See get_year_model and get_make for semantics of the parameters.
		"""
		self.__year_model = yearModel
		self.__make = make
		self.__speed = 0

	def get_year_model(self, ):
		"""
		Gets the year-model (e.g., 2007 Accord).
		"""
		return self.__year_model

	def get_make(self, ):
		"""
		Gets the make (e.g., Honda).
		"""
		return self.__make

	def accelerate(self, value=5):
		"""
		Accelerates the car by 'value'. Defaults to 5.
		"""
		if value > 0:
			self.__speed += value

	def brake(self, value=5):
		"""
		Brakes, slowing the car by 'value'. Defaults to 5.
		"""

		self.__speed -= value
		if self.__speed < 0:
			self.__speed = 0

	def get_speed(self, ):
		"""
		Returns the speed of the car.
		"""
		return self.__speed
