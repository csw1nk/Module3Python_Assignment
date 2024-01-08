import csv #this is a reuired library in python that will help us write code to pull read and write csv files

# defining file is located the resources folder and using the file budget_data.csv
csvfile = 'Resources/budget_data.csv'

# this is where the library comes in - we will open the csv file and read it with 'r' not using any encoding here but we can if needed usually utf-6
with open(csvfile, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #there is a header row on csv so we need to call the script to skip the header, next does this in the csv library
    data = list(csv_reader) #then we initialize a list of the data with the name 'data'
#references in class

# print(data[:5]) #used this function to make sure i was able to read the script, reference for this in class and further research here: https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-16.php

# Now we need to define our functions for each calculation to call these into a csv file later
total_months = len(data) #using len - in class - means length of list - in this case the list is data and we are getting the entire length of the data set, with months being column A
total_profit_losses = sum(int(row[1]) for row in data) #using a sum function we are adding together the entire rows of [1] which is the second column [0] is the first. then for row in data part is the looping that iterates over each value in the list. 
monthly_changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))] #again we are using index [1] - then "for" each month, we subtract the previous months value - range in (1,len(data)) is saying we start at the second month - had to test this one out, need the 1 there due to the change from previous month
average_change = sum(monthly_changes) / len(monthly_changes) #love a good average function taking the sum of the monthly changes then divide by the length of the data set
greatest_increase = max(monthly_changes) #max is the function for finding the value in monthly changes that was the max incease from month to month
greatest_decrease = min(monthly_changes) #similarily min is the function for finding the lowest value that occured in the monthly changes
greatest_increase_month = data[monthly_changes.index(greatest_increase) + 1][0] #this one was tricky used this reference: https://www.programiz.com/python-programming/methods/list/index - using data[] to access a value from the list - used index to find in the list monthly changes where the greatest increase happened, need to add one similarily to the script above
greatest_decrease_month = data[monthly_changes.index(greatest_decrease) + 1][0] #same as above but switched for decrease

#Printing out the results, this is straightfoward using the print function and seeing line by line our function, we could create an object that is the analysis analysis and call it out as well but this is good for now
#matching output in msubootcamp login
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")#need to use f here to call an object into the print reference in class
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}") #refernce for .2f - http://programarcadegames.com/index.php?chapter=formatting&lang=en
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#creating the file in folder analysis and creating headers and dropping the data into the file - refernce in class
outputcsv_file = 'analysis/financial_analysis.csv'
headers = ["Metric", "Value"]
data = [ #reference in class census example
    ["Total Months", total_months],
    ["Total", f"${total_profit_losses}"],
    ["Average Change", f"${average_change:.2f}"],
    ["Greatest Increase in Profits", f"{greatest_increase_month} (${greatest_increase})"],
    ["Greatest Decrease in Profits", f"{greatest_decrease_month} (${greatest_decrease})"]
]
#using csv library to write the data out
with open(outputcsv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data:
        writer.writerow(row)