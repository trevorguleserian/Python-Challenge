# Importing modules
import os
import csv


# Setting path for PyBank.csv
csvpath = os.path.join("Resources", "PyBank.csv")

# Establishing counter for total monthcount and Profit_Losses
Monthcount = 0
Profit_Losses = 0.0

# Setting empty array values to add into later
date = []
profit = []
profit_month = []



# Opening path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Stating header of data
    Header = next(csvreader)

    # Initiating iteration to add values to empty arrays listed above
    for row in csvreader:

        profit.append(int(row[1]))
        date.append(row[0])

        # Month counter mechanism
        Monthcount = Monthcount + 1  

        
    # iterating through profit to find total profit
    for x in profit:
        Profit_Losses = sum(profit)

    # Calculating average change
    Average_Change = round(Profit_Losses/Monthcount,2) 

    # Iterating through profit to find the length of the profit as a range in order to find biggest change and loss 
    for i in range(len(profit)-1):
        profit_month.append(profit[i-1] - profit[i])

    # Using the index of the greatest increase and decrease to find the date accociated with the change
    Max = profit_month.index(max(profit_month)) + 1
    Min = profit_month.index(min(profit_month)) + 1 



    

    # Printing findings
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {Monthcount}")
    print(f"Total: {Profit_Losses}")
    print(f"Average Change: {Average_Change}")
    print(f"Greatest increase in profits: {date[Max]} ({max(profit_month)})")
    print(f"Greatest increase in profits: {date[Min]} ({min(profit_month)})")

    # Output path written as txt file
    output_path = os.path.join("Analysis", "PyBank_Analysis")
with open(output_path, "w") as txtfile:
    
    Lines = ["Financial Analysis\n","------------------\n"]
    txtfile.writelines(Lines)
    txtfile.write(f"Total Months: {Monthcount}\n")
    txtfile.write(f"Total: {Profit_Losses}\n")
    txtfile.write(f"Average Change: {Average_Change}\n")
    txtfile.write(f"Greatest increase in profits: {date[Max]} ({max(profit_month)})\n")
    txtfile.write(f"Greatest increase in profits: {date[Min]} ({min(profit_month)})\n")
    
    
    
        
    

        
        


