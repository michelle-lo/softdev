Lone Devos - Michelle Lo, Theodore Fahey, Rayat Roy
SoftDev
K<06> -- Our Approach to Assignment 6 
2021-09-29

Our approach to assignment #6:

file:
In our function reader(), we used with open(csv) to open the csv file. We then used csv.reader() with our delimiter set as "," to separate each line into the title and its percentage. 

dictionary: 
In the same function as reader(), we created the dictionary "jobs" to store our data. We used a for loop to iterate through each line of the file (skipping the first line/heading). We stored the titles as keys of the dictionary (jobs[row[0]]) and its percentage as the associated values (float(row[1]). 

list:
