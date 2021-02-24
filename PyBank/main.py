#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv

# Path to collect data from the Resources folder

budget_csv = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")
months = []
profit_loss = []


# Read CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)
    
    for row in csvreader:

        months.append(row[0])
        profit_loss.append(row[1])  
        #print(row)

        #capture date for max profit and max loss

        if row[1] == min(profit_loss):
            max_loss_date = row[0]
        
        

Total_months = len(months)
print(Total_months)

max_loss = min(profit_loss)
max_profit =max(profit_loss)

print(max_loss_date)
print(max_loss)
print(max_profit)
print(int(max_profit) - int(max_loss))

avg_change = (int(max_profit) - int(max_loss))/Total_months

print(round(avg_change,2))




# Set variable for output file
analysis_csv = os.path.join(os.path.dirname(__file__),"analysis","analysis_data.csv")
#  Open the output file
with open(analysis_csv, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------"])

    # Write in output rows
    #------




