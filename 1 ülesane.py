import pygame 
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Lumememm")
screen = pygame.display.set_mode((400, 400))

black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
yellow = (250,250,0)
brown= (205,133,63)

pygame.draw.circle(screen, white, (200, 210), 60, 0) # тело
pygame.draw.circle(screen, white, (200, 100), 50, 0) # голова
pygame.draw.circle(screen, orange, (200, 120), 10, 0) # нос
pygame.draw.line(screen, orange, (200, 140), (200, 145), 6) # рот
pygame.draw.circle(screen, black, (175, 110), 5, 0) # глаза
pygame.draw.circle(screen, black, (225, 110), 5, 0) # глаза
pygame.draw.circle(screen, white, (200, 335), 70, 0) # низ тела
pygame.draw.circle(screen, yellow, (200, 180), 9, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 210), 9, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 240), 9, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 290), 11, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 320), 11, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 350), 11, 0) # пуговица
pygame.draw.circle(screen, yellow, (200, 380), 11, 0) # пуговица
pygame.draw.circle(screen, brown, (200, 20), 40, 0) # голова
pygame.draw.line(screen, brown, (200, 40), (200, 60), 100) # шляпа
pygame.draw.line(screen, brown, (60, 190), (140, 210), 8) # ручка
pygame.draw.line(screen, brown, (110, 300), (260, 210), 8) # ручка


pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

pygame.quit()