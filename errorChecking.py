from doctest import FAIL_FAST
from enum import Flag
import pathlib
import string
import linecache
from tkinter.tix import Tree

from DFAProcessing import readinput

#checks the input text file
def checkInput(user_in, dfa_table, statusCanvas):
    flag1=True
    flag2=True
    flag3=True

    particular_line = linecache.getline(dfa_table, 1) #extracts first line from DFA text file
    res=splitFirstLine(particular_line)#calls for the fuction that removes the comma from the first line from DFA text file and stores it
    input=readinput(user_in)#reads the string text file


    #for loop that checks if there is an empty element
    for i in range (len(input)):
        if input[i]=='':
            flag1=False
            statusCanvas.configure(text="there's an empty element")
            statusCanvas.pack()
            return False
    #for loop that checks if there is a whitespace in an element
    for i, word in enumerate(input):
        #insert statuscanvas
        # print(input[i])
        for x in range(len(word)):
            # print(word[x])
            if word[x] ==" ":
                flag2 = False
                statusCanvas.configure(text="existing whitespace in elements")
                statusCanvas.pack()
                return False
    
    flag3=(compareString(res, input, statusCanvas))

    if(flag1==False or flag2==False or flag3==False):
        return False
    else:
        return True

def checkDFA(dfa_table):
    particular_line = linecache.getline(dfa_table, 1)
    # print(particular_line)
    test= splitFirstLine(particular_line)
    # print(test)
    input=readinput(dfa_table)

    myset = set(test)

    for i in range (len(input)):
        if input[i]=='':

            print('Theres an empty element --DFA')
            return False

    #for loop that checks if there is a whitespace in an element
    for i, dfaword in enumerate(input):
        #insert statuscanvas
        for x in range(len(dfaword)):
            if dfaword[x] == ' ':
                print("Existing whitespace in elements! --DFA")
                return False
    
    if (len(test) != len(myset)):
        print('Duplicates in line 1 for DFA file!')
        return False
    else:
        return True 


#splits the first line and removes the comma
def splitFirstLine(firstLine):

    string = firstLine.strip()
    res=string.split(",")
    return res

#compares the input string with the valid strings in the DFA file
def compareString(res, input, statusCanvas):
    
    setRes = set(res)
    setInput=''.join(input)
    finalInput=set(setInput)

    mergedRes = ''.join(setRes)
    mergedInput = ''.join(finalInput)

    # testRes = '10'
    # testInput = '01'

    # if testRes == testInput:
    #     print('holyshit it worked!')
    # else:
    #     print('oh no no no...')

    print("mergedRes: %s" %mergedRes)
    print("mergedInput: %s" %mergedInput)
    if mergedRes == mergedInput:
        print('input strings are valid')
        return True
    else:
        statusCanvas.configure(text="an error with input string exists")
        statusCanvas.pack()
        return False
