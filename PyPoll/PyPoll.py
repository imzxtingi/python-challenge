# Import OS Module to allow for creation of path files across all OS 
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
filepath = os.path.join('Resources', 'election_data.txt')

# Create lists to store data
voter_id = []
county = []
candidate = []
new_candidate_list = []
candidate_name = 0
vote_stockham = 0
vote_degette = 0
vote_doane = 0

# Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add voter id list, county list, and candidate list
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        # Calculate total number of votes
        total_votes = len(voter_id)

        # Total number of votes for each candidate
        if row[2] == "Charles Casper Stockham":
            vote_stockham = vote_stockham + 1
        elif row[2] == "Diana DeGette":
            vote_degette = vote_degette + 1
        elif row[2] == "Raymon Anthony Doane":
            vote_doane = vote_doane + 1
   
# Calculate percentage of votes per candidate
    percent_stockham = round((vote_stockham / total_votes) * 100, 3) 
    percent_degette = round((vote_degette / total_votes) * 100, 3)  
    percent_doane = round((vote_doane / total_votes) * 100, 3) 
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {percent_stockham}% ({vote_stockham})")
print(f"Diana Degette: {percent_degette}% ({vote_degette})")
print(f"Raymon Anthony Doane: {percent_doane}% ({vote_doane})")
print("-------------------------")
print(f"Winner:")
print("-------------------------")

# Export results to text file
with open(filepath, "w") as results:
    results.write("Election Results\n")
    results.write("-------------------------\n")
    results.write(f"Total Votes: {total_votes}\n")
    results.write("-------------------------\n")
    results.write(f"Charles Casper Stockham: {percent_stockham}% ({vote_stockham})\n")
    results.write(f"Diana Degette: {percent_degette}% ({vote_degette})\n")
    results.write(f"Raymon Anthony Doane: {percent_doane}% ({vote_doane})\n")
    results.write("-------------------------\n")
    results.write(f"Winner:\n")
    results.write("-------------------------\n")
