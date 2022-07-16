import pygame
import random
pygame.init()
#to create a window in th pygame
display=pygame.display.set_mode((1000,600))
#title and logo setting to the game that we were creating 
pygame.display.set_caption("janarthananxo")
logo=pygame.image.load('spaceship.png')
pygame.display.set_icon(logo)

burstimg=pygame.image.load('explosion.png')

playerimg=pygame.image.load('spaceship.png')
playerx=468
playery=550
playerxmove=0
playerymove=0



bulletimg=pygame.image.load('bullet.png')
bulletymove=0.5

aliens = []
alienimg=pygame.image.load('alien.png')


for i in range(1):
    alienx=random.randint(0,968)
    alieny=0
    alienymove=0.2
    aliens.append([alienx, alieny, alienymove])

bullets=[]

def bullet(x,y):
    bulletx=x+8
    bullety=y+16
    display.blit(bulletimg,(bulletx,bullety))

def burst(x,y):
    display.blit(burstimg,(x,y))

score=0

def aliendes(bul,alien):

    global score

    if abs(bul[0]- alien[0]) <= 26 and abs(bul[1]-alien[1])<=20:
        alien[1] = 0
        alien[0] = random.randint(0, 968)
        bullets.remove(bul)
        score += 1


def player(x,y):
    display.blit(playerimg,(x,y))


def alien(x,y):
    display.blit(alienimg,(x,y))

run=True 
while run:
    
    display.fill((0,0,0)) 


    for event in pygame.event.get():
        if event.type ==pygame.QUIT: 
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                playerxmove -= 0.4
            elif event.key == pygame.K_RIGHT :
                playerxmove += 0.4
            if event.key == pygame.K_UP  :
                playerymove -= 0.4
            if event.key == pygame.K_DOWN :
                playerymove += 0.4
            if event.key == pygame.K_s:
                bullets.append([playerx, playery])


        if event.type== pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerxmove = 0
                playerymove = 0
    playerx += playerxmove
    playery += playerymove 
    if playerx <= 0 : 
        playerx = 0
    if playerx >=968:
        playerx=968
    if playery <=0 :
        playery = 0
    if playery >= 568:
        playery = 568    
    

    for i in aliens:
            alienx = i[0]
            alieny = i[1]
            i[1]+= alienymove
            alien(alienx,alieny)
            if i[1]>= 568:
                print('gameover')
                run=False
    for bul in bullets:
        bullet(bul[0],bul[1]) 
        aliendes(bul,i)
        bul[1] -= bulletymove

    for bul in bullets:
        if bul[1] <= 0:
            bullets.remove(bul)    

    player(playerx,playery)

    pygame.display.update()              
print( 'your score ',score)