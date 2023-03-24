#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:58:36 2023

@author: kianatalavera
"""

import os
import csv

filepath = os.path.join('Resources', '/Users/kianatalavera/Desktop/github/python-challenge/PyPoll/Resources/election_data.csv')

# Opening the CSV
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]
    
#total votes
total_votes = len(candidate_list)

#candidates with the corresponding number of votes
canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

#first candidate becomes the winner 
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")




filepath = os.path.join('Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)

