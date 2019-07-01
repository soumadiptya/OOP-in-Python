# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:04:13 2019

@author: Soumadiptya.c
"""

class Employees:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        #self.email = self.fname + '.' + self.lname + '@' + 'gmail.com'
    
    @property
    def fullname(self):
        fullname = self.fname + ' ' + self.lname
        return fullname
    
    # Change email by making it a property
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last
    
    @fullname.deleter #- Gets run when you run del statement
    def fullname(self):
        print('Delete Name')
        self.fname = None
        self.lname = None
    
emp_1 = Employees('Soumadiptya', 'Chakraborty', 65000)
emp_2 = Employees('Vivek', 'Ananthan', 70000)
    
print(emp_1.fname)
print(emp_1.lname)
print(emp_1.email)
print(emp_1.fullname)    

# Change email
emp_1.fname = 'Anu'
print(emp_1.email)

# Set fullname
emp_1.fullname = 'Sam Winchester'
print(emp_1.fname, emp_1.lname, emp_1.fullname)

# Deletion
del emp_1.fullname
print(emp_1.__dict__)
print(emp_2.__dict__)