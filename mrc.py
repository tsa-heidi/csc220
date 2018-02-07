'''

Author: Mai Ngo
Class: CSC 220
Coding Challenge 1

Objective: write a program that reads all the files in a specified directory
and prints a report of the lines that are identical in any pair of files

-------------------------------------
File 1: <f1>
File 2: <f2>
Number of identical lines: <n>
-------------------------------------
*** <line_num_f1> < line_num_f2> <line_contents>
*** <line_num_f1> < line_num_f2> <line_contents>

'''

import os, re
from itertools import combinations

def compare(file1, file2):
    
    for key in file1.keys():
        if key in file2.keys():
            print(str(file1[key]) + ", " + str(file2[key]) + ", " + key)
            

def main():

    source = input("Please input the path to directory: ")
    # test path: /Users/Mai/Documents/___CLASSES/First year/Spring 2017/CSC 111/Final project

    # find all .py files in directory
    pyfiles = [file for file in os.listdir(source) if file.endswith('.py')]    

    print(pyfiles) # test print names of all .py files

    # add all the lines in each file into a separate dictionary
    line_num = 1 # line number starts at 1
    dicts_list = [{} for i in range(0,len(pyfiles))] # list of dictionaries containing all the lines along witht their line number
    file_num = 0
    for file in pyfiles:
        file_object = open(str(source + "/" + file), "r")
        
        for line in file_object: 
            dicts_list[file_num][line.s/Users/Mai/Documents/___CLASSES/First year/Spring 2017/CSC 111/Final projecttrip()] = line_num
            line_num += 1
        file_num +=1

     
    #print(dicts_list[2]) # test print a dictionary

    # compare different files
    comb = combinations(dicts_list, 2)
    for i in list(comb):
        print("File 1: " + pyfiles[dicts_list.index(i[0])] + "\nFile 2: " +
              pyfiles[dicts_list.index(i[1])])
        compare(i[0],i[1])
       

main()
    
