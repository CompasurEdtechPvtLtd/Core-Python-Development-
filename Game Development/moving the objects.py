import pygame
pygame.init()

W = 800
H = 500
#rgb - red,green,blue - 0-255
color = 255,255,255
screen = pygame.display.set_mode((W,H))
red = 255,0,0
rectW = 50
rectH = 50
rectX=0
rectY=0
circleX=100
circleY=100
c_radius = 50
moveX = 0.5
moveY = 0.5
while True:
    screen.fill(color)
    # rect(screen,color,[x,y,w,h])
    pygame.draw.rect(screen,red,[rectX,rectY,rectW,rectH])
    rectX+=moveX
    rectY+=moveY
    #pygame.draw.circle(screen,red,[circleX,circleY],c_radius)
    if rectX > W-rectW:
        moveX=-0.5
    elif rectX < 0:
        moveX=0.5

    if rectY > H-rectH:
        moveY=-0.5
    elif rectY < 0:
        moveY=0.5
    pygame.display.update()
