#Crie uma cena com “quatro formas geométricas”. Cada forma (círculo, quadrado, triângulo, e outra que você deve escolher) deve ser desenhada em uma área própria da janela. Utilize cores variadas para cada forma.
#incompleta

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random as rd
import sys
import math

r = rd.random()
g = rd.random()
b = rd.random()


def cor():
    global r, g, b
    r = rd.random()
    g = rd.random()
    b = rd.random()


def teclado(tecla, x, y):
    if tecla == b"\x1b":
        glut.glutDestroyWindow(glut.glutGetWindow())
        sys.exit(0)


def circulo(x, y, r, nseg=100):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x, y)

    for i in range(nseg + 1):
        ang = 2 * math.pi * i / nseg
        gl.glVertex2f(x + math.cos(ang) * r, y + math.sin(ang) * r)

    gl.glEnd()


def display():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glShadeModel(gl.GL_FLAT)

    cor()

    circulo(0.025, 0.5, 0.2)

    cor()

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(r, g, b)
    gl.glVertex2f(0.3, 0.7)
    gl.glVertex2f(0.7, 0.7)
    gl.glVertex2f(0.7, 0.3)
    gl.glVertex2f(0.3, 0.3)
    gl.glEnd()

    cor()

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(r, g, b)
    gl.glVertex2f(-0.2, -0.2) #base direita
    gl.glVertex2f(0.05, 0.2) #topo
    gl.glVertex2f(0.3, -0.2) #base esquerda
    gl.glEnd()

    cor()

    gl.glBegin(gl.GL_POLYGON)  # octogono -> se der tempo, "devo puxar ele mais pra perto do triângulo"
    gl.glColor3f(r, g, b)
    gl.glVertex2f(0.6, 0.2)
    gl.glVertex2f(0.5, 0.1)
    gl.glVertex2f(0.5, -0.1)
    gl.glVertex2f(0.6, -0.2)
    gl.glVertex2f(0.8, -0.2)
    gl.glVertex2f(0.9, -0.1)
    gl.glVertex2f(0.9, 0.1)
    gl.glVertex2f(0.8, 0.2)
    gl.glEnd()

    gl.glFlush()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("O painel das formas")
glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
