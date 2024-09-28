import random, math, pygame, time, sys
from itemDeclaration import *
from setBonuses import *

mainMenu = True
shop = False
battle = False
out = False
money = 100
nav = 0
currentPosition = 0
clearing = 0
fighting = False
_index = 0
subMenu = False
turns = 0
clearing = 1 #this is the enemy level, but i realized it was going up one per location, so it also equals clearing
escapeCost = 1
dead = False
fullHealth = 0
speed = 1/25
hasNewEnemy = False

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

def writeAnim(text, speed):
    for character in text:
        visibleText.append("{}".format(character))
        time.sleep(speed)

def loopDelay(text = '. . . . ', speed = .1):
    speed = .2
    while True:
        #print('looped {} times'.format(loopCount))
        writeAnim('. . . . . ', speed)
        speed1 = speed1 - speed1/20

def shopDisp(item1, item2, currentPosition): #menu animation
    w = 22
    printToTerminal('make a selection:')
    printToTerminal('')
    printToTerminal(item1[0].ljust(w) + item1[1].ljust(w) + item1[2].ljust(w))


    if currentPosition == 6:
        printToTerminal('[7] '.ljust(w) + ' 8 '.ljust(w) + ' 9 '.ljust(w) + ' exit')

    elif currentPosition == 7:
        printToTerminal(' 7 '.ljust(w) + '[8] '.ljust(w) + ' 9 '.ljust(w) + ' exit')

    elif currentPosition == 8:
        printToTerminal(' 7 '.ljust(w) + ' 8 '.ljust(w) + '[9] '.ljust(w) + ' exit')

    elif currentPosition == 9:
        printToTerminal(' 7 '.ljust(w) + ' 8 '.ljust(w) + ' 9  '.ljust(w) + '[exit]')
    else:
        printToTerminal(' 7 '.ljust(w) + ' 8 '.ljust(w) + ' 9 '.ljust(w) + ' exit')

    printToTerminal('')
    printToTerminal(item2[0].ljust(w) + item2[1].ljust(w) + item2[2].ljust(w))


    if currentPosition == 3:
        printToTerminal('[4] '.ljust(w) + ' 5 '.ljust(w) + ' 6 '.ljust(w))

    elif currentPosition == 4:
        printToTerminal(' 4 '.ljust(w) + '[5] '.ljust(w) + ' 6 '.ljust(w))

    elif currentPosition == 5:
        printToTerminal(' 4 '.ljust(w) + ' 5 '.ljust(w) + '[6] '.ljust(w))

    else:
        printToTerminal(' 4 '.ljust(w) + ' 5 '.ljust(w) + ' 6 '.ljust(w))

    printToTerminal("")

    if currentPosition == 0:
        printToTerminal('[reroll!] 3g'.ljust(w) + ' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w))
        printToTerminal('                                                            0  1g')
    elif currentPosition == 1:
        printToTerminal(' reroll!  3g'.ljust(w) + '[reroll!] 3g'.ljust(w) + ' reroll!  3g'.ljust(w))
        printToTerminal('                                                            0  1g')
    elif currentPosition == 2:
        printToTerminal(' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w) + '[reroll!] 3g'.ljust(w))
        printToTerminal('                                                            0  1g')
    elif currentPosition == 99:
        printToTerminal(' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w))
        printToTerminal('                                                           [0] 1g')
    else:
        printToTerminal(' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w) + ' reroll!  3g'.ljust(w))
        printToTerminal('                                                            0  1g')

class Enemy:
    def __init__(self, level):
        baseHp = 5
        baseDef = 5
        baseAtt = 1
        firstName = ['charles', 'david', 'glorbo', 'greepus', 'grabon', 'flub', 'grub', 'graham', 'greebs', 'bunkle', 'bonkle', 'bunkis', 'nunkis', 'charles']    
        lastName = ['the strange', 'beepy, the eepy deepy zeepy' , 'the younger', 'the older', 'greepus', 'the sleepy', '', '', '', '', '', '', 'smith', 'agnew']
        self.name = random.choice(firstName) + " " + random.choice(lastName)
        self.hp = baseHp + len(self.name) + math.ceil(level*1.5)
        self.defense = baseDef + (level * random.choice(range(2,4)))
        self.att = baseAtt + level + (level * random.choice(range(2,4)))
        self.gold = (level * random.choice(range(2,4))) + math.ceil(len(self.name)/3)

    def damage(self, itemDamage):
        if itemDamage - self.defense > 0:
            self.hp = self.hp - (itemDamage - self.defense)
        else:
            self.hp = self.hp - 1

class Player:
    def __init__(self):
        self.itemDamage = playerStatCalc(myItem)[0]
        self.playerHp = 5+(clearing+playerStatCalc(myItem)[1]/2)
        self.playerDefense = playerStatCalc(myItem)[2]


    def damagePlayer(self, enemyDamage):
        if enemyDamage - self.playerDefense > 0:
            self.playerHp = self.playerHp - (enemyDamage - self.playerDefense)
        if self.playerHp < 0:
            self.playerHp = 0 

newenemy = Enemy(1)
pc = Player()

def uiTop():
    printToTerminal("gold: " + str(money))
    printToTerminal("nav:" + str(nav) + "currentPos:" + str(currentPosition))
    printToTerminal("")
    printToTerminal("hp: " + str(pc.playerHp))
    printToTerminal(myItem.toReadable())
    if battle:
        printToTerminal("clearing: " + str(clearing))
    if allitBonus(myItem):
        printToTerminal('alliteration bonus!!')
    printToTerminal(setBonus())
    #printToTerminal("attack: {}  defense: {}  speed: {}".format(playerStatCalc(myItem)[0], playerStatCalc(myItem)[1], playerStatCalc(myItem)[2]))
    printToTerminal("---------------------------------------------")
    

def uiBot(thisText = "> "):
    printToTerminal("---------------------------------------------")
    
    emptyLines = 0
    i = 0
    while i < len(visibleText):
        if visibleText[i] == "".ljust(lineWidth):
            visibleText.pop(i)
            emptyLines = emptyLines + 1
        else: i = i + 1
    for i in range(emptyLines):
        visibleText.append("".ljust(lineWidth))
    


def mainmenuUI(currentPosition):
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
    else:
        printToTerminal(" 1. start")
        printToTerminal(" 2. battle")
        printToTerminal("[3] quit")
    
def subMenuUI(currentPosition):
    w = 22
    if currentPosition == 0:
        printToTerminal('[yes]'.ljust(w) + ' no')
    elif currentPosition == 1:
        printToTerminal(' yes '.ljust(w) + '[no]')
    else:
        printToTerminal(' yes '.ljust(w) + '[no]')

def battleDisp(currentPosition):
    w = 20
    printToTerminal("what do you do?")
    if (currentPosition == 0):
        printToTerminal('[fight!]'.ljust(w) + ' run! {}g '.format(escapeCost))
    elif (currentPosition == 1):
        printToTerminal(' fight! '.ljust(w) + '[run! {}g]'.format(escapeCost))
    else:
        printToTerminal(' fight! '.ljust(w) + '[run! {}g]'.format(escapeCost))

#main playing loop
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while playing:
    # poll for events
    events = pygame.event.get()
    # pygame.QUIT event means the user clicked X to close your window
    for event in events:
        if event.type == pygame.QUIT:
            playing = False

    screen.fill(BLACK)

    if mainMenu: 
        clearTerminal()
        nav=0
        uiTop() #print the UI
        mainmenuUI(currentPosition)
        uiBot()
                                                                                                                                                                                                                                                                 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_UP):
                    currentPosition = (currentPosition - 1) % 5
                elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_DOWN):
                    currentPosition = (currentPosition + 1) % 5
                elif (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
                    currentPosition = 0
                elif (event.key == pygame.K_2) or (event.key == pygame.K_KP2):
                    currentPosition = 1
                elif (event.key == pygame.K_3) or (event.key == pygame.K_KP3):
                    currentPosition = 2
                elif (event.key == pygame.K_4) or (event.key == pygame.K_KP4):
                    currentPosition = 3
                elif (event.key == pygame.K_5) or (event.key == pygame.K_KP5):
                    currentPosition = 4
                elif (event.key == pygame.K_6) or (event.key == pygame.K_KP6):
                    currentPosition = 5
                elif (event.key == pygame.K_7) or (event.key == pygame.K_KP7):
                    currentPosition = 6
                elif (event.key == pygame.K_8) or (event.key == pygame.K_KP8):
                    currentPosition = 7
                elif (event.key == pygame.K_9) or (event.key == pygame.K_KP9):
                    currentPosition = 8
                elif (event.key == pygame.K_0) or (event.key == pygame.K_KP0):
                    currentPosition = 99
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1

        # if it's 1, 2, or 3, we move to a different screen
        if nav == 1:
            mainMenu = False
            shop = True
            nav = currentPosition = 0
        elif nav == 2:
            mainMenu = False
            battle = True
            newenemy = Enemy(clearing)
            nav = currentPosition = 0
        elif nav == 3:
            mainMenu = False
            out = True
            nav = currentPosition = 0

    elif shop:
        menuOptions = 10
        clearTerminal()
        
        uiTop()
        shopDisp(shopItem1.getList(), shopItem2.getList(), currentPosition) #sending the item string as it currently is, and the position of the highlighted number
        uiBot()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentPosition = (currentPosition - 1) % menuOptions
                elif event.key == pygame.K_RIGHT:
                    currentPosition = (currentPosition + 1) % menuOptions
                elif event.key == pygame.K_UP:
                    currentPosition = (currentPosition + 3) % menuOptions
                elif event.key == pygame.K_DOWN:
                    currentPosition = (currentPosition - 3) % menuOptions                                              
                elif (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
                    currentPosition = 0
                elif (event.key == pygame.K_2) or (event.key == pygame.K_KP2):
                    currentPosition = 1
                elif (event.key == pygame.K_3) or (event.key == pygame.K_KP3):
                    currentPosition = 2
                elif (event.key == pygame.K_4) or (event.key == pygame.K_KP4):
                    currentPosition = 3
                elif (event.key == pygame.K_5) or (event.key == pygame.K_KP5):
                    currentPosition = 4
                elif (event.key == pygame.K_6) or (event.key == pygame.K_KP6):
                    currentPosition = 5
                elif (event.key == pygame.K_7) or (event.key == pygame.K_KP7):
                    currentPosition = 6
                elif (event.key == pygame.K_8) or (event.key == pygame.K_KP8):
                    currentPosition = 7
                elif (event.key == pygame.K_9) or (event.key == pygame.K_KP9):
                    currentPosition = 8
                elif (event.key == pygame.K_0) or (event.key == pygame.K_KP0):
                    currentPosition = 99
                elif (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1

        if (nav == 4 or nav == 5 or nav == 6 or nav == 7 or nav == 8 or nav == 9) and (money -3 >= 0):
            itemNumber = nav
            nav = currentPosition = 0
            subMenu = True
        
        if (nav == 1 or nav == 2 or nav == 3) and (money >= 1) and not subMenu:
            money -= 1
            shopItem1.roll(nav)
            shopItem2.roll(nav)
            nav = currentPosition = 0

        if nav == 10 and not subMenu:
            nav = currentPosition = 0
            shop = False
            mainMenu = True

        elif (nav == 100 )and (money >= 4):
            money -= 4
            shopItem1.roll(4)
            shopItem2.roll(4)
            nav = currentPosition = 0

        elif nav == 10:
            nav = currentPosition = 0
            shop = False
            mainMenu = True

        elif subMenu:
            
            _index = 0 #initialize local variable to pass to either of the items that is being asked about
            if itemNumber == 7 or itemNumber == 4:
                _index = 0
                type = 'adj'
            if itemNumber == 8 or itemNumber == 5:
                _index = 1
                type = 'noun'
            if itemNumber == 9 or itemNumber == 6:
                _index = 2
                type = 'of'

            if itemNumber in range(7,10):
                clearTerminal()
                uiTop()
                printToTerminal(shopItem1.getList()[_index])
                printToTerminal(" ")
                printToTerminal("attack: {}  defense: {}  speed: {}".format((shopItem1.getInfo(type, "att")),
                                                                            (shopItem1.getInfo(type, "def")), 
                                                                            (shopItem1.getInfo(type, "speed"))))
                printToTerminal("set(s): {}".format(shopItem1.getInfo(type, "set")))
                printToTerminal(" ")
                printToTerminal("do you want to replace?")
                subMenuUI(currentPosition)
                uiBot()
                if nav == 1: #yes
                    money -= 4
                    Replace(myItem.getList(), _index, shopItem1.getList()[_index])
                    subMenu = False
                    shop = True
                    nav = currentPosition = 0
                elif nav == 2: #no
                    subMenu = False
                    shop = True
                    nav = currentPosition = 0


            elif itemNumber in range(4,7):
                clearTerminal()
                uiTop()
                printToTerminal(shopItem2.getList()[_index])
                printToTerminal(" ")
                printToTerminal("attack: {}  defense: {}  speed: {}".format((shopItem2.getInfo(type, "att")),
                                                                            (shopItem2.getInfo(type, "def")), 
                                                                            (shopItem2.getInfo(type, "speed"))))
                printToTerminal("set(s): {}".format(shopItem2.getInfo(type, "set")))
                printToTerminal(" ")
                printToTerminal("do you want to replace?")
                subMenuUI(currentPosition)
                uiBot()
                if nav == 1: #yes
                    money -= 4
                    Replace(myItem.getList(), _index, shopItem2.getList()[_index])
                    subMenu = False
                    shop = True
                    nav = currentPosition = 0
                elif nav == 2: #no
                    subMenu = False
                    shop = True
                    nav = currentPosition = 0

    elif battle:
        for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        currentPosition = (currentPosition - 1) % 2
                    elif event.key == pygame.K_RIGHT:
                        currentPosition = (currentPosition + 1) % 2
                    elif (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                        nav = currentPosition + 1
                    elif (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
                        currentPosition = 0
                    elif (event.key == pygame.K_2) or (event.key == pygame.K_KP2):
                        currentPosition = 1
        if pc.playerHp <= 0:
            dead = True
        
        if not fighting:
            clearTerminal()
            uiTop()
            printToTerminal('{} attacks!!!!!'.format(newenemy.name))
            printToTerminal("he has {} health, {} defense, {} gold!".format(newenemy.hp, newenemy.defense, newenemy.gold))
            printToTerminal("attack this enemy?")
            subMenuUI(currentPosition)
            uiBot()
            
            if nav == 1:
                nav = currentPosition = 0
                fighting = True

            elif nav == 2:
                nav = currentPosition = 0
                battle = False
                shop = True

        elif fighting:
            if hasNewEnemy:
                clearTerminal()
                uiTop()
                printToTerminal("you win!")
                printToTerminal("UH OH! you see an enemy! {}".format(newenemy.name))
                printToTerminal("continue to next clearing?")
                subMenuUI(currentPosition)
                uiBot()
                if nav == 1:#yes continue
                    nav = currentPosition = 0
                    hasNewEnemy = False

                elif nav == 2: #no
                    nav = currentPosition = 0
                    fighting = False
                    shop = True
            else:
                clearTerminal()
                uiTop()
                printToTerminal("{}'s current health is {} with defense {}".format(newenemy.name, newenemy.hp, newenemy.defense))
                battleDisp(currentPosition)
                uiBot()
                if nav == 1 and not dead: #fight current enemy
                    turns += 1
                    escapeCost = turns + math.floor(clearing*(1/3))
                    newenemy.damage(pc.itemDamage)
                    pc.damagePlayer(newenemy.att)
                    nav = currentPosition = 0
                elif (nav == 2) and (not dead) and (money - escapeCost > 0): #run away
                    money = money - escapeCost
                    shopItem1.roll(4)
                    shopItem2.roll(4)
                    fighting = False
                    shop = True
                    nav = currentPosition = 0
                if dead:
                    uiTop()
                    printToTerminal("you died at clearing: " + str(clearing) + " and dropped your item!")
                    printToTerminal(" ")
                    printToTerminal("[Menu]")
                    uiBot()
                    if nav == 1:
                        fighting = False
                        mainMenu = True
                        shopItem1.roll(4)
                        shopItem2.roll(4)
                        nav = currentPosition = 0
                        clearing = 0
                elif newenemy.hp <= 0:
                    nav = 0
                    clearing += 1
                    turns = 0
                    money = money + newenemy.gold
                    newenemy = Enemy(clearing)
                    hasNewEnemy = True


    
    elif out:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentPosition = (currentPosition - 1) % 2
                elif event.key == pygame.K_RIGHT:
                    currentPosition = (currentPosition + 1) % 2
                elif (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1
                elif (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
                    currentPosition = 0
                elif (event.key == pygame.K_2) or (event.key == pygame.K_KP2):
                    currentPosition = 1
        clearTerminal()
        uiTop()
        printToTerminal('are you sure?')
        subMenuUI(currentPosition)
        uiBot()

        if nav == 1:
            playing = False
        elif nav == 2:
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

    time.sleep(speed)

