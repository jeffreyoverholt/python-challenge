import os
import csv

# The total number of votes cast
    # Length of first column
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

py_poll = os.path.join("Resources", "election_data.csv")

#code from Dwight meeting with study group
with open(py_poll) as csvfile:      
    csvreader = csv.reader(csvfile, delimiter=",")  

    # Skip over the csv file header on the first row
    next(csvreader)      
    # # Pass the raw text data out as a list     
    csv_data = list(csvreader)          
    # for row in csv_data:
        # print(f"{row[0]:8}  {int(row[1]):14,.0f}")

    #  for row in csv_data

    # votes = [row[0] for row in csv_data]
    # County = [row[1] for row in csv_data]
    # candidates = [row[2] for row in csv_data]

    # The total number of votes cast
    votes = [row[0] for row in csv_data]
    total_votes = len(votes)
    print(total_votes)
    
    # A complete list of candidates who received votes
    candidates = [row[2] for row in csv_data]

    # {"candidate": 0, "candidate2": 1, "Candidate3": 2}
    set_candidates = set(candidates)
    # [list_candidates.append(i) for i in candidates if i not in list_candidates]
    # print(set_candidates)
    # print(len(list_candidates))

    #Feedback and direction from Mohamad the TA
    vote_book = {x : 0 for x in set_candidates}
    for candidate in candidates :
        vote_book[candidate] = vote_book[candidate] + 1
        # vote_book[candidate]["Votes"] = vote_book[candidate]["votes"] + 1
    
    win_candidate = 0
    winner_votes = 0
    # (key, value)
    for [candidate, votes] in vote_book.items():
        if votes > winner_votes:
            win_candidate = candidate
            winner_votes = votes
    print()


    # The total number of votes each candidate won
    
    count = 0

            




# Sample Output 
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# ------------------------
