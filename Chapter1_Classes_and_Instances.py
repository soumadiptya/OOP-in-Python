# Python Object Oriented programming

class Employee:
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = self.fname + '.' + self.lname + '@company.com'

	# Class Methods
	def fullname(self):
		'''Returns the fullname of an employee'''
		fullname = self.fname + ' ' + self.lname
		return fullname

# Create an instance of the class
emp_1 = Employee('Soumadiptya', 'Chakraborty', 50000) 

# Print results
print(emp_1.fname, emp_1.email)
print(emp_1.lname)

# Using methods
print(emp_1.fullname())

# Let's see help
help(Employee.fullname)

# self is always passed to all class methods automatically so it must be used as an argument
# Another way to run class methods is to use the class name and pass the instance as an argument
print(Employee.fullname(emp_1))