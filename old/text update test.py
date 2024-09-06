import pygame
import pygame.freetype
import random
import os
import sys

pygame.init()
os.system('cls')
screen = pygame.display.set_mode((640, 576))
clock = pygame.time.Clock()
running = True
font = pygame.freetype.SysFont("Courier", 32)
screensize = pygame.Rect((0,640), (576, 0))
running = True

anim = open("anim.txt", 'r')
animHolder = anim.read()
textRend= animHolder.split('\n')

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    def Update(arg):
        if arg == 1:
            pygame.time.wait(200)
            pygame.display.flip()
            screen.fill("white")
        if arg == 2:
            pygame.time.wait(20)
            pygame.display.flip()


   
    i = 0
    #textOut = ["this is line 1", "this is line 2", "this is line 3"]
    #textRend = ["|","/","+","\\"]
    #
    for n in range(10000):
        
        #textRend.append("this is line {}".format(n))
        i += 1
        #print(i)
        #drawY = font.size*(i-1)
        text_surface, rect = font.render(" "+str(textRend[i]), (0, 0, 0))
        screen.blit(text_surface, (screensize.x/2,1))
        print(i)
        if i >= len(textRend)-1:
            i = 0
        Update(1)
        #if drawY > screensize.y:
        #    Update()
    
       

        
        #i = 0

    
    # top to bottom iterator
    

 





     
    clock.tick(10) 

pygame.quit()