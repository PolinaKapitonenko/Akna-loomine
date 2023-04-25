import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/5.0) *kõrgus)), (x,y), (x+laius,y), (x+laius,y- (3/5.0) * kõrgus), (x,y- ((3/5.0) * kõrgus)),(x+laius/2.0,y-kõrgus),(x+laius,y-(3/5.0) *kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)


def Uks(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,True,punktid,suurus)



def akn(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-kõrgus),(x+laius,y-kõrgus),(x+laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,True,punktid,suurus)



r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)


fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

majavärv=[r,g,b]


pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud koju")
pind.fill(fon)


Maja(50,350,450,400,pind,majavärv)
Uks(50,350,250,400,pind,majavärv)
akn(235,90,80,40,pind,majavärv)  
pygame.display.flip()





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

