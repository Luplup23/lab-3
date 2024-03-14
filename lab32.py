import pygame as pg

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption("Second Game")

ZOLTY = (255, 255, 0)
imageForEdit = pg.image.load('background.png')
normalImage=pg.transform.scale(imageForEdit,(400,250))
image01 = pg.transform.scale(imageForEdit,(300,200))
image02 = pg.transform.rotate(normalImage,320)
image031 = pg.transform.rotate(normalImage, 180)
image03 = pg.transform.scale(image031, (200,300))
image041 = pg.transform.rotate(normalImage,353)
image04 = pg.transform.flip(image041,1,0)
imagee05 = pg.transform.scale(normalImage, (300,100))
image06 = pg.transform.rotate(normalImage, 278)
image07 = pg.transform.flip(image03,1,0)
image081 =pg.transform.scale(normalImage, (400,100))
image082 =pg.transform.rotate(image081, 330)
image09 = pg.transform.rotate(normalImage, 340)


addimage=image01;
x = 150
y = 180
rect1X1=0
rect2X1=0
rect1Y1=0
rect2Y1=0
rect1X2=0
rect2X2=0
rect1Y2=0
rect2Y2=0
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
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0
            if event.key == pg.K_2:
                x=60
                y=100
                addimage=image02
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0
            if event.key == pg.K_3:
                x=200
                y=100
                addimage=image03
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0 
            if event.key ==pg.K_4:
                x=60
                y=100
                addimage=image04
                rect1X1=0
                rect2X1=0
                rect1Y1=600
                rect2Y1=170
                rect1X2=0
                rect2X2=330
                rect1Y2=600
                rect2Y2=170
                pg.draw.rect(win,ZOLTY, (0,0,600,170))
                pg.draw.rect(win,ZOLTY, (0,330,600,170))
            if event.key ==pg.K_5:
                x=150
                y=0
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0 
                addimage=imagee05
            if event.key == pg.K_6:
                x=100
                y=100
                addimage=image06
                rect1X1=0
                rect2X1=0
                rect1Y1=160
                rect2Y1=600
                rect1X2=340
                rect2X2=0
                rect1Y2=160
                rect2Y2=600
                pg.draw.rect(win,ZOLTY,(0,0,160,600))
                pg.draw.rect(win,ZOLTY,(340,0,160,600))
            if event.key == pg.K_7:
                x=200
                y=100
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0                 
                addimage=image07
            if event.key ==pg.K_8:
                x=100
                y=300
                rect1X1=0
                rect2X1=0
                rect1Y1=0
                rect2Y1=0
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0                 
                addimage=image082
            if event.key ==pg.K_9: 
                x=250
                y=100  
                rect1X1=0
                rect2X1=0
                rect1Y1=350
                rect2Y1=600
                rect1X2=0
                rect2X2=0
                rect1Y2=0
                rect2Y2=0                 
                pg.draw.rect(win,ZOLTY,(0,0,350,600))
                addimage=image09

    pg.draw.rect(win, ZOLTY,(0,0,600,600))
    win.blit(addimage,(x,y))
    pg.draw.rect(win,ZOLTY, (rect1X1,rect2X1,rect1Y1,rect2Y1))
    pg.draw.rect(win,ZOLTY, (rect1X2,rect2X2,rect1Y2,rect2Y2))
  
    pg.display.update()
