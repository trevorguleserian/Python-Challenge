import os
import csv


csvpath = os.path.join("Resources", "PyPoll.csv")

Vote_tally = 0
Canidate = []
Khan = []
Correy = []
Li = []
OTooley = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    Header = next(csvreader)

    

    for row in csvreader:
        
        Vote_tally = Vote_tally + 1

        if row[2] == "Khan":
            Khan.append(row[2])                       
        elif row[2] == "Correy":
            Correy.append(row[2])
        elif row[2] == "Li":
            Li.append(row[2])
        elif row[2] == "O'Tooley":
            OTooley.append(row[2])
        
    KhanTotal = len(Khan)
    CorreyTotal = len(Correy)
    LiTotal = len(Li)       
    OTooleyTotal = len(OTooley)

    KhanPercentage = (KhanTotal/Vote_tally) * 100
    CorreyPercentage = (CorreyTotal/Vote_tally) * 100
    LiPercentage = (LiTotal/Vote_tally) * 100
    OTooleyPercentage = (OTooleyTotal/Vote_tally) * 100

    PopularVoteIndex = [KhanTotal,CorreyTotal,LiTotal,OTooleyTotal]
    PopularVoteCount = max(PopularVoteIndex)

    for VoteCount in PopularVoteIndex:
        if PopularVoteCount == KhanTotal:
            Winner = "Khan" 
        elif PopularVoteCount == CorreyTotal:
            Winner = "Correy"
        elif PopularVoteCount == LiTotal:
            Winner = "Li"
        elif PopularVoteCount == OTooleyTotal:
            Winner = "O'Tooley"







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
