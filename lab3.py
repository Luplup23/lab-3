import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255 ,255)
CZARNY = (0, 0 ,0)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, BIALY, (0,0 ,600 ,600))
    # koło kwadrat
    pygame.draw.circle(win, CZARNY, (70, 80), 50, 0)
    pygame.draw.rect(win, ZOLTY , (47, 55, 50, 50))
    # zielony kwardrat z wcieciem
    pygame.draw.rect(win, ZIELONY, (160, 30, 100, 100))
    pygame.draw.polygon(win, BIALY, ((160, 130),(210, 80),(260, 130)))
    # niebieski kształt
    pygame.draw.rect(win, NIEBIESKI, (30, 200, 100, 50))
    pygame.draw.polygon(win, NIEBIESKI, ((55,150), (105,150),(80,200)))
    pygame.draw.polygon(win, NIEBIESKI, ((55,300), (105,300),(80,250)))

    # Z
    pygame.draw.line(win, CZERWONY, (160, 205), (260, 205), 5)
    pygame.draw.line(win, CZERWONY, (160, 300), (260, 205), 5)
    pygame.draw.line(win, CZERWONY, (160, 300), (260, 300), 5)
    # wypisywanie tekstu
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Tekst do wyświetlania ', 1, (255, 255, 255))
    win.blit(label, (100, 425))

    pygame.display.update()