# dependencies
import os
import csv
# file path
budget_csv= os.path.join(".","Resources","budget_data.csv")
#lists for months, profit, and profit changes
total_months=[]
total_profit=[]
profit_change=[]
# Opening and reading CSV
with open(budget_csv) as budgetfile:
    budget_reader=csv.reader(budgetfile)
    #Skip header
    header=next(budget_reader)
    #Creating Lists of each column to perform functions
    for row in budget_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

#Getting Total Months (length of months)
totalmonths=len(total_months)
print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalmonths}")
# Getting Total Profits (sum of profits)
totalprofit=sum(total_profit)
print(f"Total: {totalprofit}")
# Loop through Total Profits to find monthly changes
for i in range(len(total_profit)-1):
    profit_change.append((total_profit[i+1])-total_profit[i])
#Average of Monthly Changes
averagechange=sum(profit_change)/len(profit_change)
print(f"Average Change: {averagechange}")
#Get Max and min of profit_change
maxincrease=max(profit_change)
minincrease=min(profit_change)
#Find indexes to get the month
#Have to add 1 because i+1 is the month that changes
maxmonth= profit_change.index(maxincrease)+1
minmonth=profit_change.index(minincrease)+1
print(f"Greatest Increase in Profits: {total_months[maxmonth]} (${maxincrease})")
print(f"Greatest Decrease in Profits: {total_months[minmonth]} (${minincrease})")

# Create path for output file
financialsummary= os.path.join(".","Analysis","FinancialAnalysis.txt")
with open(financialsummary,"w") as file:
    file.write("Financial Analysis \n")
    file.write("-----------------\n")
    file.write(f"Total Months: {totalmonths}\n")
    file.write(f"Total: ${totalprofit}\n")
    file.write(f"Average Change: ${averagechange}\n")
    file.write(f"Greatest Increase in Profits: {total_months[maxmonth]} (${maxincrease})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[minmonth]} (${minincrease})\n")