import csv

monthly_steps = {}

file_obj = open('steps.csv', 'r')

csv_obj = csv.reader(file_obj)

next(csv_obj)
outfile = open('avg_steps.py', 'w')

for row in csv_obj:
    month = int(row[0])
    steps = int(row[1])

average_steps_per_month = sum(monthly_steps[month]) / len(monthly_steps[month])

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June", 
    7: "July",
    8: "August",
    9: "September",
    10: "October", 
    11: "November",
    12: "December"
}

for month, avg_steps in average_steps_per_month():
        
    if month == 1:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 2:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 3:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 4:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 5:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 6:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 7:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 8:
        print(f"{month_name} - {average_steps_per_month:.2f}")
        
    elif month == 9:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 10:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    elif month == 11:
        print(f"{month_name} - {average_steps_per_month:.2f}")

    else:
        print(f"{month_name} - {average_steps_per_month:.2f}")