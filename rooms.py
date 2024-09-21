import random
print("you come to a fork in the road")

def Room():
    roomName = ['battle', 'shop', 'mystery']
    return random.choice(roomName)


#make a room of a random name 
#
#
#

print(Room())