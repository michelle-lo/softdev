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
def reader():
    with open('occupations.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter= ",")
        jobs = {} #dictionary created
        i = 0;
        for row in spamreader:
            if (i == 0):
                i += 1 #skips heading
            else:
                jobs[row[0]] = float(row[1]);
        return jobs
            
#random selector
def randSelect(jobs):
    r = random.random() #generates a random float from 0 to 1
    s = 0
    for key in jobs: #for every occupation
        s+= jobs[key]/100 #add occupation's percentage to s
        if(s > r): #if combined percentages is larger than random number,
            #print(key) #return final occupation
            #break
            return key

#randChoices utilizes random.choices to randomly choose an element based on its weighted probability
def randChoices(jobs):
    jobList = list(jobs.keys()) #turns dict keys into a list
    percentages = list(jobs.values()) #dict values into a list
    fin = random.choices(jobList, weights = percentages, k = 1) #generates a list of 1 randomly chosen occupation
    return fin[0]

def main():#runs program
    print(randSelect(reader())) 
    print(randChoices(reader()))

if __name__ == '__main__':
    main()
    


    


