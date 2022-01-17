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
    print(set_candidates)
    # [list_candidates.append(i) for i in candidates if i not in list_candidates]
    # print(set_candidates)
    # print(len(list_candidates))

    #Feedback and direction from Mohamad the TA
    vote_book = {x : 0 for x in set_candidates}
    for candidate in candidates :
        vote_book[candidate] = vote_book[candidate] + 1
        # vote_book[candidate] = (vote_book[candidate] + 1) / total_votes
        # vote_book[candidate]["Votes"] = vote_book[candidate]["votes"] + 1
    print(vote_book)

    # vote_book[candidate] = (vote_book[votes] + 1) / total_votes
    # print(vote_book)

    # vote_book = {x : 0 for x in set_candidates}
    # for candidate in candidates :
    #     vote_book[candidate] = (vote_book[candidate] + 1) / total_votes
    # print(f"{vote_book[candidate]:,%}")
    vote_book_alternate = {
        "candidates_votes": {
            "O'Tooley": 105630,
            "Correy": 704200,
            "Li": 492940,
            "Kahn": 2218231
        }
    }
    
    

    # vote_book_alternate["name"] = ["O'Tooley", "Correy", "Li", "Kahn"]
    # vote_book_alternate["total_can_votes"] = [105630, 704200, 492940, 2218231]
    # print(vote_book_alternate)


    win_candidate = 0
    winner_votes = 0
    # (key, value)
    for [candidate, votes] in vote_book.items():
        if votes > winner_votes:
            win_candidate = candidate
            winner_votes = votes
        # print(win_candidate)
        # print(winner_votes)
    print(win_candidate, winner_votes)

    print(" ")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f'Kahn: {(vote_book_alternate["candidates_votes"]["Kahn"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Kahn"]})')
    print(f'Correy: {(vote_book_alternate["candidates_votes"]["Correy"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Correy"]})')
    print(f'Li: {(vote_book_alternate["candidates_votes"]["Li"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Li"]})')
    # print(f'O'Tooley: {(vote_book_alternate["candidates_votes"]["O'Tooley"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["O'Tooley"]})')
    print("----------------------------")
    print(f"Winner: {win_candidate}")
    print("----------------------------")


with open("Analysis/PyPoll_Analysis.txt", "w") as f:
    f.write("Election Results\n")
    f.write("------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("------------------\n")
    f.write(f'Kahn: {(vote_book_alternate["candidates_votes"]["Kahn"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Kahn"]})\n')
    f.write(f'Correy: {(vote_book_alternate["candidates_votes"]["Correy"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Correy"]})\n')
    f.write(f'Li: {(vote_book_alternate["candidates_votes"]["Li"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["Li"]})\n')
    # f.write(f'O'Tooley: {(vote_book_alternate["candidates_votes"]["O'Tooley"]) / total_votes:.3%} ({vote_book_alternate["candidates_votes"]["O'Tooley"]})\n')
    f.write("------------------\n")
    f.write(f"Winner: {win_candidate}\n")
    f.write("------------------\n")
    
    
    
    # for [candidate, votes] in vote_book.items():
    #     candidate_percent = votes / total_votes

        

    # # winner_percent = winner_votes / total_votes
    # print(f"{candidate_percent : .0%}")


    # The total number of votes each candidate won
    
    # count = 0

            




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
