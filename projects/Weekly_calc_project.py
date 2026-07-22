print("Weekly Pay Calculator")

employee_name = input("What is your name? ")
hours_worked = float(input("How many hours did you work? "))
hourly_rate = float(input("What is your hourly pay rate? "))
regular_hours = 40

if  (hours_worked) > (regular_hours):
    overtime_hours = (hours_worked) - (regular_hours)
    regular_pay = (regular_hours) * (hourly_rate)
    overtime_pay = (overtime_hours) * (hourly_rate) * 1.5
    total_pay = (regular_pay) + (overtime_pay)
else:
    total_pay = (hours_worked) * (hourly_rate)

print(f"Employee: {employee_name}")
print(f"Hours worked: {hours_worked}")
print(f"Total pay: ${total_pay:.2f}")





#The important shortcuts are:
#Convert input once instead of repeatedly.
#Use float() for values that may contain decimals.
#Use f-strings instead of combining strings with +.
#Use :.2f to show money with two decimal places.

# i added float into lines 4 and 5 to be able to store them as numerical values when operator is to put them in, initially i had went and put int() on everything but that takes  too much time
# for future refrence just add float or int to the storage or op input oints int for flat nubmers and flaot for decimals 
# i also had to use f strings since i was mixing strings with floats 