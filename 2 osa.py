import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/4.0) *kõrgus)), (x,y), (x+laius,y), (x+laius,y- (3/4.0) * kõrgus), (x,y- ((3/4.0) * kõrgus)),(x+laius/2.0,y-kõrgus),(x+laius,y-(3/4.0) *kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)



fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

majavärv=[r,g,b]


pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud")
pind.fill(fon)



Maja(100,400,300,400,pind,majavärv)
pygame.display.flip()


lil=pygame.Rect(215,22,70,70)
pygame.draw.ellipse(pind, (250,250,0), lil)

ristkülik=pygame.Rect(297,217,100,180)                            
pygame.draw.rect(pind,(205,133,63),ristkülik)

ristkülik=pygame.Rect(120,165,100,100)                            
pygame.draw.rect(pind,(250,250,0),ristkülik)

ristkülik=pygame.Rect(167,165,6,100)                            
pygame.draw.rect(pind,(205,133,63),ristkülik)

ristkülik=pygame.Rect(120,212,100,6)                            
pygame.draw.rect(pind,(205,133,63),ristkülik)



for i in range(0):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    varv=[r,g,b]

    laius=random.randint(1,80)
    kõrgus=random.randint(1,80)



    x=random.randint(0,640-laius)
    y=random.randint(0,480-kõrgus)
    pygame.draw.rect(pind,varv,[x,y,laius,kõrgus])


  







pygame.display.flip()

while True:
    event=pygame.event.poll()  
    if event.type==pygame.QUIT:
        sys.exit()

pygame.quit() 
