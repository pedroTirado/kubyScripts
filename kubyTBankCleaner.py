import csv

"""
TIME CLOCKED-IN:
    04/21/2022 ---> 8 hrs

MACROS:
print("",) # DEBUG
"""

macInPath = '/Users/dro/Documents/' # input file path on dro's macPro
macOutPath = '/Users/dro/Documents/'
debInPath = '/home/dro/kubyScripts/' # input file path on dro's debian
debOutPath = '/home/dro/kubyScripts/'
buntuInPath = '/data/birc/home/pedrotirado/kubyScripts/origCopies/' # input file path on dro's ubuntu
buntuOutPath = '/data/birc/home/pedrotirado/kubyScripts/editedCopies/'

"""
load accessory metadata from .txt files
"""
def loadTxtMeta(file = ''):
    
    chaptQs = {}
    curLine = ''
    curPrompt = ''
    chName = ''
    blooms = ''

    if file != '':
        with open(buntuInPath + file, 'r') as f:
            
            # return f.read() # returns contents of entire file
            curLine = str(f.readline())
            # print("curLine:", curLine) # DEBUG
            
            while curLine != '': # haven't reached EOF...
            
                if '.  ' in curLine: # if is question prompt...
                    
                    # print("curLine:", repr(curLine)) # DEBUG
                    # print("curPrompt:", repr(curLine[curLine.index('.  ')+3:-1])) # DEBUG
                    curPrompt = curLine[curLine.index('.  ')+3:-1]
                    # print("curPrompt:", curPrompt) # DEBUG

                elif 'chaptername' in curLine: # if is chapter name...
                    
                    chName = curLine[-2:-1] # extracts the integer val. only
                    # print(curLine) # DEBUG
                    # print("num:",repr(curLine[-2:-1])) # DEBUG
                
                elif 'bloomslevel' in curLine:
                    blooms = curLine[curLine.index(':  ')+3:-1]
                    chaptQs[curPrompt] = {chName, blooms} 
                
                curLine = str(f.readline())
                # print("curLine:", curLine) # DEBUG
            
            # print("chaptQs:", chaptQs) # DEBUG
    else:
        print("ERROR: Can't load specified txt file!")
    
    return chaptQs

"""
load accessory metadata from taxonChaptIDs.csv
"""
def loadChID(chaptIDs):
    with open(buntuInPath + 'taxonChaptIDs.csv') as r:
        reader = csv.reader(r, delimiter=',')
        
        row = next(reader)

        for row in reader:
            chaptIDs[row[3]] = row[4]

"""
review prompt in column K (col. #11 - mc_prompt), and fill in this column (col. #2 - destination_topic)
with the relevant chapter ID; chapter codes can be found in ---> taxonChaptIDs.csv
"""
def cleanColB(colK: str = ""):
    # print("colK:",colK) # DEBUG

    chID = 0
    global ch1Qs
    global ch2Qs
    global chaptIDs

    # print("ch1Qs:",ch1Qs) # DEBUG
    # print("ch1Qs:",ch2Qs) # DEBUG

    # q = colK[3:-4] # slices away the <p>...</p>
    q = colK[3:colK.index('</p>')] # slices away the <p>...</p>
    # print("q:",q) # DEBUG
    
    if ch1Qs.get(q) != None:
        chID = chaptIDs["Chapter 1"]
    elif ch2Qs.get(q) != None:
        chID = chaptIDs["Chapter 2"]
    else:
        chID = -1 # specified prompt (col. K) DNE in available question bank dictionaries

    return chID


"""
assign a Webb's Depth of Knowledge
1-Recall <---> Understanding/Remembering
2-Skill/Concept <---> Applying
3-Strategic Thinking <---> Analyzing
4-Extended Thinking <---> Evaluating/Creating

correlation based on Bloom's (https://uen.instructure.com/courses/314069/files/70811844/preview?verifier=XrzkpNsZVLMJnXLhYgfx41G0BpMwE9bhCXFKtXNT)
"""
def cleanColE():
    ...


if __name__ == "__main__":

    ch1Qs = {}
    ch2Qs = {}
    ch1Qs = loadTxtMeta('tbankCh1.txt')
    ch2Qs = loadTxtMeta('tbankCh2.txt')

    # print("tbankCh1Buff", tbankCh1Buff) # DEBUG
    # print("tbankCh2Buff", tbankCh2Buff) # DEBUG

    # print("ch1Qs:", ch1Qs) # DEBUG
    # print("ch2Qs:", ch2Qs) # DEBUG

    chID = 0

    chaptIDs = {'Chapter 1': -1,'Chapter 2': -1,'Chapter 3': -1,
                'Chapter 4': -1,'Chapter 5': -1,'Chapter 6': -1,
                'Chapter 7': -1,'Chapter 8': -1,'Chapter 9': -1,
                'Chapter 10': -1,'Chapter 11': -1,'Chapter 12': -1,
                'Chapter 13': -1,'Chapter 14': -1,'Chapter 15': -1,
                'Chapter 16': -1,'Chapter 17': -1,'Chapter 18': -1,
                'Chapter 19': -1,'Chapter 20': -1}
    
    loadChID(chaptIDs)

    # print("chaptIDs:", chaptIDs) # DEBUG

    with open(buntuInPath + 'mc.csv',newline='') as csvinput:
        with open(buntuOutPath + 'mc_edited.csv','w',newline='') as csvoutput:
            reader = csv.reader(csvinput, delimiter=',')
            writer = csv.writer(csvoutput, delimiter=',')

            all = []
            row = next(reader)

            for row in reader:

                chID = cleanColB(str(row[10])) # row[10] ---> col. #11 ---> mc_prompt

                # print("chID:",chID) # DEBUG

                if chID != -1: # corresp. chapter ID could be discerned...
                    
                    row[1] = chID # row[1] ---> col. #2 ---> destination_topic
                
                writer.writerow(row)
