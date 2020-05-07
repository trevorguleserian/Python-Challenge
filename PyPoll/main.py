import os
import csv


csvpath = os.path.join("Resources", "03-Python_Homework_Instructions_PyPoll_Resources_election_data")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimter=",")

    print(csvreader)
