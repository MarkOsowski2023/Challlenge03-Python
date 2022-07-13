# Importing Modules
import os
import csv

# Csv Path
csvpath = os.path.join('Resources', 'budget_data.csv')

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

    header = next(csv_reader)

    
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

    sum_profit_loss = sum(profit_loss)
    mean_profit_loss = (sum_profit_loss / (total_months - 1))

    greatest_increase = max(profit_loss)
    greatest_decrease = min(profit_loss)

    index_greatest_increase = profit_loss.index(greatest_increase)
    index_greatest_decrease = profit_loss.index(greatest_decrease)

    greatest_increase_month = months[index_greatest_increase]
    greatest_decrease_month = months[index_greatest_decrease]

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: {sum_profit_loss}")
print(f"Average Change: {mean_profit_loss}")







        