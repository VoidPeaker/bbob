import pandas as pd
import json, random

exItem = []
resourcesPath = "../bbob/resources/"

def Replace(list, i, string):
    list.pop(i)
    list.insert(i, "{}".format(string))
    return list

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

adjPool = []
nounPool = []
ofPool = []
adjRarity = []
nounRarity = []
ofRarity = []

for i in adjJson:
    adjPool.append(i)
    adjRarity.append(adjJson[i]['rollWeight'])
for i in nounJson:
    nounPool.append(i)
    nounRarity.append(nounJson[i]['rollWeight'])
for i in ofJson:
    ofPool.append(i)
    ofRarity.append(ofJson[i]['rollWeight'])



class Item:
    def __init__(self):
        #initialize list
        self.list = ["NULL", "NULL", "NULL"]

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
            adj = random.choices(adjPool, adjRarity)
            Replace(self.list, 0, adj[0]) #replace function removes previous list element and adds the list element from line above
        elif nav == 2:
            noun = random.choices(nounPool, nounRarity)
            Replace(self.list, 1, noun[0])
        elif nav == 3:
            of = random.choices(ofPool, ofRarity)
            Replace(self.list, 2, of[0])
        elif nav == 4:
            adj = random.choices(adjPool, adjRarity)
            noun = random.choices(nounPool, nounRarity)
            of = random.choices(ofPool, ofRarity)
            Replace(self.list, 0, adj[0])
            Replace(self.list, 1, noun[0])
            Replace(self.list, 2, of[0])

    # def roll(shopItem, nav, myItem):

    #     #shopItem n = list of the elements 
    #     #nav = which option is selected
    #     #myItem = players item 




    #     #reroll individual values based on nav from the menu
    #     if nav == 1:#set current shop item value to the myitem value
    #         Replace(myItem, 0, shopItem[0])
    #     elif nav == 2:
    #         Replace(myItem, 1, shopItem[1])
    #     elif nav == 3:
    #         Replace(myItem, 2, shopItem[2])
    #     elif nav == 4: #reroll only the shop
    #         adj = random.choices(adjPool, adjRarity)
    #         noun = random.choices(nounPool, nounRarity)
    #         of = random.choices(ofPool, ofRarity)
    #         Replace(shopItem, 0, adj[0])
    #         Replace(shopItem, 1, noun[0])
    #         Replace(shopItem, 2, of[0])

    def initRoll(self):
        adj = random.choices(adjPool, adjRarity)
        noun = random.choices(nounPool, nounRarity)
        of = random.choices(ofPool, ofRarity)
        Replace(self.list, 0, adj[0])
        Replace(self.list, 1, noun[0])
        Replace(self.list, 2, of[0])


    def toReadable(self):
        s = self.list[0] + " " + self.list[1] + " " + self.list[2]
        return s
    
    def getList(self):
        return self.list


myItem = Item()
shopItem = Item()
myItem.roll(4)
shopItem.roll(4)




    
def allitBonus(item):
    return item.getInfo('adj', 'firstLetter') == item.getInfo('noun', 'firstLetter') == item.getInfo('of', 'firstLetter')


def playerStatCalc(item): #is list rn
    #attack
    adjAtt = item.getInfo('adj', 'att')
    nounsAtt = item.getInfo('noun', 'att')
    ofAtt = item.getInfo('of', 'att')
    #def
    adjDef = item.getInfo('adj', 'def')
    nounsDef = item.getInfo('noun', 'def')
    ofDef = item.getInfo('of', 'def')
    #speed
    adjSpd = item.getInfo('adj', 'speed')
    nounsSpd = item.getInfo('noun', 'speed')
    ofSpd = item.getInfo('of', 'speed')

    a = 1 #alliteration bonus
    if allitBonus(item):
        a = 2
    baseAtt = 5
    baseDef = 1
    aab=1
    adb=1
    asb = 1 #adjective attack bonus, adjective defense bonus, adjective speed bonus
    nab=1
    ndb=1
    nsb = 1 #noun set bonus
    oab =1
    odb=1
    osb = 1 #of set bonus

    att = a*((aab*adjAtt) + (nab*nounsAtt) + (oab*ofAtt) + baseAtt)
    defence = a*((adb*adjDef) + (ndb*nounsDef) + (odb*ofDef) + baseDef)
    speed = a*(int((asb*adjSpd)) + int((nsb*nounsSpd)) + (osb*ofSpd)+1)
    stats = [att, defence, speed]
    return stats

#print(playerStatCalc(myItem))