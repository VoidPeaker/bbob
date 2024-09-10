import pandas as pd
import json, random, os


elements = ["adjectives", "nouns", "of"]
#resourcesPath = "C:/Users/fires/OneDrive/Documents/Programming/blank blank of blank/bbob/resources/"
resourcesPath = "../bbob/resources/"


# class jsonRepo:
#     wordJson = json
#     wordProb = []
#     wordList = []

#     def __init__(self, inputFile):
#         self.wordJson = inputFile
#         i = 0
#         for i in self.wordJson:
#             self.wordProb.append(self.wordJson[int(i)]['rollWeight'])
#             self.wordList.append(i)
    
#     def getRandomWord(self):
#         word = random.choices(self.wordList, self.wordProb)

        
    # for i in nounsRepo:
    #     nounsProb.append(nounsRepo[i]['weight'])
    #     nounsList.append(i)
    # for i in ofRepo:
    #     ofProb.append(ofRepo[i]['weight'])
    #     ofList.append(i)
def convertExcelSheetIntoJson(sheetName):
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    hold2 = sheetName+".json"

    return json.load(open(hold2))

# def loadResources():

adjRepo = convertExcelSheetIntoJson("adjectives") #at the same time converting the excell worksheet into the json and setting the json file to be accesses from the rest of this program
nounsRepo = convertExcelSheetIntoJson("nouns")
ofRepo = convertExcelSheetIntoJson("of")

class myItem():
    def __init__(self):
        pass
    def adjective(self, item, Repo=adjRepo):

        self.name = Repo[item[0]]['name']
        self.rollWeight = item[0]['rollWeight']
        self.attack = item[0]['att']
        self.speed = item[0]['speed']
        self.firstLetter = item[0]['firstLetter']
        self.set = item[0]['set']
        self.hp = item[0]['hp']
    def noun(self, item):
        self.name = item[1]['name']
        self.rollWeight = item[1]['rollWeight']
        self.attack = item[1]['att']
        self.speed = item[1]['speed']
        self.firstLetter = item[1]['firstLetter']
        self.set = item[1]['set']
        self.hp = item[1]['hp']
    def of(self, item):
        self.name = item[2]['name']
        self.rollWeight = item[2]['rollWeight']
        self.attack = item[2]['att']
        self.speed = item[2]['speed']
        self.firstLetter = item[2]['firstLetter']
        self.set = item[2]['set']
        self.hp = item[2]['hp']


#adjRepo = jsonRepo("adjectives")

# adjClass.weight(thisItem)

#loadResources()

thisItem = ['fearful', '______', '______']
print(myItem.adjective(thisItem).name)


"""
def playerStatCalc(element): #is list rn
    #attack
    adjAtt = adjRam['{}'.format(element[0])]['att']
    nounsAtt = nounsRam['{}'.format(element[1])]['att']
    ofAtt = ofRam['{}'.format(element[2])]['att']
    #defence
    adjDef = adjRam['{}'.format(element[0])]['def']
    nounsDef = nounsRam['{}'.format(element[1])]['def']
    ofDef = ofRam['{}'.format(element[2])]['def']
    #speed
    adjSpd = adjRam['{}'.format(element[0])]['speed']
    nounsSpd = nounsRam['{}'.format(element[1])]['speed']
    ofSpd = ofRam['{}'.format(element[2])]['speed']

    a = 1 #alliteration bonus
    if allitBonus(element):
        a = 2
    baseAtt = 5
    baseDef = 1
    asb = 1 #adjective set bonus
    nsb = 1 #noun set bonus
    osb = 1 #of set bonus


    att = a*((asb*adjAtt) + (nsb*nounsAtt) + (osb*ofAtt) + baseAtt)
    defence = a*((asb*adjDef) + (nsb*nounsDef) + (osb*ofDef) + baseDef)
    print("att:{} def:{} ".format(att, defence))
"""