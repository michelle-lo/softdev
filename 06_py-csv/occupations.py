# Lone Devos: Michelle Lo, Rayat Roy, Theodore Fahey
# SoftDev
# K<06> -- Reading CSV file + weighted probabilities
# <2021>-<09>-<28>

##SUMMARY
##Our team first discussed how to parse through a csv file.
##We also reviewed how to use and set up a dictionary.Then, we discussed how we can generate
##a random occupation based on its probability.

import csv
import random

#reading csv file
with open('occupations.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ",")
    jobs = {} #dictionary created
    i = 0;
    for row in spamreader:
        if (i == 0):
            i += 1 #skips heading
        else:
            jobs[row[0]] = float(row[1]);
        
#random selector
r = random.random() #generates a random float from 0 to 1
s = 0
for key in jobs: #for every occupation
    s+= jobs[key]/100 #add occupation's percentage to s
    if(s > r): #if combined percentages is larger than random number,
        print(key) #return final occupation
        break

    


