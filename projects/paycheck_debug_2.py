print("Employee Paycheck Calculator")

employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: $"))
tax_rate = float(input("Enter tax percentage: "))

regular_hours = 40
overtime_multiplier = 1.5

if hours_worked > regular_hours:
    actual_regular_hours = regular_hours
    overtime_hours = hours_worked - regular_hours
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * (hourly_rate * overtime_multiplier)
else: 
    actual_regular_hours = hours_worked
    overtime_hours = 0
    regular_pay = actual_regular_hours * hourly_rate
    overtime_pay = 0
    regular_pay = hours_worked * hourly_rate
    overtime_hours = 0
    overtime_pay = 0

gross_pay = regular_pay + overtime_pay
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount


print("\n--- PAYCHECK SUMMARY ---")
print(f"Employee: {employee_name}")
print(f"Regular hours: {actual_regular_hours}")
print(f"Overtime hours: {overtime_hours}")
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Taxes withheld: ${tax_amount:.2f}")
print(f"Net pay: ${net_pay:.2f}")