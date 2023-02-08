import pygame,random
pygame.init()
W = 800
H = 500
#rgb - red,green,blue - 0-255
black =0,0,0
blue =  0 , 255 , 0
color = 255,255,255
green = 0,255,0
screen = pygame.display.set_mode((W,H))
red = 255,0,0

sound1 = pygame.mixer.Sound("collision_sound.wav")



rectW = 30
rectH = 30




def Snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,red,[snakeList[i][0],snakeList[i][1],rectW,rectH])


def Score(score):
    font = pygame.font.SysFont(False,20)
    text = font.render(f"Score : {score}",True,black)
    screen.blit(text,(20,20))

def GameOver():
    font = pygame.font.SysFont(None,80)
    text_1 = font.render("GAME OVER",True,blue)
    text_2 = font.render("Press ENTER TO RESTART",True,red)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Game()
                
            elif event.type==pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text_1,(W//2-150,H//2-150))
        screen.blit(text_2,(10,350))
        pygame.display.update()

def Game():
    rectX=0
    rectY=0
 
    moveX = 0
    moveY = 0
    enemyW=30
    enemyH=30
    snakeList = []
    snakeLength = 1
    score=0
    enemyX,enemyY = random.randint(0,W-enemyW) , random.randint(0,H-enemyH)
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

        snakeList.append((rectX,rectY))
        Snake(snakeList)
        if snake.colliderect(enemy):
            enemyX,enemyY = random.randint(0,W-enemyW) , random.randint(0,H-enemyH)
            sound1.play(0)
            score += 1
            snakeLength+=50

        if snakeLength<len(snakeList):
            del snakeList[0]

        for i in snakeList[:-1]:
            if snakeList[-1] == i:
                GameOver()


        Score(score)

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


Game()