import os
import csv

employee_count = 0
employee_list = []

def AddEmployee():
    employee = []
    employee.append(str(input("Enter employee name: ")))
    employee.append(str(input("Enter employee\'s social security number: ")))
    employee.append(str(input("Enter employee\'s phone number: ")))
    employee.append(str(input("Enter employee\'s email address: ")))
    employee.append(str(input("Enter employee\'s salary: ")))
    employee_list.append(employee)

def RemoveEmployee():
    pass

def LoadState(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            employee_list.append(row)

def DumpState(file_path):
    writer = csv.writer(open(file_path,'w'), lineterminator='\n')
    for e in employee_list:
        writer.writerow(e)

def ViewAllEmployees():
    for e in employee_list:
        print("{}, {}, {}, {}, ${}".format(e[0],e[1],e[2],e[3],e[4]))

def ViewEmployee(e):
    print("{}, {}, {}, {}, ${}".format(e[0],e[1],e[2],e[3],e[4]))

def PrintStatus():
    print("Hi! Welcome to The Management System! There are currently " \
          + str(len(employee_list)) + " employees in the system!")

def SearchEmployees():
    i = int(input("Enter: 1 to search by name, 2 to search by SSN, 3 to search by phone #, or 4 to search by email address ")) - 1

    if i == 0:
        d = str(input("Enter name: "))
    elif i == 1:
        d = str(input("Enter SSN: "))
    elif i == 2:
        d = str(input("Enter phone #: "))
    elif i == 3:
        d = str(input("Enter email address: "))
 
    for e in employee_list:
        if e[i] == d:
            ViewEmployee(e)

try:
    LoadState("state")
except IOError:
    pass

while True:
    i = str(input("Enter: 1 to add an employee: 2 to view all employees: 3 to view the status of the system: 4 to search employees:  5 to exit "))

    if i == "1":
        AddEmployee()
    elif i == "2":
        ViewAllEmployees()
    elif i == "3":
        PrintStatus()
    elif i == "4":
        SearchEmployees()
    elif i == "5":
        print("Saving current list.")
        DumpState("state")
        print("Goodbye!")
        exit()
