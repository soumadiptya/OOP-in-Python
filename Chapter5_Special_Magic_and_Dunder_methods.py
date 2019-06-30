# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:56:09 2019
Special Magic and Dunder methods
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
        self.pay = int(self.pay * self.raise_amount)
       
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
    
    # Special dunder methods
    def __repr__(self):
        return "Employee('{}', '{}' , '{}')".format(self.fname, self.lname, self.pay) 
    
    def __str__(self):
        return "Employee('{}', '{}')".format(self.fullname(), self.email) 
    
    def __add__(self, other): # Add two Employees salarys together
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
# Define an employee
emp_1 = Employee('Soumadiptya', 'Chakraborty', 50000) 
emp_2 = Employee('Smriti', 'Sukul', 30000) 

print(emp_1)
print(emp_1 + emp_2)

# Example of a dunder method at work
print(len('test'))
print('test'.__len__())
print(len(emp_1))