from doctest import FAIL_FAST
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

    # firstlineDFA = open(dfa_table)
    # contentfirstLineDFA = firstlineDFA.read()
    # firstlineDFA.close()
    particular_line = linecache.getline(dfa_table, 1) #extracts first line from DFA text file
    #print('particular-line:')
    #print(particular_line)

    res=splitFirstLine(particular_line)#calls for the fuction that removes the comma from the first line from DFA text file and stores it
    #print(res)
    # dfa_file = open(dfa_table)
    # content = dfa_file.readlines()
    # print('-----------')
    # print(content[0])
    # testfile = open(content[0])
    # raw = testfile.read()
    # content = raw.split(",")
    # print('----------->')
    # print(content)
    #print("hello")
    #print("hi", input)
    input=readinput(user_in)#reads the string text file
    flag3=(compareString(res, input, statusCanvas))#

    #for loop that checks if there is an empty element
    for i in range (len(input)):
        if input[i]==[]:
            flag1=False
            statusCanvas.configure(text="there's an empty element")
            statusCanvas.pack()
            break
    #for loop that checks if there is a whitespace in an element
    for i, word in enumerate(input):
        #insert statuscanvas
        #print ("string[{}] = {}".format(i, word))
        for x in range(len(word)):
            #print("huh?", word[x])
            if word[x] == ' ':
                flag2 = False
                statusCanvas.configure(text="existing whitespace in elements")
                statusCanvas.pack()
                break

    if(flag1==False or flag2==False or flag3==False):
        return False
    else:
        return True

# def checkDFA(dfa_table):
#     particular_line = linecache.getline(dfa_table, 1)
#     print()

#splits the first line and removes the comma
def splitFirstLine(firstLine):
    # print("--------^")
    string = firstLine.strip()
    res=string.split(",")
    return res

#compares the input string with the valid strings in the DFA file
def compareString(res, input, statusCanvas):
    
    setRes = set(res)
    setInput=''.join(input)
    finalInput=set(setInput)
    # print(testInput)
    # print(finalInput)

    mergedRes = ''.join(setRes)
    mergedInput = ''.join(finalInput)

    # print("--------^")
    # print(mergedRes)
    # print(mergedInput)
    if mergedRes == mergedInput:
        print('input strings are valid')
        return True
    else:
        statusCanvas.configure(text="an error with input string exists")
        statusCanvas.pack()
        return False
