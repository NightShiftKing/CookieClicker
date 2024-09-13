import math
import pygame

pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("cookie clicker")

#game variables
doExit = False #variable to quit out of game loop
numClicks = 0 
xpos = 400 
ypos = 400
mousePos = (xpos, ypos) 

circX = 400
circY = 400
radius = 100

CookiePic = pygame.image.load("cookie.jfif")
CookieRect = CookiePic.get_rect(center=(400,400))



font = pygame.font.Font('calibri', 32)
text1 = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))



def Cookie():

    CookieColor = (150, 75, 0)
    pygame.draw.circle(screen, CookieColor, (xpos, ypos), radius)
    





#BEGIN GAME LOOP######################################################
while not doExit:
   
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = event.pos
        if math.sqrt((mousePos[0] - circX)**2 + (mousePos[1] - circY)**2)<100: 
            numClicks+=3
            print(numClicks)  
     

        
     
    #render section-----------------------------------vis
    Cookie()
    pygame.display.flip()

    screen.blit(CookiePic, CookieRect)
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
