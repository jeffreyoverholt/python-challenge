#import csv file
from ipaddress import summarize_address_range
import os
import csv

#instructions
#The total number of months included in the dataset
    #add number of months from list
#The net total amount of "Profit/Losses" over the entire period
    #add profits, add loss
    #total profit = prfits-loss
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period



#build path for csv
#referenced in class python activities 2 module 8
csvpath = os.path.join("Resources", "budget_data.csv")
#print(csvpath)

# #define variables from csv
months_total = []
profit_loss = []

with open(csvpath, encoding='utf-8') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    #csvdata = list(csvreader)
    for row in csvreader:
         #print(row)

#Add the total number of months (row 0 of the csv)
#referenced Python activity 1 module 9 
        months_total.append(row[0])
        profit_loss.append(int(row[1]))
        # print(profit_loss)
    #print(len(months_total))
        
    # print(int(row[1]))
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {len(months_total)}")
    
    #total not matching homework
    profit_sum = sum(profit_loss)
#     x = 0
#     for x in profit_loss:
#         sum = sum + x
# #     print(int(row[1]))
# # print(sum)

    print(f"Total : {profit_sum}")

#referenced Python activity 3 module 7
#not quite right - need to figure out change between months then average
    average_sum = profit_sum / len(profit_loss)
    # def average(nums):
    #     sum = 0
    #     for x in nums:
    #         sum = sum + x
    #         print(sum)
    #     avg = sum / len(profit_loss)
    #     return avg
        
    print(f"Average Change: {average_sum}")