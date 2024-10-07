import random

def randomize(win = 0):
    result = random.randrange(0,100)
    if isinstance(win, int) and (result >= win):
        return True
    elif isinstance(win, str) and (win == "number"):
        return result
    else: return False


while True:
    print("enter to randomize a number")
    vibes = input()
    try:
        value = int(vibes)
    except ValueError:
        value = vibes
    print(randomize(value))