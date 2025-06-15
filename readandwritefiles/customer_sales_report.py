import csv

# open the sales.csv file in read mode
sales_file = open('sales.csv','r')

# create a csv object delimiter ',' tells the program how the columns are separated
sales_reader = csv.reader(sales_file, delimiter=',')

# skip the first line in the csv file since it contains a header row
next(sales_reader)

# create a dictionary to store customer totals
totals = {}

# using a for loop you can step through the file, one line at a time
for row in sales_reader:
    # sales.csv has columns: CustomerID, OrderDate, ShipDate, SubTotal, TaxAmt, Freight
    id = row[0]
    sub = float(row[3])
    tax = float(row[4])
    freight = float(row[5])
    
    # total for this order = subtotal + tax + freight
    order = sub + tax + freight
    
    # add to customer's running total
    if id in totals:
        totals[id] = totals[id] + order
    else:
        totals[id] = order

# close the sales file
sales_file.close()

# open new file for writing the sales report
report_file = open('salesreport.csv','w', newline='')
report_writer = csv.writer(report_file, delimiter=',')

# write the header for the new file
report_writer.writerow(['Customer ID', 'Total'])

# write each customer's total to the file
for id in totals:
    total = totals[id]
    report_writer.writerow([id, '{:.2f}'.format(total)])

# close the report file
report_file.close()
