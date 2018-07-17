# Aaron Bolyard
# 2018-07-16
# Handles employee information.
# M6HW1_AaronBolyard

import M6HW1_Employee_AaronBolyard as Employee
import M6HW1_Input_AaronBolyard as ConsoleInput

def main():
	employee_name = ConsoleInput.get_string("Enter the employee name:")
	employee_name = ConsoleInput.prettify_name(employee_name)
	employee_id = ConsoleInput.get_integer("Enter the employee ID:", lambda x: x > 0)
	employee_shift = ConsoleInput.get_string("Enter the shift ('d' for day or 'n' for night):", lambda x: x.lower() == "d" or x.lower() == "n")
	employee_pay = ConsoleInput.get_float("Enter the employee pay:", lambda x: x >= 0)

	worker = Employee.ProductionWorker()
	worker.set_name(employee_name)
	worker.set_number(employee_id)
	if employee_shift.lower() == "d":
		worker.set_shift(Employee.ProductionWorker.DAY_SHIFT)
	else:
		worker.set_shift(Employee.ProductionWorker.NIGHT_SHIFT)
	worker.set_pay(employee_pay)

	print("Employee name:", worker.get_name())
	print("Employee ID:", worker.get_number())
	if worker.get_shift() == Employee.ProductionWorker.DAY_SHIFT:
		print("Employee shift:", worker.get_shift(), "(day)")
	else:
		print("Employee shift:", worker.get_shift(), "(night)")
	print("Employee pay:", "$" + format(worker.get_pay(), ".02f"))

if __name__ == "__main__":
	main()
