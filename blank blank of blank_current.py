import random, os, json, time, math
# from convertexcel import loadResources, resourcesPath

# loadResources()
# resourcesPath

#open documents
adjList = []
adjProb = []
adjFile = open('adjectives.json', "r")
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
    adjProb.append(adjRam[i]['rollWeight'])
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
    #attack
    adjAtt = adjRam['{}'.format(self[0])]['att']
    nounsAtt = nounsRam['{}'.format(self[1])]['att']
    ofAtt = ofRam['{}'.format(self[2])]['att']
    #defence
    adjDef = adjRam['{}'.format(self[0])]['def']
    nounsDef = nounsRam['{}'.format(self[1])]['def']
    ofDef = ofRam['{}'.format(self[2])]['def']
    #speed
    adjSpd = adjRam['{}'.format(self[0])]['speed']
    nounsSpd = nounsRam['{}'.format(self[1])]['speed']
    ofSpd = ofRam['{}'.format(self[2])]['speed']

    a = 1 #alliteration bonus
    if allitBonus(self):
        a = 2
    baseAtt = 5
    baseDef = 1
    asb = 1 #adjective set bonus
    nsb = 1 #noun set bonus
    osb = 1 #of set bonus


    att = a*((asb*adjAtt) + (nsb*nounsAtt) + (osb*ofAtt) + baseAtt)
    defence = a*((asb*adjDef) + (nsb*nounsDef) + (osb*ofDef) + baseDef)
    print("att:{} def:{} ".format(att, defence))


class Item:
    def __init__(self):
        #initialize list
        self.itemElements = ["NULL 1","NULL 2","NULL 3"]
        adj = random.choice(adjList)
        noun = random.choice(nounsList)


    def roll(self, nav):
        #reroll individual values based on nav from the menu
        if nav == 1:
            adj = random.choices(adjList, adjProb) #
            Replace(self.itemElements, 0, adj[0]) #replace function removes previous list element and adds the list element from line above
        elif nav == 2:
            noun = random.choices(nounsList, nounsProb)
            Replace(self.itemElements, 1, noun[0])
        elif nav == 3:
            of = random.choices(ofList, ofProb)
            Replace(self.itemElements, 2, of[0])
        elif nav == 4:
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

class Enemy:
    def __init__(self):
        pass

    def makeEnemy(self, level):
        baseHp = 5
        baseDef = 5
        baseAtt = 1
        firstName = ['charles', 'david', 'glorbo', 'greepus', 'grabon', 'flub', 'grub', 'graham', 'greebs', 'bunkle', 'bonkle', 'bunkis', 'nunkis', 'charles']    
        lastName = ['the strange', 'beepy, the eepy deepy zeepy' , 'the younger', 'the older', 'greepus', 'the sleepy', '', '', '', '', '', '', 'smith', 'agnew']
        self.name = random.choice(firstName) + " " + random.choice(lastName)
        self.hp = baseHp + len(self.name) + math.ceil(level*1.5)
        self.defence = baseDef + (level * random.choice(range(2,4)))
        self.att = baseAtt + level + (level * random.choice(range(2,4)))

    def damage(self, itemDamage):
        if itemDamage - self.defence > 0:
            self.hp = self.hp - (itemDamage - self.defence)
        else:
            self.hp = self.hp - 1

class Player:

    def __init__(self):
        self.itemDamage = 5
        self.playerHp = 15
        self.playerDefence = 5


    def damagePlayer(self, enemyDamage):
        if enemyDamage - self.playerDefence > 0:
            self.playerHp = self.playerHp - (enemyDamage - self.playerDefence)

myItem = Item()
myItem.roll(4)
newenemy = Enemy()
newenemy.makeEnemy(1)
pc = Player()

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
        nav=0
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
        nav = int(input())
        if (nav == 1 or nav == 2 or nav == 3) and (money >= 3): #money-3 == 0?
            money -= 3
            Screen()
            myItem.roll(nav)

        elif (nav == 4) and (money >= 1):
            money = money - 1
            Screen()
            myItem.roll(nav)

        elif (nav == 1 or nav == 2 or nav == 3 or nav == 4) and (money - 3 <= 0):
            Screen()
            infoText = "not enough money!\n enter to continue"
            input()

        elif nav == 5:
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
        elif nav == 6:
            Screen()
            with open("user saved.txt", "a+") as file:
                file.write("\n" + myItem.toReadable())
            #savedItems.write("{}".format(myItem.toReadable()))
            infoText = "Saved!"
            uiTop()
            shopDisp(myItem.itemElements)
            uiBot(infoText)
            input()

    while battle:
        i = 1
        combo = 0
        newenemy.makeEnemy(i)

        nav = int(input())
        if nav == 1:
            attack = True
            print('{} attacks!!!!!! he has {} health and {} defence!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defence))
        elif nav == 2:
            battle = False
            shop = True
        while attack:
            if newenemy.hp - pc.itemDamage <= 0:
                os.system('cls')
                print("enemies beaten: {}\nitem attack: {}\ncurrent health: {}".format(combo, pc.itemDamage, pc.playerHp)) 
                print("you won!")
                input()
                newenemy.makeEnemy(i)
                print('uh oh!\n{} attacks!!!!!! he has {} health and {} defence!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defence))
                combo +=1
                i += 1
                pc.itemDamage += 1
                input()
            
            elif pc.playerHp - newenemy.att <= 0:
                os.system('cls')
                print('you died!')
                input()
                battle = False
                Shop = True

            
            else:
                os.system('cls')
                print("enemies beaten: {}\nitem attack: {}\ncurrent health: {}".format(combo, pc.itemDamage, pc.playerHp))
                newenemy.damage(pc.itemDamage)
                pc.damagePlayer(newenemy.att)
                print("{}'s current health is {} with defence {}".format(newenemy.name, newenemy.hp, newenemy.defence))
                input()
                





            # nav = 0
            # uiTop()
            # print("this is the battle\n1. go back")
            # uiBot()
            # nav = int(input())
            # if nav == 1:
            #     battle = False
            #     mainMenu = True
            # os.system('cls')
            
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