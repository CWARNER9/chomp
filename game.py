import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


puffer_fish = pygame.image.load('assets/images/puffer_fish.png')
water_tile = pygame.image.load('assets/images/fishTile_089.png')
sand_top_tile = pygame.image.load('assets/images/fishTile_021.png')
sand_tile = pygame.image.load('assets/images/fishTile_126.png')
plant_tile = pygame.image.load('assets/images/fishTile_032.png')
background = pygame.Surface((WIDTH, HEIGHT))
tile_width = water_tile.get_width()
tile_height = water_tile.get_height()

#Water Tiles
for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT,tile_height):
        background.blit(water_tile, (x,y))

for x in range(0,WIDTH,tile_width):
     background.blit(sand_tile, (x,HEIGHT-tile_height))

for x in range(0,WIDTH,tile_width):
    background.blit(sand_top_tile, (x,HEIGHT-2*tile_height))

num_plants = 6
for p in range(num_plants):
    background.blit(plant_tile, (randint(0,WIDTH), randint(HEIGHT-3*tile_height, HEIGHT-1*tile_height)))


screen.blit(background, (0,0))


game_font = pygame.font.SysFont('impact', 120)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    font_surface = game_font.render('CHOMP', 1, (199, 23, 4))
    f_width = font_surface.get_width()
    f_height = font_surface.get_height()
    screen.blit(font_surface, (WIDTH/2-f_width/2, HEIGHT/2-f_height/2))
    clock.tick()
    pygame.display.set_caption(f"CHOMP {clock.get_fps():3f}")

    screen.blit(puffer_fish, (WIDTH/2, HEIGHT/2))
    pygame.display.flip()

