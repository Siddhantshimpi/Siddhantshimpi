import pygame, math

pygame.init()

# CONSTANTS:

WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot")

PLANET_MASS = 100 ## CHANGE LATER to 1.5467972e+26
PLANET_RADIUS = 50 # CHANGE LATER to 34326.301
SPACESHIP_MASS = 5 # CHANGE LATER to 28,801
SPACESHIP_SIZE = 5 # CHANGE LATER to something

VELOCITY_SCALE = 100 # CHANGE LATER to something
G = 5 # CHANGE LATER to 6.67408e-11
FPS = 120

# BACKGROUND AND PLANET SIZES

BG = pygame.transform.scale(pygame.image.load("Images\galaxy.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("Images\planet.jpg"), (PLANET_RADIUS * 2, PLANET_RADIUS * 2))

# COLORS

WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
 
# MAIN CODE

def main():
    running = True
    clock = pygame.time.Clock()
    
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.circle(win, RED, temp_obj_pos, SPACESHIP_SIZE)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()