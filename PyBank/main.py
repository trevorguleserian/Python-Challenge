import os
import csv



csvpath = os.path.join("Resources", "PyBank.csv")

Monthcount = 0
Profit_Losses = 0.0
date = []
profit = []
profit_month = []




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    Header = next(csvreader)

    for row in csvreader:

        profit.append(int(row[1]))
        date.append(row[0])

        Monthcount = Monthcount + 1  

        

    for x in profit:
        Profit_Losses = sum(profit)

    Average_Change = round(Profit_Losses/Monthcount,2) 

    for i in range(len(profit)-1):
        profit_month.append(profit[i-1] - profit[i])

    Max = profit_month.index(max(profit_month)) + 1
    Min = profit_month.index(min(profit_month)) + 1 





    
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {Monthcount}")
    print(f"Total: {Profit_Losses}")
    print(f"Average Change: {Average_Change}")
    print(f"Greatest increase in profits: {date[Max]} ({max(profit_month)})")
    print(f"Greatest increase in profits: {date[Min]} ({min(profit_month)})")
    
    
    
        
    

        
        


