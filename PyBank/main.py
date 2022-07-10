# Importing Modules
import os
import csv

# Csv Path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read Csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        print(row)
        