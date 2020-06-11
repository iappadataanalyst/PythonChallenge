# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#csvpath = os.path.join('..','Resources', 'budget_data.csv') 
csvpath = os.path.join('Resources', 'election_data.csv') 
output_path = os.path.join('Resources',"ElectionResultOutput.txt")
# Open the CSV


#Assign the variables for the analysis

TotalVotes=0
WinnerVotes= 0
Winner=0
votes= 0
WinningVotes = 0
PollCountDictionary = {}


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header labels to iterate with the values
    header = next(csvreader)    
    csvreader = list(csvreader)
    
    #loop to find the total votes
    for row in csvreader:
        TotalVotes=TotalVotes+1
        #Counting votes for the candidates
        Candidate = row[2]
        
        if Candidate in PollCountDictionary:     
            PollCountDictionary[Candidate] = PollCountDictionary[Candidate]+1 
        else: 
            #Add the candidate to dictionary, and start the counting
            PollCountDictionary.update({Candidate:1})

#calculate the percentage
PollResultsDictionary = {}
for(Candidate), votes in PollCountDictionary.items():
    PollResultsDictionary[Candidate] = str(format((votes*100/TotalVotes), '.3f')) +'% (' + str(votes)+ ')'
#find the Winner
    if votes > WinningVotes:
        WinningVotes = votes 
        Winner = Candidate

#Checkthe results at console
#print(PollResultsDictionary)
#print (Winner, WinningVotes)
#PrintCandidateDetails =[print(key, ' : ', value) for key, value in PollResultsDictionary.items()]


#Getting the results into format
PrintResults1= (    
    f"Election Results"+'\n'
    f"-------------------------" +'\n'
    f"Total Votes: {TotalVotes}" +'\n' 
    f"------------------------- ")+'\n'
    
PrintResults2 = (     
    f"\n------------------------- \n"
    f"Winner: {Winner}"
    f"\n------------------------- \n"    
    )

# assembling the results to make them ready for printing
PollResults = PrintResults1
for key, value in PollResultsDictionary.items():
    PollResults += key + ' : '+ value + '\n'
PollResults += PrintResults2

print(PollResults)
#Write to file
file = open(output_path,"w+")
file.write(PollResults)
file.close()  