from tkinter import *
import csv


def generateTable(transitionCanvas, path):

    tablelist = list()
    print("path: %s" %path)

    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            tablelist.append(row)
            print(row)

    itemsinLine1 = len(tablelist[0])
    itemsinLine2 = len(tablelist[1])
    numberOfIterations = itemsinLine2 - itemsinLine1

    print('items in line 1: %s' %itemsinLine1)
    print('items in line 2: %s' %itemsinLine2)
    print('number of iterations: %s' %numberOfIterations)

    total_rows = len(tablelist)
    total_columns =  len(tablelist[1])

    for i in range(numberOfIterations):
        if i == 0:
            tablelist[0].insert(0, 'Start')
        else:
            tablelist[0].insert(0, '')

    print(tablelist)
    print('total rows: %s' %total_rows)
    print('total columns: %s' %total_columns)

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(transitionCanvas, width=5, fg='red', font=('Arial',15, 'bold' ))
            e.grid(row=i, column=j)
            e.insert(END, tablelist[i][j])



