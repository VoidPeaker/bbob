# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1210, 633))
clock = pygame.time.Clock()
running = True

# initialize font
fontSize = 25
font = pygame.font.SysFont("lucidaconsole", fontSize)


# set colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# declaring the list that will contain the visible lines of text
numLines = 24
lineWidth = 80
visibleText = []
for i in range(numLines):
    visibleText.append("".ljust(lineWidth))

# function to print a line to the terminal window
def printToTerminal(newLine):
    visibleText.pop(0) # remove the oldest line
    visibleText.append(newLine.ljust(80))

def clearTerminal():
    visibleText = []
    for i in range(numLines):
        visibleText.append("".ljust(lineWidth))

printToTerminal("test one")
printToTerminal("test two")
printToTerminal("test three")
printToTerminal("lorem ipsum dolor sit amet")
printToTerminal("mooonday leeft me borken")
printToTerminal("tuesday i was through with ohpin")
printToTerminal("wednesday I forget the fuckin lyrics")
clearTerminal()
printToTerminal("test?")


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    


    # RENDER YOUR GAME HERE
    height = 5
    for line in visibleText:
        img = font.render(line, True, GREEN)
        #rect = img.get_rect()
        #pygame.draw.rect(img, RED, rect, 1)
        screen.blit(img, (5,height))
        height = height + fontSize + 1
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()