'''
Authors: Tiffany Xiao, Mai Ngo, Karen Santamaria
Date: February 1, 2018
Title: Redundancy Detector


Program that reads all the files in a specified directory and prints a report of
lines that are identical in any pair of files
'''
import os
from itertools import combinations

def compare(path, file1, file2):
    """ Function to compare two files and identify a matching line, then print the matching lines in desired format.

    Parameters:
    path - path to the files
    file1 - the first file to check
    file2 - the second file to check
    """

    # count number of duplicate lines
    duplicate_count = 0

    # string with all duplicate lines (and their line numbers)
    duplicate_info = ""


    # create 2Dlists of file1 and file2 which stores [string, line_num]

    with open(path+"/"+file1) as file:
        lines = [line for line in file]
    file1_list = [[lines[i].strip(), i+1] for i in range(len(lines)) if lines[i].strip()]

    with open(path+"/"+file2) as file:
        lines2 = [line for line in file]
    file2_list = [[lines2[i].strip(), i+1] for i in range(len(lines2)) if lines2[i].strip()]

    for word_line1 in file1_list:
        for word_line2 in file2_list:
            if word_line1[0] == word_line2[0]:
                duplicate_count += 1
                duplicate_info += "*** " + str(word_line1[1]) + " "+  str(word_line2[1]) + " " + word_line1[0] + "\n"

    if (duplicate_count != 0):
        print("-------------------------------------")
        print("File 1: ", file1)
        print("File 2: ", file2)
        print("Number of identical lines: ", duplicate_count)
        print("-------------------------------------")
        print(duplicate_info)

def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    path = input("Please indicate absolute path to directory below: \n")

    # create a try catch block in case of invalid directory inputted
    try:
        # identify all python files in directory
        textFiles = [f for f in os.listdir(path) if (os.path.isfile(os.path.join(path, f)) and not f.startswith("."))]

        # get all combinations of textFiles
        comb = combinations(textFiles, 2)

        # compare each combination of text files
        for i in list(comb):
            compare(path,i[0], i[1])

    except OSError:
        print("Invalid path to directory inputted. Please try again.")
        main()

main()
