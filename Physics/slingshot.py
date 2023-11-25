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

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        win.blit(PLANET, (self.x - PLANET_RADIUS, self.y - PLANET_RADIUS))
class Spaceship:
    def __init__(self, x, y, x_vel, y_vel, mass):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mass = mass

    def move(self, planet = None):
        distance = math.sqrt((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2)
        force = G * self.mass * planet.mass / (distance ** 2)
        
        acceleration = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)
        
        x_acceleration = acceleration * math.cos(angle)
        y_acceleration = acceleration * math.sin(angle)

        self.x_vel += x_acceleration
        self.y_vel += y_acceleration 

        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), SPACESHIP_SIZE)

def create_spaceship(location, mouse):
    x_t, y_t = location
    x_m, y_m = mouse
    x_vel = (x_m - x_t) / VELOCITY_SCALE
    y_vel = (y_m - y_t) / VELOCITY_SCALE

    obj = Spaceship(x_t, y_t, x_vel, y_vel, SPACESHIP_MASS)
    return obj


def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos: 
                    obj = create_spaceship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
            
                else:
                    temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, SPACESHIP_SIZE)

        for obj in objects[:]:
            obj.draw()
            obj.move(planet)

            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT 
            collided = math.sqrt((obj.x - planet.x) ** 2 + (obj.y - planet.y) ** 2) <= PLANET_RADIUS
            
            if off_screen or collided:
                objects.remove(obj)
            
        planet.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()