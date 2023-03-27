import pandas as pd
import wikipedia
import time

running = True # is the computation running
index = None

myDict = {'company': [],
          'summary': []}

# Get the first result (title) of a search
# What do you return if there are no results?
def getFirstResult(query):
    results = wikipedia.search(query)
    #print(query,results)
    if (len(results) == 0):
        return []
    else:
        return results[0]

def getSummary(title):
    page = wikipedia.page(title=title,auto_suggest=False)
    return page.summary

def createFrame(companies):
    global index
    for i in range(index, len(companies)):
        if running:
            c = companies[i]
            firstResult = getFirstResult(c)
            if not isinstance(firstResult, list): # if not empty list (firstResult returns either a string or an empty list)
                myDict['company'].append(c)
                myDict['summary'].append(getSummary(firstResult))
                print('success', i)
        else:
            writeToFile()
            break

        index += 1


def writeToFile():
    pd.DataFrame(myDict).to_csv(f'out{index}.csv')

# Read from CSV file, returns series
def getCompanies(i, j):
    df = pd.read_csv('data/nasdaq.csv')
    companies = df.iloc[i:j,1]
    return companies

def getAllCompanies():
    df = pd.read_csv('data/nasdaq.csv')
    companies = df.iloc[:,1]
    return companies

def stopComputation():
    global running
    running = False
    with open('index', 'w') as f:
        f.write(str(index))

def readIndex():
    global index
    with open('index', 'r') as f:
        index = int(f.read())
    
def runComputation():
    c = getAllCompanies()
    readIndex()

    createFrame(c)



'''
I need create table chunks and merge them vertically.

I can either try to construct a CSV file myself or I can use a dataframe
and convert it to a CSV

You dont have to create a new CSV. You will always be appending.

My dataframe needs to be global so that it can be accessed when
the keyboard interrupt comes in

Actually you don't have to worry about appending. Just let the app
output the chunk that it made. The name of the chunk will be the index
of its first row.
'''