# Import OS Module to allow for creation of path files across all OS 
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
filepath = os.path.join('Resources', 'budget_data.txt')

# Lists to store data
month_list = []
profit_loss = []
profit_change_list = []
previous_row = 0

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

# Calculate changes in profits & losses over each month and the months with the greatest increase and decrease
        profit_change = (int(row[1])) - previous_row
        if previous_row == 0:
            profit_change = 0
        previous_row = (int(row[1]))
        profit_change_list.append(profit_change)
        if profit_change == max(profit_change_list):
            inc_month = row[0]
        if profit_change == min(profit_change_list):
            dec_month = row[0]

# Calculate average change of profit/losses
average_change = sum(profit_change_list) / (len(profit_change_list) - 1)
final_average = round(average_change, 2)

#Find the greatest increase/decrease in profits
great_inc = max(profit_change_list)
great_dec = min(profit_change_list)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${(net_total_profit)}")
print(f"Average Change: ${(final_average)}")
print(f"Greatest Increase in Profits: {inc_month} (${great_inc})")
print(f"Greatest Decrease in Profits: {dec_month} (${great_dec})")

# Export results to text file
with open(filepath, "w") as results:
    results.write("Financial Analysis\n")
    results.write("-------------------------\n")
    results.write(f"Total Months: {total_month}\n")
    results.write(f"Total: ${(net_total_profit)}\n")
    results.write(f"Average Change: ${(final_average)}\n")
    results.write(f"Greatest Increase in Profits: {inc_month} (${great_inc})\n")
    results.write(f"Greatest Decrease in Profits: {dec_month} (${great_dec})\n")
