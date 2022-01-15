import os
import csv

#instructions
#The total number of months included in the dataset
    #add number of months from list
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

py_bank = os.path.join("Resources", "budget_data.csv")

#code from Dwight meeting with study group
with open(py_bank) as csvfile:      
    csvreader = csv.reader(csvfile, delimiter=",")      
    
    # Skip over the csv file header on the first row
    next(csvreader)      
    # # Pass the raw text data out as a list     
    csv_data = list(csvreader)          
    # for row in csv_data:
        # print(f"{row[0]:8}  {int(row[1]):14,.0f}")

    # for row in csv_data:
    months = [row[0] for row in csv_data]
    total_months = len(months)
    # print(total_months)

    # for row in csv_data:
    profit = [int(row[1]) for row in csv_data]
    sum_profit = sum(profit)
    # print(sum_profit)

    change_profitloss = [[profit[i] - profit [i-1], months[i]] for i in range(1, total_months)]
    # print(change_profitloss)

    average_change = [profit[i] - profit[i-1] for i in range(1, total_months)]
    # print(average_change)

    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum_profit}")
    print(f"Average Change: ${int(sum(average_change)/total_months)}")
    print(f"Greatest Increase in Profits: {max(change_profitloss)}")
    print(f"Greatest Decrease in Profits: {min(change_profitloss)}")

# https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python/48964410
# When writing a .txt file, use "x" if the file doesn't exist and use "w" if file exists and needs to be written/changed/appended
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines
# Use "\n" in the f.write string to move text to next line for better file viewing

# with open("Analysis/PyBank_Analysis.txt", "x") as f:
with open("Analysis/PyBank_Analysis.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("------------------\n")
    f.write(f"Total months: {total_months}\n")
    f.write(f"Total: ${sum_profit}\n")
    f.write(f"Average Change: ${int(sum(average_change)/total_months)}\n")
    f.write(f"Greatest Increase in Profits: {max(change_profitloss)}\n")
    f.write(f"Greatest Decrease in Profits: {min(change_profitloss)}\n")




# Example - Final Output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
