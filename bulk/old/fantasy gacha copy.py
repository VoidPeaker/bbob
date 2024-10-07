import random
import os
nouns = open("nouns.txt", 'r')
nounsHolder = nouns.read()
nounsList= nounsHolder.split('\n')

adj = open("adjectives.txt", 'r')
adjHolder = adj.read()
adjList = adjHolder.split('\n')

of = open("of.txt", 'r')
ofHolder = of.read()
ofList = ofHolder.split('\n')


os.system('cls')
input("generate item?") 


class Item:
    def __init__(self):
        adj = random.choice(adjList)
        if adj != '': adj = adj + ' '
        noun = random.choice(nounsList)
        of = random.choice(ofList)
        if of != '': of = ' ' + of
        
        output = adj + noun + of      
        print("Your item is:\n{}".format(output) +'!!')
        

        if (adj != '') and (adj[0] == noun[0]):
            print("alliteration bonus! 2x effectiveness")
        elif (adj != '') and (of != '') and (adj[0] == noun[0] == of[3]):
            print("TRIPLE ALLITERATION! 4x EFFECTIVENESS")




while(True):
    os.system('cls')
    Item()
    input("generate another?")



#if responce:
#    output = Item()
#    print("your item is: \n{}".format(output.name))
#    responce = input("generate another?")
    



nouns.close()
adj.close()
of.close()