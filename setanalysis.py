"""
Purpose: to find the similarities and differences between different files, made for comparing gene names from a reference genome and specific pathways 
Preconditions: 3 files, 2 input files (doesn't matter the type), title for output and extension
Postconditions: 1 file, output file with the similar elements (strings), number of similar elements (integer), differences between the files, and number of different elements 
"""


import sys
import argparse
def main():
    import os
    # arg parse for input and output files for use with different files
    # got rid of dest for argparse bc it wasn't working
    parser = argparse.ArgumentParser(description='Query elements from two different files.')
    parser.add_argument("input1",help="First Input File",action="store")
    parser.add_argument("input2",help="Second Input File",action="store")
    parser.add_argument("output",help="Output File",action="store")
    #parser.add_argument("-t",help="Number of Cores",action="store",dest="threads",type=int, default=-1, required=False)
    args = parser.parse_args()
    filename = getattr(args, "output")
    # error statements
    if not os.path.isfile(args.input1):
        print (args.input1, "is not a correct file path!")
        sys.exit()
    if not os.path.isfile(args.input2):
        print (args.input2, "is not a correct file path!")
        sys.exit()
    # open and read file
    with open(args.input1, "r") as inputf1:
        # for loop to iterate through each line of the file, split the elements, and turning them 
        for line in inputf1:
            elements1 = line.split(', ')
            elements_set1 = set(elements1)
    # open and read file
    with open(args.input2, "r") as inputf2:
        # for loop to iterate through each line of the file, split the elements, and turning them
        for line in inputf2:
            elements2 = line.split(', ')
            elements_set2 = set(elements2)
        # making the sets of similarities and differences
        similarities = elements_set1.intersection(elements_set2)
        set_of_diffs1 = elements_set1.difference(elements_set2)
        set_of_diffs2 = elements_set2.difference(elements_set1)
    # open output file and write to it
    with open(args.output, "w") as outputf:
        # print header (similarities between both files)
        outputf.write(filename)
        outputf.write("\n")
        # converting set to a list 
        similarities_lst = list(similarities)
        # sorting the list
        similarities_lst.sort()
        # iterating through each line and writing it to the file
        #for i in range(len(similarities_lst)):
        outputf.write(str(similarities_lst))
        # length of elements in list 
        outputf.write(str(len(similarities_lst)))
        #outputf.write("\n")
        # print header
        #outputf.write("\nDifferences between both files:\n") # add names of the files
        # converting set to list
        #setdiffs1_lst = list(set_of_diffs1)
        #setdiffs2_lst = list(set_of_diffs2)
        # combining both lists together
        #setdiffs = setdiffs1_lst + setdiffs2_lst
        # sorting the list
        #setdiffs.sort()
        # iterating through each line and writing it to the file
        #for i in range(len(setdiffs)):
        #    outputf.write(str(setdiffs[i] + "\n"))
        #outputf.write("\n")
        # length of elements in the list
        #outputf.write(str(len(setdiffs)) + " differences")
        #outputf.write("\n")
main()
