import random, os, json, time, math
from convertexcel import playerStatCalc, Item, allitBonus, myItem

os.system('cls')


playing = True
mainMenu = True
shop = False
battle = False
out = False
money = 100000000
nav = 0



def shopDisp(item):
    w = 20
    print(item[0].ljust(w), item[1].ljust(w), item[2].ljust(w), "\n\n" + '1 [3g]'.ljust(w),'2 [3g]'.ljust(w),'3 [3g]'.ljust(w), '\n' '|_______________________________________________| 4 [1g]')



class Enemy:
    def __init__(self, level):
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


newenemy = Enemy(1)
pc = Player()

def Screen():
    os.system('cls')

def uiTop():
    print("gold: " + str(money))
    print(myItem.getList())
    if allitBonus(myItem):
        print('alliteration bonus!!')
    #print(playing, mainMenu, shop, battle, nav)
    playerStatCalc(myItem)
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
    

#main playing loop
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
        shopDisp(myItem.getList())
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
            shopDisp(myItem.getList())
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
            shopDisp(myItem.getList())
            uiBot(infoText)
            input()

    while battle:
        i = 1
        combo = 0
        newenemy = Enemy(i)

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
                newenemy = Enemy(i)
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