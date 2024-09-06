import random, json, os, collections, numbers

list =['a', 'b', 'a']
i = 1
c = collections.Counter(list)
# print(c.values())
# print(c.keys())
# if(len(c.keys()) == 1):
#     print("yahoo")


def allitBonus(letters):
    return letters[0] == letters[1] == letters[2]

if allitBonus(list):
    i = 2

print(i)
        
