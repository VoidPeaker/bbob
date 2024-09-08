import random, json, os, collections, math, time

playing = True 
attack = True



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

newenemy = Enemy()
newenemy.makeEnemy(1)
pc = Player()


while playing:
    i = 1
    combo = 0
    newenemy.makeEnemy(i)
    print('{} attacks!!!!!! he has {} health and {} defence!\nenter to attack!'.format(newenemy.name, newenemy.hp, newenemy.defence))
    input()
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

        
        else:
            os.system('cls')
            print("enemies beaten: {}\nitem attack: {}\ncurrent health: {}".format(combo, pc.itemDamage, pc.playerHp))
            newenemy.damage(pc.itemDamage)
            pc.damagePlayer(newenemy.att)
            print("{}'s current health is {} with defence {}".format(newenemy.name, newenemy.hp, newenemy.defence))
            input()
            

    


