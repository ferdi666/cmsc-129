from struct import pack
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

import pathlib

px = 30
py = 10


class ImportTable:
    def __init__(self, window):

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(window, width=5, fg='red', font=('Arial',15, 'bold' ))
                self.e.grid(row=i, column=j)
                self.e.insert(END, dataList[i][j])

dataList = [(1,'Raj','Mumbai',19),
        (2,'Aaryan','Pune',18),
        (3,'Vaishnavi','Mumbai',20),
        (4,'Rachna','Mumbai',21),
        (5,'Shubham','Delhi',21)]

total_rows = len(dataList)
total_columns =  len(dataList[0])

#functionalities
def loadFile():
    
    path = filedialog.askopenfilename(filetypes=[("Text files","*.txt"),('all files','*.*')])
    fileExtension = pathlib.Path(path).suffix

    if(fileExtension=='.in'):
        textFile = open(path)
        textData = textFile.read()
        textFile.close()
        inputCanvas.create_text(100,100, text=textData, fill='black')
        inputCanvas.pack()
    elif(fileExtension=='.dfa'):
        print('file extension is dfa')
    else:
        print('Invalid file type')


    
    # print('File is loaded')



def processFile():
    print('Processing at the moment')


#main window
mainWindow = Tk()
mainWindow.title('Strings and DFA')
mainWindow.geometry('900x500')
mainWindow.config(bg='lightgreen')


#main frames
upperFrame = Frame(mainWindow, width=800, height= 200, bg='red')
upperFrame.pack(anchor='c', padx=px, pady=py)

middleFrame = Frame(mainWindow, width=800, height=300, bg='blue')
middleFrame.pack(anchor='c', padx=px, pady=py)

lowerFrame = Frame(mainWindow, width=800, height=100, bg='yellow')
lowerFrame.pack(anchor='c', padx=px, pady=py)


# transition frames/table
transitionFrame = LabelFrame(middleFrame, text='Transition table', bg='pink')
transitionFrame.grid(column=0, row=0, padx=5)

transitionCanvas = Canvas(transitionFrame, width=260, height=300)
transitionCanvas.pack()

# transitionTable = ImportTable(transitionCanvas)


#input frame
inputFrame = LabelFrame(middleFrame, text='Input', bg='violet', width=260, height=300)
inputFrame.grid(column=1, row=0, padx=5)

inputCanvas = Canvas(inputFrame, width=260, height=300)
inputCanvas.pack()


#output frame
outputFrame = LabelFrame(middleFrame, text='Output', bg='white', width=260, height=300)
outputFrame.grid(column=2, row=0, padx=5)

outputCanvas = Canvas(outputFrame, width=260, height=300)
outputCanvas.pack()


#status frame
statusFrame = LabelFrame(lowerFrame, text='Status', width=800, height=100)
statusFrame.pack(anchor='c', padx=px, pady=py)

statusLabel = Label(statusFrame, width=800, height=100)
statusLabel.configure(text='STATUS') #status message
statusLabel.pack(anchor='c')


#buttons
loadFileButton = Button(upperFrame, text='Load file', width=40, command=loadFile)
loadFileButton.grid(column=0, row=0, padx=5)

processButton = Button(upperFrame, text='Process', width=40, command=processFile)
processButton.grid(column=1, row=0)


mainWindow.mainloop()
