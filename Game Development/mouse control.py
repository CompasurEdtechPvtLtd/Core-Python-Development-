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

bg = pygame.image.load("pexels-fwstudio-129731.jpg")
bg = pygame.transform.scale(bg,(W,H))
while True:
    screen.fill(color)
    screen.blit(bg,(0,0))
    for event in pygame.event.get():


            
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            
    # rect(screen,color,[x,y,w,h])
    mouseX,mouseY = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    pygame.draw.rect(screen,red,[mouseX-rectW/2,mouseY-rectH/2,rectW,rectH])
   
    #pygame.draw.circle(screen,red,[circleX,circleY],c_radius)

    pygame.display.update()
