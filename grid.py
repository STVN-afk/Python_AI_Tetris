import pygame

def drawGrid(screen):
    color = (0,0,0)
    pygame.draw.rect(screen, color, pygame.Rect(20, 20, 300, 600),  2)

    for x in range(1,10):
        pygame.draw.line(screen,color,((x*30)+ 20,20),((x*30) + 20,618),1)

    for x in range(1,20):
        pygame.draw.line(screen,color,(20,(x*30)+ 20), (318,(x*30)+ 20),1)
