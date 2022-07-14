# Importing Modules
from enum import unique
import os
import csv

# CSV Path
csv_path = os.path.join('Resources', 'election_data.csv')

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
    for x in set(canidates):
        
        canidates_unique.append(x)
        # y count each unique canadates total votes
        y = canidates.count(x)
        # append to vote count
        vote_count.append(y)
        # z calculate each canadates vote perctenage
        z = (y / votes) * 100
        # append to vote percentage list 
        vote_percent.append(z)
    
    winning_votes_total = max(vote_count)
    election_winner = canidates_unique[vote_count.index(winning_votes_total)]

print("Election Results")
print("------------------------")
print(f"Total Votes: {votes}")
print("------------------------")
for i in range(len(set(canidates_unique))):
    print(f"{canidates_unique[i]} : {vote_percent[i]} ({vote_count[i]})")
print(f"Winner: {election_winner}")





# Print Results
