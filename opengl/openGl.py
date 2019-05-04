
# ####################################################
#
# ####################################################
from cube import Cube

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

objectList = []

def main():
    #objectList.append(Cube(size=0.5, offsetX=1.4))
    #objectList.append(Cube(size=0.2, offsetX=2.0))
    #objectList.append(Cube(size=0.1, offsetX=4.0))
    #objectList.append(Cube(size=0.05, offsetX=8.0))
    objectList.append(Cube(offsetX=0.0))
    pygame.init()
    display = (1024,768)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/ display[1]), 0.1, 50.0)


    glRotatef(0, 0,0,0)

    glTranslate(0.0, 0.0, -5.0)
    r = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        r -= 0.0001
        glTranslate(r, r, r)

        glRotate(0.5, 1, 1, 1)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for nextObject in objectList:
            nextObject.render()

        pygame.display.flip()
        pygame.time.wait(20)

main()

