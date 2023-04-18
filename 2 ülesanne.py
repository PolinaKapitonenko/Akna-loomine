import pygame

pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))#создает окно размеров в скобках 
pygame.display.set_caption("teine ülesanne")

pilt=pygame.image.load("ivi2.png")
ekraani_pind.blit(pilt,(640,480))

font=tekst=pygame.font.SysFont("Broadway",40)
sõnad="kõrb!"
värv=[0,0,0]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(250,15))



pygame.display.flip() #нужно для того, чтобы код работала и запускался #отображает

while True:
    event=pygame.event.poll()  #функция для крестика, чтобы закрыть раб.  код
    if event.type==pygame.QUIT:
        break

pygame.quit() #нужно для того, чтобы код работала


