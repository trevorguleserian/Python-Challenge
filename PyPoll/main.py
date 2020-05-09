# Importing modules
import os
import csv

# Setting path for PyPoll.csv
csvpath = os.path.join("Resources", "PyPoll.csv")

# Setting variable for counter in iteration below
Vote_tally = 0

# Establising lists to hold each vote for Canidate
Khan = []
Correy = []
Li = []
OTooley = []

# Opening csv path in order to work within its perameters
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Establishing the header of the csvfile
    Header = next(csvreader)

    
    # Starting an iteration through our csv data for each row
    for row in csvreader:

        # Mechanism to count total votes
        Vote_tally = Vote_tally + 1

        # Mechanism to add votes each canidate received through an conditional satement
        if row[2] == "Khan":
            Khan.append(row[2])                       
        elif row[2] == "Correy":
            Correy.append(row[2])
        elif row[2] == "Li":
            Li.append(row[2])
        elif row[2] == "O'Tooley":
            OTooley.append(row[2])

    # Evaluating the ammount of votes each canidate received   
    KhanTotal = len(Khan)
    CorreyTotal = len(Correy)
    LiTotal = len(Li)       
    OTooleyTotal = len(OTooley)

    # Calculating percentage of the total vote each canidate received
    KhanPercentage = (KhanTotal/Vote_tally) * 100
    CorreyPercentage = (CorreyTotal/Vote_tally) * 100
    LiPercentage = (LiTotal/Vote_tally) * 100
    OTooleyPercentage = (OTooleyTotal/Vote_tally) * 100

    # Storing the total vote for each canidate in an array in order to find popular vote   
    PopularVoteIndex = [KhanTotal,CorreyTotal,LiTotal,OTooleyTotal]
    PopularVoteCount = max(PopularVoteIndex)

    # Iterating through the popular vote index to find who had the most votes
    for VoteCount in PopularVoteIndex:
        if PopularVoteCount == KhanTotal:
            Winner = "Khan" 
        elif PopularVoteCount == CorreyTotal:
            Winner = "Correy"
        elif PopularVoteCount == LiTotal:
            Winner = "Li"
        elif PopularVoteCount == OTooleyTotal:
            Winner = "O'Tooley"

    #Printing out each value that we calculated
    print("Election Results")
    print("------------------")
    print(f"Total Votes: {Vote_tally}")
    print("------------------")    
    print(f"Khan: {KhanPercentage} ({KhanTotal})")
    print(f"Correy: {CorreyPercentage} ({CorreyTotal})")
    print(f"Li: {LiPercentage} ({LiTotal})")
    print(f"O'Tooley: {OTooleyPercentage} ({OTooleyTotal})")
    print("------------------")
    print(f"Winner: {Winner}")
# Establishing path for file to be written out
output_path = os.path.join("Analysis", "PyPoll_Analysis")
with open(output_path, "w") as txtfile:
    
    Lines = ["Election Results\n","------------------\n"]
    txtfile.writelines(Lines)
    txtfile.write(f"Total Votes: {Vote_tally}\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Khan: {KhanPercentage} ({KhanTotal})\n")
    txtfile.write(f"Correy: {CorreyPercentage} ({CorreyTotal})\n")
    txtfile.write(f"Li: {LiPercentage} ({LiTotal})\n")
    txtfile.write(f"O'Tooley: {OTooleyPercentage} ({OTooleyTotal})\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Winner: {Winner}\n")



    