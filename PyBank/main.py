# imported csv module so that csv.reader function can be used in python to read an external csvfile

import csv 

# Opened excel budget_data_1 as a csvfile. 
# Csv.reader function iterates each line in csv file to a form rows as new lists in python called Budget_1
# Skip header of the Budget_1 List (Date and Revenue)

with open ('budget_data_1.csv') as csvfile:
    Budget_1=csv.reader(csvfile , delimiter=",")
    next(Budget_1)

#Created empty List 
    Months=[]
    Revenue=[]
    Revenue_Change=[]

#Iterate through every row in Budget_1 List to display the comma seperated values in print as lists
#Everytime goes through a row which is a list, collects the first string (0 index) which is the Date
#Puts each iterated month in the for loop in the empty array of Months, created above 
#Repeats for Revenue, in addition to turning every string number in Revenue List into integer numbers in new Revenue List
    for row in Budget_1:
        Months.append(row[0])
        Revenue.append(row[1])

Revenue_Integers=[int(i) for i in Revenue]

for i in range(1,len(Revenue_Integers)):
    Difference=Revenue_Integers[i]-Revenue_Integers[i-1]
    Revenue_Change.append(Difference)

Average_Change_Revenue=sum(Revenue_Change)/len(Revenue_Change)

a=(Revenue_Change.index(max(Revenue_Change)) + 1 )
b=(Revenue_Change.index(min(Revenue_Change)) + 1 )

print("Financial Analysis")
print("------------------")
print("Total Months: ", int(len(Months)))
print("Total Revenue: $", sum(Revenue_Integers))
print("Average Revenue Change: $", int(Average_Change_Revenue))

print("Greatest Increase in Revenue: ", Months[a], Revenue_Integers[a])
print("Greatest Decrease in Revenue: ", Months[b], Revenue_Integers[b])