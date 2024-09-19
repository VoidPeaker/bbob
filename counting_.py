from convertexcel import Item, myItem 

def setBonus(self = myItem):
    output = "{} {} {}".format(self.getInfo('adj', "set"), self.getInfo('noun', "set"), self.getInfo('of', "set"))

    setList = output.split(" ")
    setCounter = {}

    for element in setList:
        if element not in setCounter:
            setCounter[element] = 0
        setCounter[element] += 1
        #counter.get(0)

    set = list(setCounter)[0]
    numInSet = list(setCounter.values())[0]

    if numInSet == 1:
        return "no set bonus"
    elif numInSet == 2:
        if set == "bad" or "abstract" or "wizard" or "machine" or "baseball" or "emotion" or "gun" or "throw" or "knight" or "classic" or "lgbt" or "cute" or "patriotic" or "gold" or "audio" or "basic" or "fancy":
            return set + " 2"
    elif numInSet == 3:
        if set == "bad" or "abstract" or "wizard" or "machine" or "baseball" or "emotion" or "gun" or "throw" or "knight" or "classic" or "lgbt" or "cute" or "patriotic" or "gold" or "audio" or "basic" or "fancy":
            return set + " 3"




