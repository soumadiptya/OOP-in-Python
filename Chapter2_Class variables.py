# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 07:06:48 2019

@author: souma
"""

class Employee:   
    # Define class variables
    raise_amount = 1.04
    num_employees = 0
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@company.com'
        Employee.num_employees += 1
	# Class Methods
    def fullname(self):
        '''Returns the fullname of an employee'''
        fullname = self.fname + ' ' + self.lname
        return fullname
    
    def apply_raise(self):
        '''Adds a raise amount to the employees salary'''
        self.pay = int(self.pay * Employee.raise_amount)
       
# Define an employee
emp_1 = Employee('Soumadiptya', 'Chakraborty', 50000) 

print(emp_1.pay)

emp_1.apply_raise()
print(emp_1.pay)

# Print the namespace of class instances and the class itself
print(emp_1.__dict__)
print(Employee.__dict__)

# Changing class variables
Employee.raise_amount = 1.05 # This will glbally update the value of raise amount
print(Employee.raise_amount, emp_1.raise_amount)
emp_1.raise_amount = 1.06 # Only change sit for employee 1 and includes it in it's namespace
print(Employee.raise_amount, emp_1.raise_amount, emp_1.__dict__)

print(Employee.num_employees)