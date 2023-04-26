﻿import pygame, random
 

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 3, 4

player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("vinni.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

enemies = []
for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0,screenY - 100), 60, 73))
enemyImage = pygame.image.load("õun.png")
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])

enemyCounter = 0
totalEnemies = 20
score = 0

gameover = False
while not gameover:
    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage,player)

    posX += speedX
    posY += speedY

    if posX > screenX-playerImage.get_rect().width or posX <0:
        speedX = -speedX

    if posY > screenY-playerImage.get_rect().width or posY <0:
        speedY = -speedY
    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()
    screen.fill(blue)

    print(score)
    if score == 20:
        gameover = True
pygame.quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Korvi_X > 0:
        Korvi_X -= 5
    if keys[pygame.K_RIGHT] and Korvi_X < X - Korvi_laius:
        Korvi_X += 5