# Importing Modules
import os
import csv

# Csv Path
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('output', 'pybank.txt')

# Defining varibales
months = []
profit_loss = []
total_months = 0.0
total_profit_loss = 0.0
current_profit_loss = 0.0
last_month_profit_loss = 0.0
change = 0.0


   
# Read Csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Storing Header
    header = next(csv_reader)

    # Looping Through CSV File
    for row in csv_reader:
        
        total_months += 1 

        current_profit_loss = float(row[1])

        total_profit_loss += current_profit_loss

        if total_months == 1:

            last_month_profit_loss = current_profit_loss

        else:

            change = current_profit_loss - last_month_profit_loss

            months.append(row[0])

            profit_loss.append(change)

            last_month_profit_loss = current_profit_loss

    # finding sum and of all profits and loss and finding average change
    sum_profit_loss = sum(profit_loss)
    mean_profit_loss = round((sum_profit_loss / (total_months - 1)),2)

    # finding greatest increase and decrease
    greatest_increase = max(profit_loss)
    greatest_decrease = min(profit_loss)

    # get index for greatest increase and decrease
    index_greatest_increase = profit_loss.index(greatest_increase)
    index_greatest_decrease = profit_loss.index(greatest_decrease)

    greatest_increase_month = months[index_greatest_increase]
    greatest_decrease_month = months[index_greatest_decrease]

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit_loss}")
print(f"Average Change: {mean_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase:,.2f}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease:,.2f}")


with open(outpath, 'w') as output:
    output.write("Financial Analysis")
    output.write("----------------------")
    output.write(f"Total Months: {total_months}")
    output.write(f"Total: {total_profit_loss}")
    output.write(f"Average Change: {mean_profit_loss}")
    output.write(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase:,.2f}")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease:,.2f}")
    




        