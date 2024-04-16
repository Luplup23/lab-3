import pygame as pg

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption("Second Game")

ZOLTY = (255, 255, 0)
ZIELONY = (0, 255, 0)


rectwhite = pg.draw.rect(win,  (0, 0 ,0), (0,0, 150, 180))   
surf = pg.Surface((150, 180))
pg.draw.rect(surf, (255,255,255), (0,0, 150, 180))
pg.draw.polygon(surf, (255,0,0), ((75,0),(100,50),(100,100),(90,120),(60,120),(50,100),(50,50)))
surf2= pg.transform.rotate(surf, 5)
forskewing = pg.Surface((150,180))
pg.draw.rect(forskewing,(0,0,0), (0,0,150,180))
pg.draw.polygon(forskewing,(255,255,255), ((0,0),(140,0),(150,180),(10,180)))
forskewing.blit(surf2,(0,0))
pg.draw.polygon(forskewing,ZIELONY, ((0,0), (0,180), (15,180)))
pg.draw.polygon(forskewing,ZIELONY, ((135,0), (150,0), (150,180)))
forskewing.set_colorkey(ZIELONY, 1)
forskewing2 =pg.Surface((150,180))
pg.draw.rect(forskewing2,(0,0,0), (0,0,150,180))
forskewing2.blit(surf2,(0,0))
pg.draw.polygon(forskewing2,ZIELONY, ((0,0), (150,0), (150,20)))
pg.draw.polygon(forskewing2,ZIELONY, ((0,160), (0,180), (150,180)))
forskewing2.set_colorkey(ZIELONY,1)

imageForEdit  = surf

normalImage=pg.transform.scale(imageForEdit,(400,250))
normalImageSkewed = pg.transform.scale(forskewing,(400,250))
normalImageSkewed2 = pg.transform.scale(forskewing2,(400,250))
image01 = pg.transform.scale(imageForEdit,(300,200))
image02 = pg.transform.rotate(normalImage,320)
image031 = pg.transform.rotate(normalImage, 180)
image03 = pg.transform.scale(image031, (200,300))
image04 = normalImageSkewed
imagee05 = pg.transform.scale(normalImage, (300,100))
image06 = pg.transform.rotate(normalImageSkewed,(270))
image07 = pg.transform.flip(image03,1,0)
image081 =pg.transform.scale(normalImage, (400,100))
image082 =pg.transform.rotate(image081, 330)
image091 = pg.transform.flip(normalImageSkewed2,1,1)
image09 = pg.transform.scale(image091, (200,300))
addimage=image01;
x = 150
y = 180
#optionalrect1=pg.draw.rect(win,ZOLTY,(0,0,0,0))
#optionalrect2=pg.draw.rect(win,ZOLTY,(0,0,0,0))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                x = 150
                y = 180
                addimage=image01
            if event.key == pg.K_2:
                x=60
                y=100
                addimage=image02
            if event.key == pg.K_3:
                x=200
                y=100
                addimage=image03
            if event.key ==pg.K_4:
                x=120
                y=180
                addimage=image04
            if event.key ==pg.K_5:
                x=150
                y=0
                addimage=imagee05
            if event.key == pg.K_6:
                x=180
                y=100
                addimage=image06
            if event.key == pg.K_7:
                x=200
                y=100
                addimage=image07
            if event.key ==pg.K_8:
                x=100
                y=300
                addimage=image082
            if event.key ==pg.K_9: 
                x=400
                y=200  
                addimage=image09

    pg.draw.rect(win, ZOLTY,(0,0,600,600))
    win.blit(addimage,(x,y))
  
    pg.display.update()
