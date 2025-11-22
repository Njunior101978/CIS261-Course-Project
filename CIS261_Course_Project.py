#Nikkshai Junior
#CIS261
#Lab: Course Project Phase 1
#Date: 11/22/2025

from datetime import datetime

EMPLOYEE_FILE = "employees.txt"


def get_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            datetime.strptime(date_str, "%m/%d/%Y")
            return date_str
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy")


def validate_date_or_all(date_str):
    if date_str.lower() == "all":
        return True
    try:
        datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value must be positive.")
        except ValueError:
            print("Invalid number format.")


def write_employee_to_file(from_date, to_date, name, hours, rate, tax_rate):
    with open(EMPLOYEE_FILE, 'a') as file:
        file.write(f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n")


def collect_employee_data():
    print("\n--- EMPLOYEE DATA ENTRY ---")
    while True:
        print("\nEnter employee information:")
        from_date = get_date("Enter From date (mm/dd/yyyy): ")
        to_date = get_date("Enter To date (mm/dd/yyyy): ")
        name = input('Enter employee name or "END" to terminate: ')
        
        if name.lower() == "end":
            break
        
        hours = get_positive_float("Enter hours worked: ")
        rate = get_positive_float("Enter hourly rate: ")
        tax_rate = get_positive_float("Enter income tax rate (e.g., 0.15 for 15%): ")
        
        write_employee_to_file(from_date, to_date, name, hours, rate, tax_rate)
        print(f"{name} added successfully.")


def get_report_date():
    while True:
        report_date = input('\nEnter From Date for report (mm/dd/yyyy) or "All": ')
        if validate_date_or_all(report_date):
            return report_date
        print("Invalid format. Please enter mm/dd/yyyy or 'All'")


def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay


def display_employee_report(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    print(f"\nFrom Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Employee Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")


def generate_report():
    print("\n--- PAYROLL REPORT ---")
    report_date = get_report_date()
    
    totals = {
        "employees": 0,
        "hours": 0.0,
        "gross": 0.0,
        "tax": 0.0,
        "net": 0.0
    }
    
    try:
        with open(EMPLOYEE_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                from_date, to_date, name, hours, rate, tax_rate = line.split('|')
                
                if report_date.lower() == "all" or from_date == report_date:
                    hours = float(hours)
                    rate = float(rate)
                    tax_rate = float(tax_rate)
                    
                    gross, tax, net = calculate_pay(hours, rate, tax_rate)
                    display_employee_report(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net)
                    
                    totals["employees"] += 1
                    totals["hours"] += hours
                    totals["gross"] += gross
                    totals["tax"] += tax
                    totals["net"] += net
        
        if totals["employees"] > 0:
            print("\n" + "="*50)
            print("TOTALS")
            print("="*50)
            print(f"Total Employees: {totals['employees']}")
            print(f"Total Hours: {totals['hours']:.2f}")
            print(f"Total Gross Pay: ${totals['gross']:.2f}")
            print(f"Total Income Tax: ${totals['tax']:.2f}")
            print(f"Total Net Pay: ${totals['net']:.2f}")
        else:
            print("\nNo employees found for the specified date.")
    
    except FileNotFoundError:
        print("No employee data found. Please enter employee data first.")


def display_menu():
    print("\n" + "="*50)
    print("PAYROLL SYSTEM")
    print("="*50)
    print("1. Enter Employee Data")
    print("2. Generate Payroll Report")
    print("3. Exit")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            collect_employee_data()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
