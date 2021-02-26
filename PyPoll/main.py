import os
import csv
import statistics 
import collections




line_break = "--------------------------"
my_csv_list = []
candidate_list = []

 

#Funtion for terminal output and writing file

def print_screen_file(*args, **kwargs):

    fileName = os.path.join(os.path.dirname(__file__), "analysis" , 'SChakrabarti_results.txt')

    print(*args, **kwargs)

    #print("the args are :" , args)

    #print("the KW args are: " , **kwargs)

    with open(fileName, 'a') as file: 

        print(*args,  file=file)

 

 

#Function to read input file and to write data to a list

def readFile (file_name):

    file_data_csv = os.path.join(os.path.dirname(__file__), "Resources" , file_name)

    with open (file_data_csv, 'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        next(csvreader)

    
        for row in csvreader:

            my_csv_list.append(row)

    calcStats()

 

# Function to read data and calculate statistics

def calcStats():

    for x, res in enumerate(my_csv_list):

        candidate_list.append(res[2])

    candidate_occurences = collections.Counter(candidate_list)

    print_screen_file("Election Results \n", line_break)

    print_screen_file("Total Votes: " , str(len(my_csv_list)))

 
    # Access dictionary and print results and compute % of VOTES

    total_votes = int(len(my_csv_list))

    for k,v in candidate_occurences.items():

        percentage_votes  = round((int(v)/total_votes)*100, 2)

        print_screen_file( k , percentage_votes, "% (", v, ")") 

    
    itemMaxValue = max(candidate_occurences.items(), key=lambda x : x[1])

    print_screen_file(line_break)

    print_screen_file("Winner: ", itemMaxValue[0])

 
readFile("election_data.csv")