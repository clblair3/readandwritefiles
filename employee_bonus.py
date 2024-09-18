import csv

file_obj = open("employee_data.csv", "r")

csv_obj = csv.reader(file_obj)

next(csv_obj)
outfile = open("employee_bonus.py", "w")

for object in csv_obj:
    first_name = object[1]
    salary = object[3]
    bonus = int(object[3]) * float(object[7])
    pay = int(bonus) + int(salary)
    print(f"Name: {first_name}\nSalary: $  {int(salary):,.2f}\nBonus:  $   {int(bonus):,.2f}\nPay:    $  {int(pay):,.2f}\n")


file_obj.close()