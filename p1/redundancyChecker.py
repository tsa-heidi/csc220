'''
-------------
File 1: <f1>
File 2: <f2>
Number of identical lines: <n>
-------------------------------------
*** <line_num_f1> < line_num_f2> <line_contents>
*** <line_num_f1> < line_num_f2> <line_contents>
Description:
'''
import glob, os
from itertools import combinations




class Pair:

    def __init__(self, file1, file2, count):
        self.file1 = file1
        self.file2 = file2
        self.count = count

    def getFile(self):
        return self.file

    def setCount(self):
        return self.line

    def __str__(self):
        result = file + " " + str(line)
        return result



def compare(file1, file2):
    count = 0
    
    ending = ""
    with open(file1) as file:
        lines = [line.strip() for line in file]
    a = dict((lines[i], i) for i in range(len(lines)))
    with open(file2) as file:
        lines2 = [line.strip() for line in file]
    b = dict((lines2[i], i) for i in range(len(lines2)))
    # find intersection of the dictionaries
    for key in a.keys():
        if key in b.keys():

            count = count + 1


            ending += "<" + str(a[key]) + ">" + "<" +  str(b[key]) + ">" +  "<" + key + ">" + "\n"
            #print("<", a[key], ">" , "<",  b[key], ">",  "<", key, ">")
            #print(type(a[key]), "I'm here", str(a[key]))





    print("-------------------------------------")
    print("File 1: ", file1)
    print("File 2: ", file2)
    print("Number of identical lines: ", count)
    print("-------------------------------------")
    print(ending)


            



def main():
    ''' Function that asks user for a directory, then prints all python file names and the number of lines in each file'''

    # ask user for path
    #path = raw_input("Please indicate path to directory below: \n")
    # test path: path '/Users/tiffanyxiao/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"
    path = "/Users/karensantamaria/Documents/GitHub/csc220-codingchallenges/Coding Challenge 1"

    # identify all python files in directory
    text_files = [f for f in os.listdir(path) if f.endswith('.py')]

    # get all combinations of text_files
    comb = combinations(text_files, 2) # currently only makes combinations with .py files

    for i in list(comb):
        compare(i[0], i[1])





    # outfile = open('results.txt', 'wb')
    # for i in b:
    #     print(outfile, i)
    # outfile.close()

    '''x = set([i.strip() for i in open('testfile1.py')])
    y = set([i.strip() for i in open('testfile2.py')])
    z = x.intersection(y)
    outfile = open('results.txt', 'wb')
    for i in z:
      print>>outfile, i
    outfile.close()'''


    # binary value if identical lines are found
    '''identicalLine = False
    # only print this when
    while identicalLine = True:
        print("-------------------------------------")
        print("File 1: ")
        print("File 2: ")
        print("Number of identical lines: ")
        print("-------------------------------------")
    # print each file name and the number of lines in each file
    for text_file in text_files:
        print(text_file+" "+str(file_len(text_file)))'''

main()