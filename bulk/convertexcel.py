import pandas as pd
import json

elements = ["adjectives", "nouns", "of"]
resourcesPath = "../bbob/resources/"

def convertExcelSheetIntoJson(sheetName): #convert the main excel to needed json
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    hold2 = sheetName+".json"
    return json.load(open(hold2))

adjJson = convertExcelSheetIntoJson("adjectives") #at the same time converting the excel worksheet into the json and setting the json file to be accesses from the rest of this program
nounJson = convertExcelSheetIntoJson("nouns")
ofJson = convertExcelSheetIntoJson("of")

def getInfo(part, word, attr): #make it easier to call attributes of json file
    if part == 'adj':
        return adjJson[word[0]][attr]
    elif part == 'noun':
        return nounJson[word[1]][attr]
    elif part == 'of':
        return ofJson[word[2]][attr]
    
def allitBonus(item):
    return getInfo('adj', item, 'firstLetter') == getInfo('noun', item, 'firstLetter') == getInfo('of', item, 'firstLetter')

def playerStatCalc(item): #is list rn
    #attack
    adjAtt = getInfo('adj', item, 'att')
    nounsAtt = getInfo('noun', item, 'att')
    ofAtt = getInfo('of', item, 'att')
    #def
    adjDef = getInfo('adj', item, 'def')
    nounsDef = getInfo('noun', item, 'def')
    ofDef = getInfo('of', item, 'def')
    #speed
    adjSpd = getInfo('adj', item, 'speed')
    nounsSpd = getInfo('noun', item, 'speed')
    ofSpd = getInfo('of', item, 'speed')

    a = 1 #alliteration bonus
    if allitBonus(item):
        a = 2
    baseAtt = 5
    baseDef = 1
    asb = 1 #adjective set bonus
    nsb = 1 #noun set bonus
    osb = 1 #of set bonus

    att = a*((asb*adjAtt) + (nsb*nounsAtt) + (osb*ofAtt) + baseAtt)
    defence = a*((asb*adjDef) + (nsb*nounsDef) + (osb*ofDef) + baseDef)
    speed = a*((asb*adjSpd) + (nsb*nounsSpd) + (osb*ofSpd)+1)
    print("att:{} def:{} speed:{}".format(att, defence, speed))
