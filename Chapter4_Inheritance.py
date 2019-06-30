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

# Creating different types of Employees- Developer and Manager
class Developer(Employee):
    raise_amount = 1.10
    
    # Custom init
    def __init__(self,fname, lname,pay,primary_lang):
        super().__init__(fname, lname, pay)
        self.primary_lang = primary_lang
    
# Define an employee
emp_1 = Employee('Soumadiptya', 'Chakraborty', 50000) 
emp_2 = Employee('Smriti', 'Sukul', 30000) 

print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)

Employee.set_raise(1.05)
print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)

print(emp_1.__dict__)

# Developers
dev_1 = Developer('Vivek', 'Ananthan', 65000, 'C++')
dev_2 = Developer('Soumadiptya', 'Chakraborty', 60000, 'R')
print(dev_1.fname, dev_1.lname, dev_1.email)

# Changing raise amount
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(Developer.raise_amount)

# Creating a Manager class
class Manager(Employee):
    raise_amount = 1.2
    
    def __init__(self, fname, lname, pay, employees_supervised = None):
        super().__init__(fname, lname, pay)
        if employees_supervised == None:
            self.employees_supervised = []
        else:
            self.employees_supervised = employees_supervised
        
    def add_employees(self, emp):
        if emp not in self.employees_supervised:
            self.employees_supervised.append(emp)
    
    def remove_employees(self, emp):
        if emp in self.employees_supervised:
            self.employees_supervised.remove(emp)
    
    def print_employees(self):
        for emp in self.employees_supervised:
            print('-->', emp.fullname())
    
Manager_1 = Manager('Srinivasan', 'Govindaraj', 200000, [dev_1, dev_2])

print(Manager_1.print_employees())

# Add an employee
dev_3 = Developer('Pooja', 'Tight Pussy Jambaladinni', 50000, 'Python')
Manager_1.add_employees(dev_3)
Manager_1.print_employees()

# Some misc methods
print(isinstance(Manager_1, Manager)) # Will show true for the base class and the parent class

print(issubclass(Developer, Employee)) # Self explanatory