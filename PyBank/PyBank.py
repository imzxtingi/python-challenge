# Import OS Module to allow for creation of path files across all OS 
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
month_list = []
profit_loss = []

# Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
# Append month list and profit/loss list
    for row in csvreader:
        month_list.append(row[0])
        profit_loss.append(int(row[1]))
 
# Calculate total number of months and net total profits
        total_month = len(month_list)
        net_total_profit = sum(profit_loss)

# Calculate changes in profit/losses over entire period
        #profit_change = int(row[1]) - prev_row
        #if prev_row == 0:
         #   profit_change = 0
        #prev_row = int(row[1])
        #total_profit_change = total_profit_change + profit_change
profit_change = [x - y for x, y in zip(profit_loss[1:], profit_loss[:len(profit_loss)-1])]
sum_profit_change = sum(profit_change)
average_profit_change = sum_profit_change / len(profit_change)
#print(average_profit_change)

# Zip month list and profit change list together
# Starting month Jan has 0 profit change
start_profitchange = 0
profit_change.insert(0, start_profitchange)
month_profit_list = zip(month_list, profit_change)

greatest = max(list(zip(month_list,profit_change)))
print(greatest)
# Look for index with greatest profit change


            
#print("Financial Analysis")
#print("-----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${(net_total_profit)}")
#print(f"Average Change: ${(average_final)}")
