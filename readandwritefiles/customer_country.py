import csv

# open the customers.csv file in read mode
customers = open('customers.csv','r')

# create a csv object delimiter ',' tells the program how the columns are separated
customer_file = csv.reader(customers, delimiter=',')

# skip the first line in the csv file since it contains a header record
next(customer_file)

# open new file for writing
result_file = open('customer_country.csv','w', newline='')
op_write = csv.writer(result_file, delimiter=',')

# write the header for the new file
op_write.writerow(['Customer Name', 'Country'])


# using a for loop you can step through the file, one line at a time
for record in customer_file:
    # full customer name = first name + last name
    first_name = record[1]
    last_name = record[2]
    full_name = first_name + ' ' + last_name
    country = record[4]
    
    # write the customer name and country to the new file
    op_write.writerow([full_name, country])

# close both files
customers.close()
result_file.close()

