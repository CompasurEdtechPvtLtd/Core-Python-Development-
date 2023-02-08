import pygame,random
pygame.init()
from pygame import *
W = 800
H = 500
#rgb - red,green,blue - 0-255
color = 255,255,255
green = 0,255,0
screen = pygame.display.set_mode((W,H))
red = 255,0,0
rectW = 30
rectH = 30
rectX=0
rectY=0
circleX=100
circleY=100
c_radius = 50
moveX = 0
moveY = 0
enemyW=30
enemyH=30
enemyX,enemyY = random.randint(0,W-enemyW) , random.randint(0,H-enemyH)
sound1 = pygame.mixer.Sound("collision_sound.wav")
while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                moveX=-0.5
                moveY=0
            elif event.key==pygame.K_RIGHT:
                moveX=0.5
                moveY=0
            elif event.key == pygame.K_UP:
                moveY=-0.5
                moveX=0
            elif event.key==pygame.K_DOWN:
                moveY=0.5
                moveX=0

            
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            
    # rect(screen,color,[x,y,w,h])
    snake = pygame.draw.rect(screen,red,[rectX,rectY,rectW,rectH])
    enemy = pygame.draw.rect(screen,green,[enemyX,enemyY,enemyW,enemyH])
    if snake.colliderect(enemy):
        enemyX,enemyY = random.randint(0,W-enemyW) , random.randint(0,H-enemyH)
        sound1.play(0)

    rectX+=moveX
    rectY+=moveY
    #pygame.draw.circle(screen,red,[circleX,circleY],c_radius)
    if rectX > W-rectW:
        rectX=0
    elif rectX < 0:
        rectX = W-rectW

    if rectY > H-rectH:
        rectY=0
    elif rectY < 0:
        rectY=H-rectH
    pygame.display.update()
