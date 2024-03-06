# 3D animation of Unsolved Rubics Cube.
# Please install below Libraries to run the program.
# Python 3.12.2
# Pygame 2.5.2
# PyOpenGL


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import itertools


colors = {
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
    "orange": (1, 0.5, 0),
    "white": (1, 1, 1),
    "yellow": (1, 1, 0),
    "purple": (0.5, 0, 0.5),
    "cyan": (0, 1, 1),
}


def select_color_for_cube(position):

    color_keys = list(colors.keys())
    index = sum(position) % len(color_keys)
    return colors[color_keys[index]]


def draw_cube_segment(position, size=1.0):
    vertices = [
        [size, -size, -size], [size, size, -size], [-size,
                                                    size, -size], [-size, -size, -size],
        [size, -size, size], [size, size, size], [-size, -
                                                  size, size], [-size, size, size]
    ]

    vertices = [[x + dx for x, dx in zip(vertex, position)]
                for vertex in vertices]

    surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    cube_color = select_color_for_cube(position)

    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv(cube_color)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv(colors["white"])
    glBegin(GL_LINES)
    for edge in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def init_scene():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -40)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_scene()

    cube_positions = [(x, y, z) for x in range(-3, 4, 3)
                      for y in range(-3, 4, 3) for z in range(-3, 4, 3)]

    rotation_x = rotation_y = 0

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        for position in cube_positions:
            draw_cube_segment(position, 1.2)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
