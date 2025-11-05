#Nikkshai Junior
#CIS261
#Lab: Course Project Phase 1
#Date: 10/27/2025

from torch import Value
from datetime import datetime

def get_date_range():
    while True:
        try:
            from_date = input("Enter From date (mm/dd/yyyy): ")
            to_date = input("Enter To date (mm/dd/yyyy): ")
            datetime.strptime(from_date, "%m/%d/%Y")
            datetime.strptime(to_date, "%m/%d/%Y")
            return from_date, to_date
        except Value:
            print("Invalid date format")

def read_employee_data():
    employees = []
    while True:
        print("\nEnter employee info: ")
        from_date, to_date = get_date_range()
        name = get_employee_name()
        if name.lower() == "end":
            break
        hours = get_hours_worked()
        rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter income rate: "))

        employees.append([from_date, to_date, name, hours, rate, tax_rate])
    return employees

def procedd_employees(employees):
    totals_dict = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
        }
    for emp in employees:
        from_date, to_date, name, hours, rate, tax_rate = emp
        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        display_employee_details(from_date, to_date, name, hours, rate, tax_rate, gross, tax, net)

        totals_dict["total_employees"] += 1
        totals_dict["total_hours"] += hours
        totals_dict["total_tax"] += tax
        totals_dict["total_net"] += net

    return totals_dict

def display_totals(totals_dict):
    print("\n ==== PayRoll =====")
    print(f"Total employees: {totals_dict['total_employees']}")
    print(f"Total hrs worked: {totals_dict['total_hours']:.2f}")
    print(f"Total income tax: {totals_dict['total_tax']:.2f}")
    print(f"Total net pay: {totals_dict['total_net']:.2f}")

def get_employee_name():
    employee_name = input("Please enter the employee's name: ")
    name = input('Enter employee name or "END" to terminate:')
    return name

def get_hours_worked():
    while True:
        
        try:

            hour = int (input("Enter hours worked: "))
            if hour >= 0: 
             rate_per_hour = 20.0
             total_pay = hour * rate_per_hour
             print(f"Total pay for {hour} hours worked is: ${total_pay:.2f}") # type: ignore
             return hour # type: ignore
            else:

             print("Hours worked cannot be negative. Please try again. ")

        except ValueError:
             print("Please enter a valid number. ")
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate # type: ignore
    tax = gross_pay * tax_rate
    net = gross_pay - tax

    return gross_pay, tax, net # type: ignore

def display_employee_details(from_date, to_date, name, hours, rate, tax_rate, gross, tax, net):
    print(f"From date: {from_date} ")
    print(f"TO date: {to_date} ")
    print(f"Employee Name: {name} ")
    print(f"Hourly Rate: {rate:.2f} ")
    print(f"Gross Pay: {gross:.2f} ")
    print(f"Net pay: {net:.2f} ")


def main():
    # Initialize variables for totals

    employees = read_employee_data()
    if len(employees) == 0:
        print("No employees dfound")
        return
    totals_dict = procedd_employees(employees)
    display_totals(totals_dict)

if __name__ == "__main__":
  main()