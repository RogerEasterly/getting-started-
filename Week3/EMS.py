#!/usr/bin/env python

employee_count = 0
employee_list = []


def AddEmployee():
    employee = []
    employee.append(str(input('Enter employee name: ')))
    employee.append(str(input('Enter employee\'s social security number: ')))
    employee.append(str(input('Enter employee\'s phone number: ')))
    employee.append(str(input('Enter employee\'s email address: ')))
    employee.append(str(input('Enter employee\'s salary: ')))
    employee_list.append(employee)

def RemoveEmployee():
    pass

def ViewEmployees():
    for e in employee_list:
        print("{}, {}, {}, {}, ${}".format(e[0],e[1],e[2],e[3],e[4]))

def PrintStatus():
    print("Hi! Welcome to the Acme Employee Management System! There are currently " + str(len(employee_list)) + " employees in the system!")

while True:
    i = str(input("Enter: 1 to add an employee; 2 to view all employees; 3 to view the status of the system: ; 4 to exit "))
    print("You entered: " + i)
    if i == "1":
        AddEmployee()
    elif i == "2":
        ViewEmployees()
    elif i == "3":
        PrintStatus()
    elif i == "4":
        print("Goodbye!")
        exit()
