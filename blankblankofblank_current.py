import random, math, pygame, time, sys
from convertexcel import *
from counting_ import *

mainMenu = True
shop = False
battle = False
out = False
money = 100
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

def writeAnim(text, speed):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
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
        printToTerminal('[7] '.ljust(w) + ' 8 '.ljust(w) + ' 9 '.ljust(w))

    elif currentPosition == 7:
        printToTerminal(' 7 '.ljust(w) + '[8] '.ljust(w) + ' 9 '.ljust(w))

    elif currentPosition == 8:
        printToTerminal(' 7 '.ljust(w) + ' 8 '.ljust(w) + '[9] '.ljust(w))
    else:
        printToTerminal(' 7 '.ljust(w) + ' 8 '.ljust(w) + ' 9 '.ljust(w))

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
    elif currentPosition == -1:
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
        self.playerHp = 15
        self.playerDefense = 5


    def damagePlayer(self, enemyDamage):
        if enemyDamage - self.playerDefense > 0:
            self.playerHp = self.playerHp - (enemyDamage - self.playerDefense)

newenemy = Enemy(1)
pc = Player()

def uiTop():
    printToTerminal("gold: " + str(money))
    printToTerminal(myItem.toReadable())
    if allitBonus(myItem):
        printToTerminal('alliteration bonus!!')
    printToTerminal(setBonus())
    printToTerminal("attack: {}  defense: {}  speed: {}".format(playerStatCalc(myItem)[0], playerStatCalc(myItem)[1], playerStatCalc(myItem)[2]))
    printToTerminal("---------------------------------------------")
def uiBot(thisText = "> "):
    printToTerminal("---------------------------------------------")
    
    # idk why this isnt working; comments are the intentions. also the i is saying its not referenced but idk wky
    # for i in range((numLines) - len(visibleText)): ## for all of the lines that are not taken up by text
    #     visibleText.append("")                     ## put a blank line



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
    else:
        printToTerminal(" 1. start")
        printToTerminal(" 2. battle")
        printToTerminal("[3] quit")

def battleDisp(currentPosition):
    w = 40
    printToTerminal("what do you do?")
    if (currentPosition == 0):
        printToTerminal('[1] fight!'.ljust(w) + ' 2  shop!'.ljust(w))
    elif (currentPosition == 1):
        printToTerminal(' 1  fight!'.ljust(w) + '[2] shop!'.ljust(w))
    else:
        printToTerminal(' 1  fight!'.ljust(w) + '[2] shop!'.ljust(w))
    
def shopItemConfirm(myItem = myItem, shopItem1 = shopItem1, shopItem2 = shopItem2,  nav = 0):
    _index = 0 #initialize local variable to pass to either of the items that is being asked about
    if nav == 7 or 4:
        _index = 0
    if nav == 8 or 5:
        _index = 1
    if nav == 9 or 6:
        _index = 2

    if nav == 7 or 8 or 9:
        printToTerminal(shopItem1.getList()[_index])
        printToTerminal("")
        printToTerminal("attack: {}  defense: {}  speed: {}".format((shopItem1.getInfo(shopItem1.getList()[_index], "att")),
                                                                    (shopItem1.getInfo(shopItem1.getList()[_index], "def")), 
                                                                    (shopItem1.getInfo(shopItem1.getList()[_index], "speed"))))
        printToTerminal("")



#main playing loop``
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
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1

        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
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


        # if it's 1, 2, or 3, we move to a different screen
        if nav == 1:
            mainMenu = False
            nav = 0
            shop = True

        elif nav == 2:
            mainMenu = False
            battle = True
            newenemy = Enemy(i)
            nav = 0
        elif nav == 3:
            out = True
            mainMenu = False
            nav = 0

    elif shop:
        clearTerminal()

        uiTop()
        shopDisp(shopItem1.getList(), shopItem2.getList(), currentPosition) #sending the item string as it currently is, and the position of the highlighted number
        uiBot()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentPosition = (currentPosition - 1) % 5
                elif event.key == pygame.K_RIGHT:
                    currentPosition = (currentPosition + 1) % 5
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1

        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
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
                    currentPosition = -1
                

        if (nav == 7 or nav == 8 or nav == 9) and (money >= 3): #money-3 == 0?
            money -= 3
            clearTerminal()
            shopItemConfirm(nav = nav)
            #Replace(myItem.getList(), nav-1,shopItem1.getList()[nav-1] )
            #shopItem1.roll(nav)
            nav = 0

        elif (nav == 4) and (money >= 1):
            money -= 1
            clearTerminal()
            shopItem1.roll(nav)
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
        clearTerminal()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currentPosition = (currentPosition - 1) % 2
                elif event.key == pygame.K_RIGHT:
                    currentPosition = (currentPosition + 1) % 2
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    nav = currentPosition + 1

        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1) or (event.key == pygame.K_KP1):
                    currentPosition = 0
                elif (event.key == pygame.K_2) or (event.key == pygame.K_KP2):
                    currentPosition = 1

        turns = 0
        i = 1 #this is the enemy level, but i realized it was going up one per location, so it also equals clearing
        nav = 0
        if nav == 0:
            uiTop()
            printToTerminal('{} attacks!!!!!'.format(newenemy.name))
            printToTerminal("he has {} health, {} defense, {} gold!".format(newenemy.hp, newenemy.defense, newenemy.gold))
            battleDisp(currentPosition)
            uiBot()             
        elif nav == 1:
            uiTop
            printToTerminal("clearing: {}").format(i)
            newenemy.damage(pc.itemDamage)
            pc.damagePlayer(newenemy.att)
            printToTerminal("{}'s current health is {} with defense {}".format(newenemy.name, newenemy.hp, newenemy.defense))
            loopDelay()
            uiBot()

        elif nav == 2:
            battle = False
            shop = True

        '''
        #nav = int(input())
        if nav == 1:
            attack = True
            printToTerminal('{} attacks!!!!!! he has {} health and {} defense!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defense))
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
                printToTerminal('uh oh!\n{} attacks!!!!!! he has {} health and {} defense!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defense))
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
                printToTerminal("{}'s current health is {} with defense {}".format(newenemy.name, newenemy.hp, newenemy.defense))
                input()
                '''      
    elif out:
        clearTerminal()
        uiTop()
        printToTerminal('are you sure?')
        uiBot()
        #nav = int(input())
        if nav == 1:
            playing = False
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