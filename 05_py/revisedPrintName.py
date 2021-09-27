# Michelle Lo, Lucas TW, Theodore Fahey
# SoftDev
# K<05> -- Combining our print name programs
# <2021>-<09>-<27>

# POW-WOW SUMMARY
# Our trio first shared with each other our programs and explained our approaches.
# Theodore and Michelle both utilized the approach of creating a list within the python program and then,
# by generating a random number, print a soft dev student’s name from either or combined lists.
# Lucas went the extra step reading a text file with a list of names for easier name input.
# DISCOVERIES
# We learned about how to read an inputted file (from Lucas’s code)
# QUESTIONS (only if you have them)
# COMMENTS (only if you have them)

import sys
#used for sys.argv
from random import randrange

def read_names(filename: str):
    """Reads a text file containing a list of names, where each line contains
    one name, and returns a list of the names."""
    file_contents = ""
    with open(filename, "r") as f: #opens file in "read only" mode
        file_contents = f.read() #records list as a string
    names = file_contents.split("\n") #separates contents of string in a list

    # Remove empty lines
    names = [name for name in names if name]
    return names

def main():
    """Prints a random student name given two files containing lists of names,
    where each line contains one name."""
    if len(sys.argv) != 3:
        print("Usage: python names.py pd1_filename pd2_filename")
        return

    pd1 = read_names(sys.argv[1])
    pd2 = read_names(sys.argv[2])
    names = pd1 + pd2
    # print(names[name_index])

    a = input("Enter 1 or 2 for a softdev student's name from periods 1 or 2 respectively. Enter 3 for a random name from either: ")

    if (a == "1"):
        pd1_index = randrange(len(pd1))
        print(pd1[pd1_index])
    elif (a == "2"):
        pd2_index = randrange(len(pd2))
        print(pd2[pd2_index])
    elif (a == "3"):
        name_index = randrange(len(names))
        print(names[name_index])
    else:
        print("Invalid entry. Try again")

if __name__ == "__main__": #helps when importing other modules
    main()
