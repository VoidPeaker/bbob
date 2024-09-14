import random, os, json, time, math, pygame
from convertexcel import playerStatCalc, Item, allitBonus, myItem



mainMenu = True
shop = False
battle = False
out = False
money = 100000000
nav = 0
currentPosition = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1210, 633))
clock = pygame.time.Clock()
playing = True

# initialize font
fontSize = 25
font = pygame.font.SysFont("lucidaconsole", fontSize)


# set colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# declaring the list that will contain the visible lines of text
numLines = 24
lineWidth = 80
visibleText = []
for i in range(numLines):
    visibleText.append("".ljust(lineWidth))

# function to print a line to the terminal window
def printToTerminal(newLine):
    #print(newLine)
    visibleText.pop(0) # remove the oldest line
    visibleText.append(newLine.ljust(80))

def clearTerminal():
    #os.system('cls')
    for i in range(numLines):
        visibleText.pop(0)
        visibleText.append("".ljust(lineWidth))


def shopDisp(item, currentPosition):
    w = 20
    if currentPosition == 0:
        printToTerminal('')
        printToTerminal(item[0].ljust(w) + item[1].ljust(w) + item[2].ljust(w))
        printToTerminal('')
        printToTerminal('')
        printToTerminal('[1] 3g'.ljust(w) + '2 3g'.ljust(w) + '3 3g'.ljust(w))
        printToTerminal('|_______________________________________________| 4 1g')
        printToTerminal('')
        printToTerminal('5 to Main Menu')
    elif currentPosition == 1:
        printToTerminal('')
        printToTerminal(item[0].ljust(w) + item[1].ljust(w) + item[2].ljust(w))
        printToTerminal('')
        printToTerminal('')
        printToTerminal('1 3g'.ljust(w) + '[2] 3g'.ljust(w) + '3 3g'.ljust(w))
        printToTerminal('|_______________________________________________| 4 1g')
        printToTerminal('')
        printToTerminal('5 to Main Menu')
    elif currentPosition == 2:
        printToTerminal('')
        printToTerminal(item[0].ljust(w) + item[1].ljust(w) + item[2].ljust(w))
        printToTerminal('')
        printToTerminal('')
        printToTerminal('1 3g'.ljust(w) + '2 3g'.ljust(w) + '[3] 3g'.ljust(w))
        printToTerminal('|_______________________________________________| 4 1g')
        printToTerminal('')
        printToTerminal('5 to Main Menu')
    elif currentPosition == 3:
        printToTerminal('')
        printToTerminal(item[0].ljust(w) + item[1].ljust(w) + item[2].ljust(w))
        printToTerminal('')
        printToTerminal('')
        printToTerminal('1 3g'.ljust(w) + '2 3g'.ljust(w) + '3 3g'.ljust(w))
        printToTerminal('|_______________________________________________| [4] 1g')
        printToTerminal('')
        printToTerminal('5 to Main Menu')
    elif currentPosition == 4:
        printToTerminal('')
        printToTerminal(item[0].ljust(w) + item[1].ljust(w) + item[2].ljust(w))
        printToTerminal('')
        printToTerminal('')
        printToTerminal('1 3g'.ljust(w) + '2 3g'.ljust(w) + '3 3g'.ljust(w))
        printToTerminal('|_______________________________________________| 4 1g')
        printToTerminal('')
        printToTerminal('[5] to Main Menu')


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

#def Screen():
#    os.system('cls')

def uiTop():
    printToTerminal("gold: " + str(money))
    printToTerminal(myItem.toReadable())
    if allitBonus(myItem):
        printToTerminal('alliteration bonus!!')
    #printToTerminal(playing, mainMenu, shop, battle, nav)
    playerStatCalc(myItem)
    printToTerminal("---------------------------------------------")
def uiBot(thisText = "> "):
    printToTerminal("---------------------------------------------")
    #printToTerminal("{}".format(thisText))
def menu1(currentPosition):
    printToTerminal("please make a selection")
    if(currentPosition == 0):
        printToTerminal("[1] start")
        printToTerminal(" 2. battle")
        printToTerminal(" 3. quit")
    elif (currentPosition == 1):
        printToTerminal(" 1. start")
        printToTerminal("[2] battle")
        printToTerminal(" 3. quit")
    elif (currentPosition == 2):
        printToTerminal(" 1. start")
        printToTerminal(" 2. battle")
        printToTerminal("[3] quit")
    


#main playing loop
while playing:

    # poll for events
    events = pygame.event.get()
    # pygame.QUIT event means the user clicked X to close your window
    for event in events:
        if event.type == pygame.QUIT:
            playing = False

    screen.fill(BLACK)

    clearTerminal()

    uiTop()
    menu1(currentPosition)
    uiBot()
    
    # if we're in the main menu
    if mainMenu: 
        clearTerminal()
        nav=0
        
        uiTop() #print the UI
        menu1(currentPosition)
        uiBot()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    currentPosition = (currentPosition - 1) % 3
                elif event.key == pygame.K_DOWN:
                    currentPosition = (currentPosition + 1) % 3
                if event.key == pygame.K_RETURN:
                    nav = currentPosition + 1

        

        # if it's 1, 2, or 3, we move to a different screen
        if nav == 1:
            mainMenu = False
            nav = 0
            shop = True

        elif nav == 2:
            mainMenu = False
            battle = True
            nav = 0
        elif nav == 3:
            out = True
            mainMenu = False
            nav = 0

    elif shop:
        clearTerminal()

        infoText = "Please make a selection to re-roll that aspect!\n5 to go back to the main menu\n6 to save current item to hall of fame"
        uiTop()
        shopDisp(myItem.getList(), currentPosition)
        uiBot(infoText)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentPosition = (currentPosition - 1) % 5
                elif event.key == pygame.K_RIGHT:
                    currentPosition = (currentPosition + 1) % 5
                if event.key == pygame.K_RETURN:
                    nav = currentPosition + 1

        if (nav == 1 or nav == 2 or nav == 3) and (money >= 3): #money-3 == 0?
            money -= 3
            clearTerminal()
            myItem.roll(nav)
            nav = 0

        elif (nav == 4) and (money >= 1):
            money = money - 1
            clearTerminal()
            myItem.roll(nav)
            nav = 0

        elif (nav == 1 or nav == 2 or nav == 3 or nav == 4) and (money - 3 <= 0):
            clearTerminal()
            infoText = "not enough money!\n enter to continue"
            input()

        elif nav == 5:
            mainMenu = True
            shop = False
            currentPosition = 0
            nav = 0

        elif nav == 6:
            clearTerminal()
            with open("user saved.txt", "a+") as file:
                file.write("\n" + myItem.toReadable())
            #savedItems.write("{}".format(myItem.toReadable()))
            infoText = "Saved!"
            uiTop()
            shopDisp(myItem.getList())
            uiBot(infoText)
            input()



    elif battle:
        i = 1
        combo = 0
        newenemy = Enemy(i)
        nav = 0

        #nav = int(input())
        if nav == 1:
            attack = True
            printToTerminal('{} attacks!!!!!! he has {} health and {} defence!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defence))
        elif nav == 2:
            battle = False
            shop = True
        elif attack:
            if newenemy.hp - pc.itemDamage <= 0:
                clearTerminal()
                printToTerminal("enemies beaten: {}\nitem attack: {}\ncurrent health: {}".format(combo, pc.itemDamage, pc.playerHp)) 
                printToTerminal("you won!")
                input()
                newenemy = Enemy(i)
                printToTerminal('uh oh!\n{} attacks!!!!!! he has {} health and {} defence!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defence))
                combo +=1
                i += 1
                pc.itemDamage += 1
                input()
            
            elif pc.playerHp - newenemy.att <= 0:
                clearTerminal()
                printToTerminal('you died!')
                input()
                battle = False
                Shop = True

            
            else:
                clearTerminal()
                printToTerminal("enemies beaten: {}\nitem attack: {}\ncurrent health: {}".format(combo, pc.itemDamage, pc.playerHp))
                newenemy.damage(pc.itemDamage)
                pc.damagePlayer(newenemy.att)
                printToTerminal("{}'s current health is {} with defence {}".format(newenemy.name, newenemy.hp, newenemy.defence))
                input()
            
    elif out:
        nav = 1
        uiTop()
        printToTerminal('are you sure?')
        uiBot()
        #nav = int(input())
        if nav == 1:
            exit()
        elif nav == 0:
            mainMenu = True
            out = False


   
    # draw visible text to pygame  
    height = 5
    
    for line in visibleText:
        #print(line)
        img = font.render(line, True, GREEN)
        #rect = img.get_rect()
        #pygame.draw.rect(img, RED, rect, 1)
        screen.blit(img, (5, height))
        height = height + fontSize + 1

    # flip() the display to put your work on screen
    pygame.display.flip()