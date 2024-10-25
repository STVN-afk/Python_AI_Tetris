import pygame
from grid import Grid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 720))
pygame.display.set_caption("AI Tetris Board")
clock = pygame.time.Clock()
grey = (211,211,211)
running = True 

#Grid Setup 
tetris_grid = Grid()
tetris_grid.print_grid()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    tetris_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
