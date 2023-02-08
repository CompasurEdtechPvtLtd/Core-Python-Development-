import pygame
pygame.init()

W = 600
H = 400
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
while True:
    screen.fill(color)
    # rect(scree,color,[x,y,w,h])
    pygame.draw.rect(screen,red,[rectX,rectY,rectW,rectH])
    pygame.draw.circle(screen,red,[circleX,circleY],c_radius)
    pygame.display.update()
