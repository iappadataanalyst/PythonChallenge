# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#csvpath = os.path.join('..','Resources', 'budget_data.csv') 
csvpath = os.path.join('Resources', 'budget_data.csv') 
# Open the CSV

# Lists to store data
TotalMonths = []
TotalProfit = []
MonthlyChange =[]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header labels to iterate with the values
    header = next(csvreader)    
    csvreader = list(csvreader)
    
    # Loop through to go through the total months, profit
    for row in csvreader:
        # Add Months
        TotalMonths.append(row[0])

        # Add TotalProfit
        TotalProfit.append(int(row[1]))        
        
        # Determine change between months
    for row in range(0, len(csvreader)-1): 
        old_revenue = int(csvreader[row][1])
        new_revenue = int(csvreader[row+1][1])        
        MonthlyChange.append(new_revenue - old_revenue)
        AverageChange = round(sum(MonthlyChange)/len(MonthlyChange), 2)
#print(MonthlyChange)        

#GreatestIncrease, GreatestDecrease
GreatestIncrease = max(MonthlyChange)
GreatestDecrease  = min(MonthlyChange)       

#GreatestIncrease, GreatestDecrease months
GreatestIncreaseMonth_index = MonthlyChange.index(GreatestIncrease)+2
GreatestDecreaseMonth_index  = MonthlyChange.index(GreatestDecrease)+2

GreatestIncreaseMonth = csvreader[GreatestIncreaseMonth_index][0]
GreatestDecreaseMonth  = csvreader[GreatestDecreaseMonth_index][0]

#AverageChange = (sum(MonthlyChange)/len(MonthlyChange))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(TotalMonths)}")
print(f"Total: ${sum(TotalProfit)}")
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth}  (${GreatestIncrease})")
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth}  (${GreatestDecrease})")

#write to file
file = open("Resources/FinancialAnalysis.txt","w+")
file.write("Financial Analysis")
file.write('\n' +"----------------------------")
file.write('\n' +f"Total Months: {len(TotalMonths)}")
file.write('\n' +f"Total: ${sum(TotalProfit)}")
file.write('\n' +f"Average Change: ${AverageChange}")
file.write('\n' +f"Greatest Increase in Profits: {GreatestIncreaseMonth}  (${GreatestIncrease})")
file.write('\n' +f"Greatest Decrease in Profits: {GreatestDecreaseMonth}  (${GreatestDecrease})")
file.close() 