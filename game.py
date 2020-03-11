import pygame
import random
from pygame import mixer

pygame.init()

running = True
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Galaxy wars")
icon= pygame.image.load("alien.png")
pygame.display.set_icon(icon)
background = pygame.image.load("b2.jpg")
mixer.music.load("BGM2.wav")
mixer.music.play(-1)
score_value = 0 
playerImg = pygame.image.load("jet.png")
playerX = 350
playerY = 480
playerX_change= 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 7

for i in range (number_of_enemies):
    enemyImg.append(pygame.image.load("enemy2.png"))
    enemyX.append( random.randint(0,730))
    enemyY.append( random.randint(40,150))
    enemyX_change.append(1.3)
    enemyY_change.append(50)

bulletImg = pygame.image.load("bul.png")
bulletX = 0
bulletY = 480
bulletY_change = 15
bullet_state = False



font = pygame.font.Font("gametext.ttf",35)
textX = 15
textY = 15
gameO_X = 365
gameO_Y = 265
buttonX= 373
buttonY = 305
tX = 377
tY = 307
def Button(x1,y1,x2,y2):
    button = pygame.draw.rect(screen,(0,5,220),(x1,y1,140,45))
    text = font.render("Tryagain",True,(0,0,0))
    screen.blit(text,(x2,y2))
def show_score(xt,yt):
     score = font.render("score: " + str(score_value),True,(0,180,0))
     screen.blit(score,(xt,yt))
def Game_over(xq,yq):
    gameover = font.render("Game over" ,True, (225,225,225))
    screen.blit(gameover,(xq,yq))
def enemy(xe,ye,i):
    screen.blit(enemyImg[i],(xe,ye))
def player(x,y):
    screen.blit(playerImg,(x,y))
def bullet(xb,yb):
    global bullet_state
    bullet_state = True
    screen.blit(bulletImg,(xb+25,yb+10))
def if_collision(x,y,z,a):
    Distance =  ((x-z)**2+(y-a)**2)**(1/2)
    if Distance < 20:
        return True
    else:
        return False

while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if not bullet_state:
                    bullet_sound = mixer.Sound("gunshot.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                        
    playerX += playerX_change    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX =  736
    
    for i in range (number_of_enemies):
        
        if enemyY[i] >= 410:
            for j in range (number_of_enemies):
                enemyY[j]= 2000
            Game_over(gameO_X,gameO_Y)
            Button(buttonX,buttonY,tX,tY)
            

        enemyX[i] += enemyX_change[i]
        if enemyX[i]<= 0:
            enemyX_change[i] = 1.3
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX_change[i] = -1.3
            enemyY[i] += enemyY_change[i]
        collisiion = if_collision(enemyX[i], enemyY[i], bulletX ,bulletY)
        if collisiion:
            col_sound = mixer.Sound("destroy.wav")
            col_sound.play()
            bulletY = 480
            bullet_state = False
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(40,200)
            score_value += 1
            value = score_value % 5
            if value == 0:
                for t in range (number_of_enemies):
                    enemyX_change[t] += 0.1
                    enemyY_change[t] += 5

        enemy(enemyX[i],enemyY[i],i)

    if bullet_state:
        bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = False
    
        
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()


