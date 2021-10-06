##[Lone Devos] Michelle Lo, Rayat Roy, Theodore Fahey
##SoftDev
##K10 -- Putting Little Pieces Together/Creating our first webpage
##2021-10-05

from flask import Flask
import csv
import random
app = Flask(__name__)

@app.route("/")
def display():
    with open('occupations.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter= ",")
        jobs = {} #dictionary created
        i = 0;
        for row in spamreader:
            if (i == 0):
                i += 1 #skips heading
            else:
                jobs[row[0]] = float(row[1]);
        occupation = randSelect(jobs)
        jobs.pop('Total') #removes "total" as a key from the list of occupations
        return "Lone Devos: Theodore Fahey, Michelle Lo, and Rayat Roy "+"Chosen occupation: " + occupation + " " + (str)(jobs.keys()) 
def randSelect(jobs):
    r = random.random() #generates a random float from 0 to 1
    s = 0
    for key in jobs: #for every occupation
        s+= jobs[key]/100 #add occupation's percentage to s
        if(s > r): #if combined percentages is larger than random number,
            #print(key) #return final occupation
            #break
            return key
app.run()
