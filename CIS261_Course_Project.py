#Nikkshai Junior
#CIS261
#Lab: Course Project Phase 1
#Date: 10/27/2025

def get_employee_name():
    employee_name = input("Please enter the employee's name: ")
    name = input('Enter employee name or "END" to terminate):')
    return name

def get_hours_worked():
    while True:
        try:

            hours = float(input("Enter hours worked:"))
            if hours >= 0: 
             rate_per_hour = 20.0
             total_pay = hours * rate_per_hour
             print(f"Total pay for {hours} hours worked is: ${total_pay:.2f}")
             return hours
           else:
            print("Hours worked cannot be negative. Please try again. ")
        except ValueError:
            print("Please enter a valid number. ")
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * pay_rate
    tax = gross_pay * tax_rate
    net = gross_pay - tax
    employee_details
    return employee_details
def display_employee_details(name, hours, pay_rate, tax_rate, employee_details):
    print(f"The employee name is {name}. ")
    print(f"The hours worked is {hours}. ")
    print(f"The employee's tax rate is {tax_rate}. ")
    print(f"The employee's pay rate is {pay_rate}. ")
    print(f"The employee's gross pay is {employee_details[0]. ")
    print(f"The empoyee's tax is {employee_details{1}. ")
    print(f"The employee's net pay is {employee_details{2}. ")
def totals(employees, total_hours, hours, total_gross, total_tax,total_net, employee_details. ")
        employee += 1
        total_hours += hours
        total_gross += employee_details[0]
        total_tax += employee_details[1]
        total_net += employee_details[2]
        return employee, total_hours, total_gross, total_tax, total_net
def main():
    # Initialize variables for totals

    #Start the main loop
    while True:
        # Get employee information by calling your functions
        employee_name =get_employee_name()

        # Check if user wants to end the program
        if employee_name.lower() == "end":
            break

        #Continue getting other information and perform calculations

        # Display information and perform calculations

        #Update totals

  # After loop ends, display totals
    # This will be our main function where we'll set up our loop
    # and call other functions
    pass

if_name_ == "_main_-:
  main()