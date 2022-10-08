from sys import flags
from tkinter import *
from tkinter import filedialog
import os
from DFAProcessing import processFile
from DFATableGenerator import generateTable
from errorChecking import checkDFA, checkInput

import pathlib

px = 30
py = 10

#functionalities
def loadFile():
    #user_in holds path for string input, dfa_table holds path for transition, global var so we can use it outside this function
    global user_in, dfa_table, inputStringName, inputDFAName
    path = filedialog.askopenfilename(filetypes=[("String files","*.in"),('Transitions','*.dfa')])
    fileExtension = pathlib.Path(path).suffix
    
    if(fileExtension=='.in'):
        textFile = open(path)
        textData = textFile.read()
        textFile.close()

        inputStringName = os.path.basename(path)

        if inputCanvas.find_all()!=():
            inputCanvas.delete('all')
        
        inputCanvas.create_text(100,100, text=textData, fill='black')
        inputCanvas.pack()

        statusCanvas.configure(text="Input from file %s has been successfully loaded" %inputStringName)
        statusCanvas.pack()
        
        user_in = path

    elif(fileExtension=='.dfa'):
        textFile = open(path)
        textData = textFile.read()
        textFile.close()

        inputDFAName = os.path.basename(path)

        if transitionCanvas.find_all()!=():
            transitionCanvas.delete('all')

        generateTable(transitionCanvas, path)

        # transitionCanvas.create_text(100,100, text=textData, fill='black')
        # transitionCanvas.pack()

        statusCanvas.configure(text="DFA table from %s has been successfully loaded" %inputDFAName)
        statusCanvas.pack()

        dfa_table = path

    else:
        statusCanvas.configure(text='Invalid file type')
        statusCanvas.pack()
        print('Invalid file type')

    return path

def processInputFiles():
    
    if(checkInput(user_in, dfa_table, statusCanvas) == True and checkDFA(dfa_table) == True):
        processFile(user_in, dfa_table)      
        textfile = open('strings.out')
        textData = textfile.read()
        textfile.close()

        if outputCanvas.find_all()!=():
            outputCanvas.delete('all')
        
        outputCanvas.create_text(100,100, text=textData, fill='black')
        outputCanvas.pack()

        statusCanvas.configure(text="Input from %s sucessfully processed using DFA Table from %s.\n Output is saved to strings.out" %(inputStringName, inputDFAName))
        statusCanvas.pack()
    else:
        if outputCanvas.find_all()!=():
            outputCanvas.delete('all')

def deleteCanvas():
    inputCanvas.delete('all')
    outputCanvas.delete('all')
    transitionCanvas.delete('all')

#-----------main-window---------------
mainWindow = Tk()
mainWindow.title('Strings and DFA')
mainWindow.geometry('1200x600')
mainWindow.config(bg='lightgreen')


#-----------main-frames---------------
upperFrame = Frame(mainWindow, width='600', height='100', bg='red', padx=10, pady=10)
middleFrame = Frame(mainWindow, width='600', height='300', bg='blue',padx=10, pady=10)
lowerFrame = Frame(mainWindow, width='600', height='100', bg='yellow',padx=10, pady=10)

mainWindow.grid_rowconfigure(1, weight=1)
mainWindow.grid_columnconfigure(0, weight=1)

upperFrame.grid(row=0, sticky='ew')
middleFrame.grid(row=1, sticky='nsew')
lowerFrame.grid(row=2, sticky='ew')


#-----------top-frame-----------------
loadFileButton = Button(upperFrame, text='Load file', width='40', command=loadFile)
loadFileButton.pack(side='left', padx=5)

processButton = Button(upperFrame, text='Process', width='50', command=processInputFiles)
processButton.pack(side='right', padx=5)


#-----------middle-frames-------------
middleFrame.grid_rowconfigure(0, weight=1)
middleFrame.grid_columnconfigure(1, weight=1)

transitionFrame = LabelFrame(middleFrame, text='Transition table', width='250', height='100', bg='pink')
inputFrame = LabelFrame(middleFrame, text='Input', width='250', height='100', bg='violet')
outputFrame = LabelFrame(middleFrame, text='Output', width='250', height='100', bg='white')

transitionFrame.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
inputFrame.grid(row=0, column=1, sticky='ns', padx=5, pady=5)
outputFrame.grid(row=0, column=2, sticky='ns', padx=5, pady=5)


#-----------lower-frame--------------
statusFrame = LabelFrame(lowerFrame, text='Status', width=800, height=100)
statusFrame.pack_propagate(False)
statusFrame.pack(anchor='c', padx=px, pady=py)


#------------Canvases----------------
transitionCanvas = Canvas(transitionFrame, highlightthickness=1, highlightbackground='black') #the transition table is presented through this canvas
transitionCanvas.pack(expand=1, fill=Y, padx=5, pady=5)

inputCanvas = Canvas(inputFrame, highlightthickness=1, highlightbackground='black') #the input string is presented through this canvas
inputCanvas.pack(expand=1, fill=Y, padx=5, pady=5)

outputCanvas = Canvas(outputFrame, highlightthickness=1, highlightbackground='black') #the output string is presented through this canvas
outputCanvas.pack(expand=1, fill=Y, padx=5, pady=5)

statusCanvas = Label(statusFrame, text='test')
statusCanvas.pack()

mainWindow.mainloop()