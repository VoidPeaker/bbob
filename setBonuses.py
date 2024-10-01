from itemDeclaration import Item, myItem 

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


    if set == "bad":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "abstract":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "wizard":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "machine":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "baseball":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "emotion":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "gun":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "throw":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "knight":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "classic":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "lgbt":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "cute":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "patriotic":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "gold":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "audio":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "basic":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "fancy":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "BASIC":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "jazz":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass
    elif set == "clown":
        if numInSet == 2:
            pass
        elif numInSet ==3:
            pass




