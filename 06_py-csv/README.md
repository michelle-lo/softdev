# Our Approach to Assignment #6

Lone Devos - Michelle Lo, Theodore Fahey, Rayat Roy 

SoftDev 

K07 -- Show What You Know/Summary of our k06 assignment

## File
In our function **reader()**, we used with **open(csv)** to open the csv file. We then used **csv.reader()** with our delimiter set as "," to separate each line into the title and its percentage.

## Dictionary
In the same function as **reader()**, we created the dictionary `jobs` to store our data. We used a for loop to iterate through each line of the file (skipping the first line/heading). We stored the titles as keys of the dictionary (`jobs[row[0]]`) and its percentage as the associated values (`float(row[1]`).

## List
We used lists in two different ways. Firstly, our variable `spamreader` is a list that stores another list. The top layer of `spamreader` stores all of the lines of the csv file. The bottom layer of `spamreader` is the list of a line with the occupation and percentage. 

In our alternative function **randChoices**, we also used lists in the method `random.choices`. `jobList` is a list of the dictionary `jobs` keys while `percentages` is a list of each of the occupations' percentages.

## Basics of github-flavoured markdown
Thanks to the resources contributed to the soft dev discussion forum, our trio was able to get a taste of github-flavoured markdown and and utilize several markdown tools to format our README.md file. For example, in order to format headings, we used `#` of varying lengths for the different sized headings. We also used the `` character to format code. Lastly, we used the `*` char to bolden our words.

```
### Headings will look like this

`Code will look like this`

**and bolded words look like this**
```
### Headings will look like this

`Code will look like this`

**and bolded words look like this**

## Weighted Randomized Selection 
We first generated a random float from 0 to 1. We then created the variable `s` to track the sum of percentages as we iterate through the dictionary. When iterating through the dictionary, once the sum of the percentages so far becomes larger than the random float generated, we return the key. This works because each interval has different sizes according to the percentage/probability. As we iterate through the dictionary, we access whether or not our random float falls in the interval (represented by the boolean (`s > r`)) and when it does, we will print it in **main()**.

Our alternative function, randChoices, uses random.choices to generate a random values from a list. The syntax for random.choices is `random.choices(my_list, weights = [0, 1, 2...], k = n)` where my_list is the list of values that a value is randomly chosen from, weights = [1, 2, 3..] is the values associated weight, and n is the size of the list (number of randomly generated values).
