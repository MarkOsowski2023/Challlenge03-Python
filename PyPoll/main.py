# Importing Modules
from enum import unique
import os
import csv

from nbformat import write

# CSV Path
csv_path = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('output', "pypolltxtfile.txt")
# Define Variables
canidates = []
canidates_unique = []
vote_count = []
vote_percent = []
votes = 0.0


# Read CSV
with open(csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # Store Header
    header = next(csv_reader)

# Loop Through Rows
    for row in csv_reader:

        votes += 1

        canidates.append(row[2])
    # loop to collect data for each unique canidate x is canadate y is their votes z is their vote perctentage
    # using set because it will only store the value once, easy way to get the unique values    
    for x in set(canidates):
        
        canidates_unique.append(x)
        # y count each unique canadates total votes
        y = canidates.count(x)
        # append to vote count
        vote_count.append(y)
        # z calculate each canadates vote perctenage
        z = (y / votes)
        # append to vote percentage list 
        vote_percent.append(z)
    
    winning_votes_total = max(vote_count)
    election_winner = canidates_unique[vote_count.index(winning_votes_total)]

# print results
print("Election Results")
print("------------------------")
print(f"Total Votes: {votes}")
print("------------------------")
for i in range(len(set(canidates_unique))):
    print(f"{canidates_unique[i]} : {vote_percent[i]:.0%} ({vote_count[i]})")
print(f"Winner: {election_winner}")

with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("------------------------\n")
    output.write(f"Total Votes: {votes}\n")
    output.write("------------------------\n")
    for i in range(len(set(canidates_unique))):
        output.write(f"{canidates_unique[i]} : {vote_percent[i]:.0%} ({vote_count[i]})\n")
    output.write(f"Winner: {election_winner}\n")







