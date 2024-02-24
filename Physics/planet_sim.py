import pygame, numpy as np
import math
pygame.init()

width, height = 1920, 1080
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Trappist-1 Planet Simulation')

class Body:
    AU = 1.496e+11
    M_E = 5.972e+24
    R_E = 6.371e+6
    G = 6.67428e-11

    scale_radius = 2500000
    scale_distance = 6000 / AU
    timestep = 1200

    def __init__(self, x, y, radius, color, mass, label):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.label = label

        self.orbit = []
        self.star = False
        self.distance_to_star = 0

        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, win):
        x = self.x * self.scale_distance + width / 2
        y = self.y * self.scale_distance + height / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.scale_distance + width / 2
                y = y * self.scale_distance + height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        star_text = pygame.font.SysFont('timesnewroman', 21).render('Trappist-1', 1, (255, 255, 255))
        win.blit(star_text, (355, 390))

        if not self.star:
            distance_text = pygame.font.SysFont('timesnewroman', 16).render('{} '.format(self.label) +
             f'[{round(self.distance_to_star / 1.496e+11, 4)} AU]', 1, (255, 255, 255))
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))
            

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.star:
            self.distance_to_star = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)

        force_x = force * np.cos(theta)
        force_y = force * np.sin(theta)

        return force_x, force_y

    def update_pos(self, bodies):
        total_fx = total_fy = 0
        for planet in bodies:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_velocity += total_fx / self.mass * self.timestep
        self.y_velocity += total_fy / self.mass * self.timestep

        self.x += self.x_velocity * self.timestep
        self.y += self.y_velocity * self.timestep
        self.orbit.append((self.x, self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    trappist_1 = Body(0, 0, 13.21 * Body.R_E / Body.scale_radius, (255, 0, 0), 29637.37 * Body.M_E, '')
    trappist_1.star = True

    trappist_1b = Body(-0.012 * Body.AU, 0, 1.116 * Body.R_E / Body.scale_radius, (48, 213, 200), 1.374 * Body.M_E, 'Trappist-1b')
    trappist_1b.star = False
    trappist_1b.y_velocity = 83.770e+03

    trappist_1c = Body(0.016 * Body.AU, 0, 1.10 * Body.R_E / Body.scale_radius, (255, 218, 164), 1.308 * Body.M_E, 'Trappist-1c')
    trappist_1c.star = False
    trappist_1c.y_velocity = -71.621e+03

    trappist_1d = Body(-0.022 * Body.AU, 0, 0.79 * Body.R_E / Body.scale_radius, (40, 122, 184), 0.388 * Body.M_E, 'Trappist-1d')
    trappist_1d.star = False
    trappist_1d.y_velocity = 60.380e+03

    trappist_1e = Body(0.029 * Body.AU, 0, 0.92 * Body.R_E / Body.scale_radius, (181, 217, 217), 0.692 * Body.M_E, 'Trappist-1e')
    trappist_1e.star = False
    trappist_1e.y_velocity = -52.256e+03

    trappist_1f = Body(-0.038 * Body.AU, 0, 1.045 * Body.R_E / Body.scale_radius, (255, 218, 164), 1.039 * Body.M_E, 'Trappist-1f')
    trappist_1f.star = False
    trappist_1f.y_velocity = 43.753e+03

    trappist_1g = Body(0.047 * Body.AU, 0, 1.129 * Body.R_E / Body.scale_radius, (255, 218, 164), 1.321 * Body.M_E, 'Trappist-1g')
    trappist_1g.star = False
    trappist_1g.y_velocity = -41.148e+03

    trappist_1h = Body(-0.062 * Body.AU, 0, 0.755 * Body.R_E / Body.scale_radius, (59, 29, 0), 0.326 * Body.M_E, 'Trappist-1h')
    trappist_1h.star = False
    trappist_1h.y_velocity = 35.820e+03

    bodies = [trappist_1, trappist_1b, trappist_1c, trappist_1d, trappist_1e, trappist_1f, trappist_1g, trappist_1h]

    while run:
        clock.tick(60)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in bodies:
            planet.update_pos(bodies)
            planet.draw(win)
        
        pygame.display.update()
    
    pygame.quit()

main()