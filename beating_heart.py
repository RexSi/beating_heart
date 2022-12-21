#!/usr/bin/env python3

import pgzrun
from math import pi, sin, cos
import random

no_p = 20000
dt = 2 * pi / no_p


def generate_point(t):
    x = 16 * sin(t) ** 3
    y = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)
    return (x, y)


class Particle():
    def __init__(self, pos, size, f):
        self.pos = pos
        self.pos0 = pos
        self.size = size
        self.f = f

    def draw(self):
        screen.draw.filled_rect(Rect((10 * self.f * self.pos[0] + 400, -10 * self.f * self.pos[1] + 300), self.size), 'hot pink')

    def update(self, t):
        df = 1 + (2 - 1.5 * self.f) * sin(3 * t) / 8
        self.pos = self.pos0[0] * df, self.pos0[1] * df


def generate_particles(dt):
    t = 0
    particles = []
    while t <= 2 * pi:
        l = (10 - abs(random.gauss(10, 2) - 10)) / 10.0
        (x, y) = generate_point(t)
        particles.append(Particle([x, y], (1, 1), l))
        t += dt
    return particles


def generate_outer_heart(dt):
    t = 0
    while t <= 2 * pi:
        l = random.gauss(1.1, 0.1)
        (x, y) = generate_point(t)
        size = (random.uniform(0.5, 2.5), random.uniform(0.5, 2.5))
        t += dt * 3
        screen.draw.filled_rect(Rect(( 10 * l * x + 400, -10 * l * y + 300), size), 'hot pink')


particles = generate_particles(dt)

def draw():
    screen.clear()
    for p in particles:
        p.draw()

    generate_outer_heart(dt)


t = 0
def update(dt):
    global t
    t += dt
    for p in particles:
        p.update(t)


pgzrun.go()
