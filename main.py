import pandas as pd
import wikipedia
import time



# Get the first result (title) of a search
# What do you return if there are no results?
def getFirstResult(query):
    results = wikipedia.search(query)
    #print(query,results)
    if (len(results) == 0):
        return []
    else:
        return results[0]
    
def firstParagraph(title):
    page = wikipedia.page(title=title,auto_suggest=False)
    return page.summary

def companySummary(name):
    title = getFirstResult(name)

    return firstParagraph(title)

def createFrame(companies):

    # Remove companies that do not have a Wikipedia article
    #companies = [c for c in companies if not isinstance(getFirstResult(c),list)]
    filterCompanies = []
    for c in companies:
        firstResult = getFirstResult(c)
        if not isinstance(firstResult, list):
            filterCompanies.append(c)

        

    # I want to create a new dataframe that consists of two columns. Company name and first paragraph
    paragraphs = []
    for c in filterCompanies:
        paragraphs.append(companySummary(c))

    myDict = {'company': filterCompanies,
            'summary': paragraphs}
        
    f = pd.DataFrame(myDict)
    return f

def getCurrentPosition():
    ret = 0
    with open('index', 'r') as f:
        ret = f.read()
    return ret

# Read from CSV file, returns series
def getCompanies(i, j):
    df = pd.read_csv('data/nasdaq.csv')
    companies = df.iloc[i:j,1]
    return companies

def getAllCompanies():
    df = pd.read_csv('data/nasdaq.csv')
    companies = df.iloc[:,1]
    return companies

def createFile(table):
    html_table = table.to_html()

    with open('myfile.html', 'w', encoding="utf-8") as file:
        file.write(html_table)

def mainProcess():
    c = getCompanies(10,50)
    fr = createFrame(c)
    print(fr)
    #createFile(fr)

#mainProcess()

print(getCurrentPosition())