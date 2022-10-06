import pathlib
import string

#functionalities

def processFile(user_in, dfa_table):
    stringinput = readinput(user_in)
    g = dfa(dfa_table)
    #create an array of all final states
    start, final = fsstate(dfa_table)
    curr = g.start()
    
    #for each line in stringinput, check for the next node given the current node and the state
    for line in stringinput:
        for state in line:
            print(curr + " " + state)
            curr = g.nextnode(curr, ord(state)-48)
        
        #added for debugging purposes only, used as guide to know the current node and the state
        #print(curr + " " + state + "\n")
        if curr in final:
            print("String is valid")
        else:
            print("String is invalid")
    

#graph will be used as a translation of dfa   
graph = dict()
class Graph:
    def __init__(self):
        self.graph = dict()
    #connects the 2 nodes as neighbor (1 way only)   
    def edge (self, n1, n2):
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []
    
        graph[n1].append(n2)
        
    #print the entire graph    
    def printGraph(self):
        for key, val in graph.items():
            print(f"{key}-->{val}")
            
    #returns the following node given the current node and the next state
    def nextnode(self, n1, state):
        #given state, which is the next node
        for line in graph.items():
            if n1 == line[0]:
                return line[1][state]
            
    #returns the starting node
    def start(self):
        for key, val in graph.items():
            return key
#check .in file
#convert input data to array
def readinput(path):
    file = open(path)
    raw = file.read();
    content = raw.split("\n")
    
    return content


def dfa(path):
    dfa = Graph()
    #insert contents of the file into alphabet
    with open(path) as myFile:
        text = myFile.read()
    raw = text.split("\n")
    
    #create an adjacency list for dfa as preparation for graph
    #remove first row, the alphabet    
    #change alphabet into array
    state = raw[0].split(',')    
    raw.pop(0)
    
    #graph will be initialized with contents already 
    table = [raw[0]] * len(raw)

    #remove the first column and 2nd column, save the rest to another array
    for x in raw:
        #graph holds
        table.pop(0)
        holder = x.split(',')
        
        #popping the first column
        holder.pop(0)
        table.append(holder)
    
    #creating adjacency table
    for line in table:
        #take the current line, take the first letter of each line, assume that 1st letter and succeeding letters are 
        #connected via states
        curr = line[0]
        line.pop(0)
        for letter in line:
            dfa.edge(curr, letter)

    return dfa

    #takes note all final states 
def fsstate(dfa_table):
    path = dfa_table
    with open(path) as myFile:
        text = myFile.read()
    raw = text.split("\n")
    
    #create an adjacency list for dfa as preparation for graph
    #remove first row, the alphabet    
    #change alphabet into array
    state = raw[0].split(',')    
    raw.pop(0)
    
    
    
    ftable = [raw[0]] * len(raw) #check first symbol for every string in raw, if +, they are a final state
    stable = [raw[0]] * len(raw) #check first symbol for every string in raw, if -, they are a start state
    for line in raw:
        ftable.pop(0)
        stable.pop(0)
        #in is used for circumstances where start and final shares the same node
        if '+' in line[0]:
            line = line.split(',')
            ftable.append(line[1])
        elif '-' in line[0]:
            line = line.split(',')
            stable.append(line[1])
    
    return stable, ftable


