# Aaron Bolyard
# 2018-07-15
# Employee class usage.
# M5HW3

from M5HW3_Employee_AaronBolyard import Employee

def main():
	employees = [
		Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
		Employee("Mark Jones", 39199, "IT", "Programmer"),
		Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
	]

	Employee.print_columns()
	for employee in employees:
		employee.print()

if __name__ == "__main__":
	main()
