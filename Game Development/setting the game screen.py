import pygame
#step1
pygame.init()

W = 600
H = 400
#rgb - red,green,blue - 0-255
color = 255,0,0
screen = pygame.display.set_mode((W,H))

while True:
    screen.fill(color)
    pygame.display.update()
