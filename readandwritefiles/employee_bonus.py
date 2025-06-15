import csv

# open the employee_data.csv file in read mode
employees = open('employee_data.csv','r')

# create a csv object delimiter ',' tells the program how the columns are separated
employee_file = csv.reader(employees, delimiter=',')

# skip the first line in the csv file since it contains a header row
next(employee_file)

# using a for loop you can step through the file, one line at a time
for row in employee_file:
    # employee_data.csv has columns ID, Name, Age, Salary, HoursWorked, Productivity, Team, Bonus
    name = row[1]
    salary = float(row[3])
    bonus_rate = float(row[7])
    
    # bonus = salary * bonus rate
    bonus_amount = salary * bonus_rate
    
    # total pay  = salary + bonus
    total_pay = salary + bonus_amount
    
    # display employee details
    print('Name: {}'.format(name))
    print('Salary:  $ {:>10,.2f}'.format(salary))
    print('Bonus:   $ {:>10,.2f}'.format(bonus_amount))
    print('Pay:     $ {:>10,.2f}'.format(total_pay))
    
    # pause the program until a key is pressed
    input()

# close the file
employees.close()
