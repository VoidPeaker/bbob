import random, os, sys, json

#open documents
adjList = []
adjProb = []
adjFile = open('basic adj.json', "r")
adjRam = json.load(adjFile)
adjFile.close()

nounsList = []
nounsProb = []
nounsFile = open('basic nouns.json', "r")
nounsRam = json.load(nounsFile)
nounsFile.close()

ofList = []
ofProb = []
ofFile = open('basic of.json', "r")
ofRam = json.load(ofFile)
ofFile.close()

#savedItems = open("user saved.txt", "a+")

for i in adjRam:
    adjProb.append(adjRam[i]['weight'])
    adjList.append(i)
for i in nounsRam:
    nounsProb.append(nounsRam[i]['weight'])
    nounsList.append(i)
for i in ofRam:
    ofProb.append(ofRam[i]['weight'])
    ofList.append(i)

os.system('cls')


playing = True
mainMenu = True
shop = False
battle = False
out = False
money = 100000000
nav = 0

def Replace(list, i, string):
    list.pop(i)
    list.insert(i, "{}".format(string))
    return list

def shopDisp(items):
    w = 20
    print(items[0].ljust(w), items[1].ljust(w), items[2].ljust(w), "\n\n" + '1 [3g]'.ljust(w),'2 [3g]'.ljust(w),'3 [3g]'.ljust(w), '\n' '|_______________________________________________| 4 [1g]')

def allitBonus(self):
    return adjRam['{}'.format(self[0])]['firstLetter'] == nounsRam['{}'.format(self[1])]['firstLetter'] == ofRam['{}'.format(self[2])]['firstLetter']

def playerStatCalc(self): #is list rn
    adjHp = adjRam['{}'.format(self[0])]['hp']
    nounsHp = nounsRam['{}'.format(self[1])]['hp']
    ofHp = ofRam['{}'.format(self[2])]['hp']
    adjDef = adjRam['{}'.format(self[0])]['def']
    nounsDef = nounsRam['{}'.format(self[1])]['def']
    ofDef = ofRam['{}'.format(self[2])]['def']
    a = 1 #alliteration bonus
    if allitBonus(self):
        a = 2
    baseHp = 1
    baseDef = 1
    asb = 1 #adjective set bonus
    nsb = 1 #noun set bonus
    osb = 1 #of set bonus


    hp = a*((asb*adjHp) + (nsb*nounsHp) + (osb*ofHp) + baseHp)
    defence = a*((asb*adjDef) + (nsb*nounsDef) + (osb*ofDef) + baseDef)
    print("hp:{} def:{} ".format(hp, defence))


class Item:
    def __init__(self):
        #initialize list
        self.itemElements = ["NULL 1","NULL 2","NULL 3"]
        adj = random.choice(adjList)
        noun = random.choice(nounsList)


    def roll(self, ans):
        #reroll individual values based on ans from the menu
        if ans == 1:
            adj = random.choices(adjList, adjProb) #
            Replace(self.itemElements, 0, adj[0]) #replace function removes previous list element and adds the list element from line above
        elif ans == 2:
            noun = random.choices(nounsList, nounsProb)
            Replace(self.itemElements, 1, noun[0])
        elif ans == 3:
            of = random.choices(ofList, ofProb)
            Replace(self.itemElements, 2, of[0])
        elif ans == 4:
            adj = random.choices(adjList, adjProb)
            noun = random.choices(nounsList, nounsProb)
            of = random.choices(ofList, ofProb)
            Replace(self.itemElements, 0, adj[0])
            Replace(self.itemElements, 1, noun[0])
            Replace(self.itemElements, 2, of[0])          
        else:
            print("bozo")


    def toReadable(self):
        s = self.itemElements[0] + " " + self.itemElements[1] + " " + self.itemElements[2]
        return s

myItem = Item()
myItem.roll(4)

def Screen():
    os.system('cls')

def uiTop():
    print("gold: " + str(money))
    print(myItem.toReadable())
    if allitBonus(myItem.itemElements):
        print('alliteration bonus!!')
    #print(playing, mainMenu, shop, battle, nav)
    playerStatCalc(myItem.itemElements)
    print("\n---------------------------------------------\n")
def uiBot(thisText = "> "):
    print("\n---------------------------------------------\n")
    print("{}".format(thisText))
def menu1():
    print("""please make a selection
1. start
2. battle
3. quit
          """)






while playing:
    while mainMenu:
        Screen()
        nav = 0
        ans=0
        uiTop()
        menu1()
        uiBot()
        nav = int(input())
        if nav == 1:
            mainMenu = False
            shop = True
        elif nav == 2:
            mainMenu = False
            battle = True
        elif nav == 3:
            out = True
            mainMenu = False


    while shop:
        Screen()
        nav = 0
        infoText = "Please make a selection to re-roll that aspect!\n5 to go back to the main menu\n6 to save current item to hall of fame"
        uiTop()
        shopDisp(myItem.itemElements)
        uiBot(infoText)
        ans = int(input())
        if (ans == 1 or ans == 2 or ans == 3) and (money >= 3): #money-3 == 0?
            money -= 3
            Screen()
            myItem.roll(ans)

        elif (ans == 4) and (money >= 1):
            money = money - 1
            Screen()
            myItem.roll(ans)

        elif (ans == 1 or ans == 2 or ans == 3 or ans == 4) and (money - 3 <= 0):
            Screen()
            infoText = "not enough money!"

        elif ans == 5:
            Screen()
            infoText = "1. main menu\n2. battle screen"
            uiTop()
            shopDisp(myItem.itemElements)
            uiBot(infoText)
            nav = int(input())
            if nav == 1:
                mainMenu = True
                shop = False
            elif nav == 2:
                shop = False
                battle = True
        elif ans == 6:
            Screen()
            with open("user saved.txt", "a+") as file:
                file.write("\n" + myItem.toReadable())
            #savedItems.write("{}".format(myItem.toReadable()))
            infoText = "Saved!"
            uiTop()
            shopDisp(myItem.itemElements)
            uiBot(infoText)

            
        
               

    while battle:
        nav = 0
        uiTop()
        print("this is the battle\n1. go back")
        uiBot()
        nav = int(input())
        if nav == 1:
            battle = False
            mainMenu = True
        os.system('cls')
        

    while out:
        nav = 0
        uiTop()
        print('are you sure?')
        uiBot()
        nav = int(input())
        if nav == 1:
            exit()
        elif nav == 0:
            mainMenu = True
            out = False