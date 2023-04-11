import pygame 
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)
jalg=pygame.Rect(310,200,20,280)
pygame.draw.rect(ekraani_pind,(50,205,0), jalg)
lill=pygame.Rect(200,100,220,200)
pygame.draw.ellipse(ekraani_pind,(250,250,0), lill)

pilt=pygame.image.load("Poke_Ball.png")
ekraani_pind.blit(pilt,(260,150))

font=pygame.font.SysFont("Broadway",40)
sõnad="Tere tulemast!"
varv=[0,0,0]
teksti_lisanime=font.render(sõnad,False,varv)
ekraani_pind.blit(teksti_lisanime,(150,30))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
