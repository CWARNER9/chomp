import pygame
print("Hello EW200!")

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((52, 140, 235))
sand_height = 100
pygame.draw.rect(background, (250, 192, 85), (0, HEIGHT-sand_height, WIDTH, sand_height))

screen.blit(background, (0,0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()