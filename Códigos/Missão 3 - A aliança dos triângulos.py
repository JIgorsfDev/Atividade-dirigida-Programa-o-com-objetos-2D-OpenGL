#Desenvolva uma função que desenhe triângulos isósceles com base e altura fornecidas pelo usuário. Em seguida, use essa função para desenhar pelo menos 5 triângulos com diferentes tamanhos e posições em tela. 
#Cada triângulo deve ter uma cor distinta.

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import sys
import random as rd

r = 0
g = 0
b = 0

triangulos = []

for i in range(5):
    bs = float(input("Digite a base do triângulo (entre -1 e 1): "))
    h = float(input("Digite a altura do triângulo (entre -1 e 1): "))

    x = rd.uniform(-1, 1 - bs)
    y = rd.uniform(-1, 1 - h)

    triangulos.append((bs, h, x, y))


def teclado(tecla, x, y):
    if tecla == b'\x1b':
        sys.exit()


def cor():
    global r, g, b
    r = rd.random()
    g = rd.random()
    b = rd.random()


def draw_triangles(bs, h, x, y):
    gl.glBegin(gl.GL_TRIANGLES)
    cor()
    gl.glColor3f(r, g, b)
    gl.glVertex2f(x, y)
    gl.glVertex2f(x + bs, y)
    gl.glVertex2f(x + bs / 2, y + h)
    gl.glEnd()


def draw():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    for i in triangulos:
        bs, h, x, y = i
        draw_triangles(bs, h, x, y)

    gl.glFlush()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("A aliança dos triângulos")
glut.glutReshapeWindow(500, 500)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
