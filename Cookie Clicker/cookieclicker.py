import math
import pygame

pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("cookie clicker")


numClicks = 0 
xpos = 400 
ypos = 400
mousePos = (xpos, ypos) 

clock = pygame.time.Clock()

circX = 400
circY = 400
radius = 100

isBig = False

CookiePic = pygame.image.load("cookie.jpg")
CookieRect = CookiePic.get_rect(center=(400,400))

CookiePic2 = pygame.image.load("cookie2.jpg")
CookieRect2 = CookiePic2.get_rect(center=(400,400))

font = pygame.font.SysFont('calibri', 32)
text1 = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))



def Cookie():
    CookiePic = pygame.image.load("cookie.jpg")
    CookieRect = CookiePic.get_rect(center=(400,400))

    CookiePic2 = pygame.image.load("cookie2.jpg")
    CookieRect2 = CookiePic2.get_rect(topleft=(390,390))

    





#BEGIN GAME LOOP######################################################
while True:

    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        break

    clock.tick(15)
   
   


    #keyboard input-----------------------------------
    
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        if math.sqrt((mousePos[0] - circX)**2 + (mousePos[1] - circY)**2)<100: 
            isBig = True
        else:
            isBig = False
        
    if event.type == pygame.MOUSEBUTTONDOWN :
        if math.sqrt((mousePos[0] - circX)**2 + (mousePos[1] - circY)**2)<100: 
            numClicks+=1
        

        
     
    #render section-----------------------------------vis

    screen.fill((0,0,0))


  
    if(isBig == True):
        screen.blit(CookiePic2, CookieRect2)
    else: 
        screen.blit(CookiePic, CookieRect)



    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
