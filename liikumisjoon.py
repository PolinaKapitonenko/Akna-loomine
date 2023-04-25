import pygame,sys,random
pygame.mixer.Sound
pygame.init()

def Liikumine():
	global posX,posY
	if posX==0 and posY==0:
		sammX=1
		sammY=0		
	if posX==x-mesilane.get_rect().width and posY<=y-mesilane.get_rect().height:	
		sammX=0
		sammY=1
	if posX<=x-mesilane.get_rect().width and posY==y-mesilane.get_rect().height:	
		sammX=1
		sammY=0
		sammX=-sammX
	if posX==0 and posY>=y-mesilane.get_rect().height:					
		sammX=0
		sammY=1
		sammY=-sammY
	posX+=sammX
	posY+=sammY
	ekraan.blit(mesilane,(posX,posY))
	pygame.display.flip()

kollane=[255,255,10]
punane=[255,0,0]
hall=[255,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

x=640
y=480
ekraan=pygame.display.set_mode([x,y])
pygame.display.set_caption("polinkina animatsija ;3 ;3 ")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("Poke_Ball.png")
posX=x-mesilane.get_rect().width
posY=y-mesilane.get_rect().height
lopp=False
samm=2
while not lopp:
    kell.tick(150)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    ekraan.blit(mesilane,(posX,posY))
    if posX <= 0:
        posX = 0
        posY -= samm
    if posY <= 0:
        posY = 0
        posX += samm + 2
    if posX >= x - mesilane.get_rect().width:
        posX = x - mesilane.get_rect().width
        posY += samm
    if posY >= y - mesilane.get_rect().height:
        posY = y - mesilane.get_rect().height
        posX -= samm + 2
    ekraan.blit(mesilane,(posX,posY))
    pygame.display.flip()
    ekraan.fill(kollane)

pygame.mixer.music.load('music/android.mp3')
pygame.mixer.music.play(0)
hit_sound = pygame.mixer.Sound("android.mp3")
pygame.mixer.Sound.play(hit_sound)

pygame.quit()