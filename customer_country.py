import csv

file_obj = open('customers.csv', 'r')

csv_obj = csv.reader(file_obj)
outfile = open('customer_country.csv', 'w')

#skip the header
    #header = next(csv_obj)

next(csv_obj)
outfile.write(f"Full Name, Country\n")
count = 0 

for rec in csv_obj:
    first_name = rec[1]
    last_name = rec[2]
    country = rec[4]
    outfile.write(f'{first_name} {last_name}, {country}\n')
    count +=1

print(count)

outfile.close()
file_obj.close()