import pandas as pd
import json, random

exItem = []
resourcesPath = "../bbob/resources/"

adjPool = []
nounPool = []
ofPool = []

def convertExcelSheetIntoJson(sheetName): #convert the main excel to needed json
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    hold2 = sheetName+".json"
    return json.load(open(hold2))



def Replace(list, i, string):
    list.pop(i)
    list.insert(i, "{}".format(string))
    return list

adjJson = convertExcelSheetIntoJson("adjectives") #at the same time converting the excel worksheet into the json and setting the json file to be accesses from the rest of this program
nounJson = convertExcelSheetIntoJson("nouns")
ofJson = convertExcelSheetIntoJson("of")

for i in adjJson:
    adjPool.append(i)
for i in nounJson:
    nounPool.append(i)
for i in ofJson:
    ofPool.append(i)


class Item:
    def __init__(self):
        #initialize list
        self.list = ["fearful", "helmet", "________"]

    def getInfo(self, word, attr): #self = list that contains item elements, word = which of the three words, attr = what attribute to return from the json file
        if word == "adj":
            return adjJson[self.list[0]][attr]
        elif word == "noun":
            return nounJson[self.list[1]][attr]
        elif word == "of":
            return ofJson[self.list[2]][attr] 

    def roll(self, nav):
        #reroll individual values based on nav from the menu
        if nav == 1:
            adj = random.choices(Item.getInfo(''))
            Replace(self.list, 0, adj[0]) #replace function removes previous list element and adds the list element from line above
        elif nav == 2:
            noun = random.choices(nounsList, nounsProb)
            noun = nounRepo.getRandomNoun()
            Replace(self.list, 1, noun[0])
        elif nav == 3:
            of = random.choices(ofList, ofProb)
            of = ofRepo.getRandomOf()
            Replace(self.list, 2, of[0])
        elif nav == 4:
            adj = adjJson.getRandomAdj()
            noun = random.choices(nounsList, nounsProb)
            of = random.choices(ofList, ofProb)
            Replace(self.list, 0, adj[0])
            Replace(self.list, 1, noun[0])
            Replace(self.list, 2, of[0])          
        else:
            print("bozo")

    def toReadable(self):
        s = self.list[0] + " " + self.list[1] + " " + self.list[2]
        return s

exItem = Item()

print(exItem.getInfo('adj', 'firstLetter'))
        

    
# def allitBonus(item):
#     return getInfo('adj', item, 'firstLetter') == getInfo('noun', item, 'firstLetter') == getInfo('of', item, 'firstLetter')


# def playerStatCalc(item): #is list rn
#     #attack
#     adjAtt = getInfo(item, 'att')
#     nounsAtt = getInfo(item, 'att')
#     ofAtt = getInfo(item, 'att')
#     #def
#     adjDef = getInfo('adj', item, 'def')
#     nounsDef = getInfo('noun', item, 'def')
#     ofDef = getInfo('of', item, 'def')
#     #speed
#     adjSpd = getInfo('adj', item, 'speed')
#     nounsSpd = getInfo('noun', item, 'speed')
#     ofSpd = getInfo('of', item, 'speed')

#     a = 1 #alliteration bonus
#     if allitBonus(item):
#         a = 2
#     baseAtt = 5
#     baseDef = 1
#     asb = 1 #adjective set bonus
#     nsb = 1 #noun set bonus
#     osb = 1 #of set bonus

#     att = a*((asb*adjAtt) + (nsb*nounsAtt) + (osb*ofAtt) + baseAtt)
#     defence = a*((asb*adjDef) + (nsb*nounsDef) + (osb*ofDef) + baseDef)
#     speed = a*((asb*adjSpd) + (nsb*nounsSpd) + (osb*ofSpd)+1)
