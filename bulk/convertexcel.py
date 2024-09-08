import pandas as pd
import json


elements = ["adjectives", "nouns", "of"]
resourcesPath = "C:/Users/fires/OneDrive/Documents/Programming/blank blank of blank/bbob/resources/"

def loadResources():

    convertExcelSheetIntoJson("adjectives")
    convertExcelSheetIntoJson("nouns")
    convertExcelSheetIntoJson("of")



    # for i in elements:
    #     file = open(elements[i]+".json", "w")
    #     hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=elements[i],index_col=0)
    #     file.write(hold.to_json())
    #     file.close()
    
    # file = open("nouns.json", "w")
    # nouns = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name='nouns',index_col=0)
    # output2 = nouns.to_json()
    # file.write(output2)
    # file.close()

    # file = open("of.json", "w")
    # of = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name='of',index_col=0)
    # output3 = of.to_json()
    # file.write(output3)
    # file.close()





def convertExcelSheetIntoJson(sheetName):
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    print("done")


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