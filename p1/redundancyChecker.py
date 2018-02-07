'''
File: redundancyChecker.py
Authors: Tiffany Xiao, Mai Ngo, Karen Santamaria
Description: Program reads all the files in a specified directory and prints a report of the lines that are identical in any pair of files
'''
import glob, os
from itertools import combinations


def compare(file1, file2):
    '''compare between two files and output information on the duplicated lines'''

    duplicate_count = 0
    duplicate_info = ""

    with open(file1) as file:
        lines = [line.strip() for line in file]
    a = dict((lines[i], i) for i in range(len(lines)))
    with open(file2) as file:
        lines2 = [line.strip() for line in file]
    b = dict((lines2[i], i) for i in range(len(lines2)))

    # find intersection of the dictionaries
    for key in a.keys():
        if key in b.keys():

            duplicate_count += 1
            duplicate_info += "*** " + str(a[key]) + " "+  str(b[key]) + " " + key + "\n"

    if duplicate_count > 0:
        print("-------------------------------------")
        print("File 1: ", file1)
        print("File 2: ", file2)
        print("Number of identical lines: ", duplicate_count)
        print("-------------------------------------")
        print(duplicate_info)




def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    #path = raw_input("Please indicate path to directory below: \n")
    path = "/Users/karensantamaria/Documents/GitHub/csc220/p1"

    # identify all python files in directory
    #text_files = [f for f in os.listdir(path) if f.endswith('.py')]
    text_files = [f for f in os.listdir(path)]

    # get all combinations of text_files
    comb = combinations(text_files, 2)

    for i in list(comb):
        compare(i[0], i[1])

main()
