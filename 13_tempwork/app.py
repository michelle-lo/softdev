# Squidcatman - Michelle Lo & Hellokitty, Angela Zhang & Inky, Deven Maheshwari & Batman
# SoftDev
# K13 - Template for Success/Using Flask/Creating flask app using the occupation python data
# October 13 2021

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/occupyflaskst")
def test_tmplt():
    """
    Creates occupyflaskst route on flask app. Uses a dictonary to take in occupation jobs, percentages, and associated links and sends them to tablified.html.
    Parameters:
        None

    Returns:
        None
    """

    jobp = {} #creates dictionary
    with open('data/occupations.csv') as csvfile: #reads csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"] #name of job
            percentage = float(row["Percentage"]) #percentage for job
            link = row["Link"] #link for job
            jobp[job] = [str(percentage), link] #the percentages and link are now values of a key
        del jobp['Total'] #gets rid of "total" from the list of occupations
    return render_template( 'tablified.html', foo = "K13", random = chooseRandom(jobp), response = jobp) #corresponds to the vars in tablified (foo is assignment #)

def chooseRandom(jobdict):
    """
    Chooses random occupation based on weighted averages.
    Parameters:
        jobdict - dictionary created of csv file
    Returns:
        k - random job name
    """
    randVal = random.uniform(0, 100) # randomly chooses a number from 0 to total percentage
    for k, v in jobdict.items():
        randVal -= float(v[0])
        if randVal <= 0:    # first cumulative percentage >= random value is the job chosen
            return k

if __name__ == "__main__":
    app.debug = True
    app.run()
