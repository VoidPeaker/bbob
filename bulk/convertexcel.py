import pandas as pd
import json, random


elements = ["adjectives", "nouns", "of"]
resourcesPath = "C:/Users/fires/OneDrive/Documents/Programming/blank blank of blank/bbob/resources/"


class jsonRepo:
    wordJson = json
    wordProb = []
    wordList = []
    def __init__(self, inputFile):
        self.wordJson = inputFile
        for i in self.wordJson:
            self.wordProb.append(self.wordJson[i]['rollWeight'])
            self.wordList.append(i)
    
    def getRandomWord(self):
        word = random.choices(self.wordList, self.wordProb)

        
    # for i in nounsRepo:
    #     nounsProb.append(nounsRepo[i]['weight'])
    #     nounsList.append(i)
    # for i in ofRepo:
    #     ofProb.append(ofRepo[i]['weight'])
    #     ofList.append(i)





adjRepo = jsonRepo()

# adjClass.weight(thisItem)

def loadResources():

    adjRepo = jsonRepo(convertExcelSheetIntoJson("adjectives")) #at the same time converting the excell worksheet into the json and setting the json file to be accesses from the rest of this program
    nounsRepo = convertExcelSheetIntoJson("nouns")
    ofRepo = convertExcelSheetIntoJson("of")

    
    


def convertExcelSheetIntoJson(sheetName):
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    return json.load(sheetName+".json")


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