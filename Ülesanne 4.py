import pygame 
import random
import sys


r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

fon=[r,g,b]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud koju")
pind.fill(fon)
pygame.display.flip()











while True:
    event=pygame.event.poll()  
    if event.type==pygame.QUIT:
        sys.exit()

pygame.quit() 