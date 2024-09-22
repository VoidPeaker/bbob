import time, sys, os

text = ['this is my text', 'this is the next part of my text', 'fart machine']

t=.1

def writeAnim(text, speed):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

def loopDelay(text = '. . . . ', speed = .1):
    loopCount = 0
    speed = .2

    while True:

        print('looped {} times'.format(loopCount))
        writeAnim('. . . . . ', speed)
        speed1 = speed1 - speed1/20
 
    

loopDelay() 