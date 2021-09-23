# Michelle Lo + Rayat Roy + Theodore Fahey
# SoftDev
# K<01> -- First Python Progam: Printing Names
# <2021>-<09>-<21>

import random

pd1 = ["Michelle Lo", "Rayat Roy", "Theodore Fahey", "Naomi Narajo",
    "Lucas Lee", "William Chen", "Rengguang Zheng", "Owen Yaggy"]
pd2 = ["Joshua Kolepfer", "Alif Abdullah", "Yoonah Chang"]

total = pd1 + pd2
#print(total[x])

#user may input a number to receive a random soft dev student's name
#from their chosen period(s).
a = input("Enter 1 or 2 for a softdev student's name from periods 1 or 2 respectively. Enter 3 for a random name from either: ")

if (a == "1"):
    x = random.randint(0, len(pd1) - 1)
    print(pd1[x])
elif (a == "2"):
    x = random.randint(0, len(pd2) - 1)
    print(pd2[x])
elif (a == "3"):
    x = random.randint(0, len(total) - 1)
    print(total[x])
else:
    print("Invalid entry. Try again")
