Lone Devos - Michelle Lo, Theodore Fahey, Rayat Roy
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
<yyyy>-<mm>-<dd>

Our approach to assignment #6:

file:
In our function reader(), we used with open(csv) to open the csv file. We then used csv.reader() with our delimiter set as "," to separate each line into the title and its percentage. 

dictionary: 
In the same function as reader(), we created the dictionary "jobs" to store our data. We used a for loop to iterate through each line of the file (skipping the first line/heading). We stored the titles as keys of the dictionary (jobs[row[0]]) and its percentage as the associated values (float(row[1]). 

list:
We used lists in several ways. Firstly, our variable "spamreader" is a list that stores another list. The top layer of spamreader stores all of the lines of the csv file. The bottom layer of spamreader is the list of a line with the occupation and percentage.
...

basics of github-flavoured markdown:
github tastes very delicious. bon appetit????

weighted randomized selection:
We first generated a random float from 0 to 1. We then created the variable "s" to track the sum of percentages as we iterate through the dictionary. When iterating through the dictionary, once the sum of the percentages so far becomes larger than the random float generated, we return the key. This works because each interval has different sizes according to the percentage/probability. As we iterate through the dictionary, we access whether or not our random float falls in the interval (represented by the boolean (s > r)).
