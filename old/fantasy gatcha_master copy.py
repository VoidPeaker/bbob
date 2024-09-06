import random, os, sys, json

#open documents
nouns = open("nouns.txt", 'r')
nounsHolder = nouns.read()
nounsList= nounsHolder.split('\n')
adj = open("adjectives.txt", 'r')
adjHolder = adj.read()
adjList = adjHolder.split('\n')
of = open("of.txt", 'r')
ofHolder = of.read()
ofList = ofHolder.split('\n')
savedItems = open("user saved.txt", "a")


money = 99

#function declaration
def Replace(list, i, string):
    list.pop(i)
    list.insert(i, "{}".format(string))
    return list

def shopDisp(items):
    w = 20
    print(items[0].ljust(w), items[1].ljust(w), items[2].ljust(w), "\n\n" + '1 [3g]'.ljust(w),'2 [3g]'.ljust(w),'3 [3g]'.ljust(w), '\n' '|_______________________________________________| 4 [1g]')


class Item:
    def __init__(self):
        self.itemElements = ["NULL 1","NULL 2","NULL 3"]
        adj = random.choice(adjList)
        noun = random.choice(nounsList)


    def Reroll(self, ans):

        if ans == 1:
            adj = random.choice(adjList)
            Replace(self.itemElements, 0, adj)
        elif ans == 2:
            noun = random.choice(nounsList)
            Replace(self.itemElements, 1, noun)
        elif ans == 3:
            of = random.choice(ofList)
            Replace(self.itemElements, 2, of)
        elif ans == 4:
            adj = random.choice(adjList)
            noun = random.choice(nounsList)
            of = random.choice(ofList)
            Replace(self.itemElements, 0, adj)
            Replace(self.itemElements, 1, noun)
            Replace(self.itemElements, 2, of)          
        else:
            print("bozo")


    def toReadable(self):
        s = self.itemElements[0] + " " + self.itemElements[1] + " " + self.itemElements[2] + "\n"
        return s
    
    def print(self):
        pass
        

def Screen():
    os.system('cls')
    
#print("gold: " + str(money))
#print("\n--------------------------------\n")

#INTRO
Screen()
myItem = Item()
myItem.Reroll(4)
print("welcome! here is your first item")
shopDisp(myItem.itemElements)


 
while True:
    print("gold: " + str(money))
    ans = int(input("\n--------------------------------\n"+"Select Element to Reroll! \nPress 5 to confirm item and Start Adventure!\n"))
    if (ans == 1 or ans == 2 or ans == 3) and (money > 0):
        money -= 3
        Screen()
        myItem.Reroll(ans)
        shopDisp(myItem.itemElements)
    elif (ans == 4) and (money > 0):
        money = money - 1
        Screen()
        myItem.Reroll(ans)
        shopDisp(myItem.itemElements)
    elif (ans == 5) or (money <= 0):
        Screen()
        print('no money')
        shopDisp(myItem.itemElements)
    elif ans == 6:
        Screen()
        savedItems.write(str(myItem.toReadable()))
        print("Saved!")
        break
        



savedItems.close()
nouns.close()
adj.close()
of.close()