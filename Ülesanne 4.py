import pygame
import sys
import random

pygame.init()

X = 640
Y = 480

Valge = (255, 255, 255)
Must = (0, 0, 0)
Kollane = (255, 255, 0)

Õuna_suurus = 20
Korvi_laius = 30
Korvi_kõrgus = 30

Õun_X = random.randint(0, X - Õuna_suurus)
Õun_Y = 0

Korvi_X = X // 2 - Korvi_laius // 2
Korvi_Y = Y // 1.5

Õuna_kiirus = 5 #Скорость падения яблок.

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Õuna ja korviga mängimine")

õuna_pilt = pygame.image.load("õun.png")  # для яблока
korvi_pilt = pygame.image.load("vinni.png")  # для корзины

clock = pygame.time.Clock()
score = 0
gameover=False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover=True
        elif pygame.key.get_pressed()[pygame.K_a]:
            Korvi_X-=5
        elif pygame.key.get_pressed()[pygame.K_d]:
            Korvi_X+=5
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                Korvi_X-=5
            elif event.key==pygame.K_RIGHT:
                Korvi_X+=5

    Õun_Y += Õuna_kiirus

    if Õun_Y >= Y:
        Õun_X = random.randint(0, X - Õuna_suurus)
        Õun_Y = 0

    if Õun_Y + Õuna_suurus >= Korvi_Y and Õun_X + Õuna_suurus >= Korvi_X and Õun_X <= Korvi_X + Korvi_laius:
        score += 1
        Õun_X = random.randint(0, X - Õuna_suurus)
        Õun_Y = 0


    screen.fill(Valge)


    screen.blit(õuna_pilt, (Õun_X, Õun_Y)) # Отображение изображения яблока на экране
    screen.blit(korvi_pilt, (Korvi_X, Korvi_Y)) # Отображение изображения корзины на экране

    font = pygame.font.Font(None, 36)
    score_text = font.render("Счет: {}".format(score), True, Must)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
