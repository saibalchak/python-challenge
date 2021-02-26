#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv
import statistics

# Path to collect data from the Resources folder

budget_csv = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")

# Read CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)

    i = 0 
    budget_list = []
    
    for row in csvreader:
        
        budget_list.append(row)
        #print(row)

        #capture date for max profit and max loss

        total_amt = 0
        month_names = []
        month_budget = []
        month_budget_var = []
        variance_list = []

    for x, res in enumerate(budget_list): 

        #print (x,":",res[0], int(res[1]))
        total_amt =round(int(res[1]) + total_amt,2)
        month_names.append(res[0])
        month_budget.append(int(res[1]))
        #print(isinstance(res[1], int))

        

    for i in range(x+1):
        if i == 0:
            month_budget_var.append(0)
            #print(f"The i value is {i}", int(month_budget[i]), 0, 0) 
        else:
            #print(f"The i value is {i}", int(month_budget[i]) , int(month_budget[i-1]),  int(month_budget[i]) - int(month_budget[i-1])  )
            month_budget_var.append(int(month_budget[i]) - int(month_budget[i-1]))

    #print(month_budget_var)
    variance_list = zip(month_names, month_budget_var)
    variance_list =list(variance_list)
    #print(list(variance_list) )

    #find min and max values

    max1 = max(month_budget_var)
    min1 = min(month_budget_var)
    totalelem = len(variance_list)
    totalavg  = round(sum(month_budget_var)/(totalelem-1),2) 

    ind_max = month_budget_var.index(max1)
    ind_min = month_budget_var.index(min1) 

    #print(ind_max)
    #print(ind_min)

    max_profit_date = variance_list[ind_max][0]
    min_profit_date = variance_list[ind_min][0]

    #print(max_profit_date)
    #print(min_profit_date)

    #print(variance_list[ind_max][0])
    
    #print(totalelem)
    #print("Total change in averages $" + str(totalavg))


#Print on terminal

print("Financial Analysis")
print("====================")
print(f"Total Months: {totalelem}")
print(f"Total: ${total_amt}")
print(f"Average Change ${totalavg}")
print(f"Greatest Increase in Profits: ({max_profit_date})$" +  str(max1)) 
print(f"Greatest Decrease in Profits: ({min_profit_date}) $" + str(min1)) 

#Set variable for output file

analysis_csv1 = os.path.join(os.path.dirname(__file__),"analysis","SChakrabarti_results.txt")
#  Open the output file
with open(analysis_csv1, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------"])
    # Write in output rows
    writer.writerow(["Total Months: " + str(totalelem)])
    writer.writerow(["Total: $" + str(total_amt)])
    writer.writerow(["Average Change: " + str(totalavg)])
    writer.writerow(["Greatest Increase in Profits:("+ str(max_profit_date) + ")$" + str(max1)])
    writer.writerow(["Greatest Decrease in Profits:("+ str(min_profit_date) + ")$"  + str(min1)])