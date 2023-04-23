import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("GUI Tic Tac Toe")
window.fill((255, 255, 255))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()
