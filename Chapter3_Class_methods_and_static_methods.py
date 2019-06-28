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
       
    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last,pay = emp_str.split('-')
        cls = Employee(first, last,pay)
        return cls
        
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
# Define an employee
emp_1 = Employee('Soumadiptya', 'Chakraborty', 50000) 
emp_2 = Employee('Smriti', 'Sukul', 30000) 

print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)

Employee.set_raise(1.05)
print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)

print(emp_1.__dict__)

# Class methods as constructors
emp_str1 = 'John-Doe-50000'
emp_str2 = 'Steve-Smith-60000'
emp_str1 = 'Jane-Doe-40000'

first, last,pay = emp_str1.split('-')

emp_3 = Employee(first, last, pay)
print(emp_3.fname, emp_3.lname, emp_3.email)

emp_4 = Employee.from_string(emp_str2)
print(emp_4.fname, emp_4.lname, emp_4.email)

# Check static method
import datetime
my_date = datetime.date(2019, 12, 26)

print(Employee.is_workday(my_date))