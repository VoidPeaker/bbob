import os, json
# import collections
# nouns = open("nouns.txt", 'r')
# nounsHolder = nouns.read()
# nounsList= nounsHolder.split('\n')

# adj = open("adjectives.txt", 'r')
# adjHolder = adj.read()
# adjList = adjHolder.split('\n')

# of = open("of.txt", 'r')
# ofHolder = of.read()
# ofList = ofHolder.split('\n')


# s = "quick brown fox jumps over the lazy dog"

# s = s.replace(' ', '')
# s = collections.Counter(s).most_common(1)
# #print(str(s).center(50))

# def replace(list, i, string):
#     list.pop(i)
#     list.insert(i, "{}".format(string))
#     return list

# def itemDisp():
#     w = 20
#     print(items[0].ljust(w), items[1].ljust(w), items[2].ljust(w), "all", "\n" + '1'.ljust(w),'2'.ljust(w),'3'.ljust(w), '4')

# #print("lover".ljust(w) + "coal".ljust(w) + 'over')

# a = "lover"
# b = "coal"
# c = "verbage"

# items = ['lover', 'coal', 'verbiage']





# #print(items[0].ljust(w), items[1].ljust(w), items[2].ljust(w), "all", "\n" + '1'.ljust(w),'2'.ljust(w),'3'.ljust(w), '4')
# #print('1'.ljust(w),'2'.ljust(w),'3'.ljust(w)+'4')
# itemDisp()

# replace(items, 1, "greenery")
# itemDisp()
# input("choose number ")

#for n in items:
def Screen():
    os.system('cls')

def Replace(list, i, string):
    list.pop(i)
    list.insert(i, "{}".format(string))
    return list

nounList = []
nounFile = open('basic nouns.json', "r")
nounRam = json.load(nounFile)
# print(nounRam["hat"])
# for i in nounRam:
#     print(i, nounRam[i]['weight'])
#     #nounList.append(i)

def roll():
    
    pass

print(nounList)



# screen = 0 

# while True:
#     Screen()
#     print(screen)
    
#     while screen == 0:
#         Screen()
#         nav = int(input('1 screen one \n2 screen two \n3 screen three\n'))
#         if nav == 1:
#             screen = 1
#             break
#         elif nav == 2:
#             screen = 2
#             break
#         elif nav == 3:
#             screen = 3
#             break
        
#     while screen == 1:
#         Screen()
#         nav = int(input('this is screen one\n1 back\n'))
#         if nav == 1:
#             screen = 0

#     while screen == 2:
#         Screen()
#         nav = int(input('this is screen two\n1 back\n'))
#         if nav == 1:
#             screen = 0

#     while screen == 3:
#         Screen()
#         nav = int(input('this is screen three\n1 back\n'))
#         if nav == 1:
#             screen = 0



    




