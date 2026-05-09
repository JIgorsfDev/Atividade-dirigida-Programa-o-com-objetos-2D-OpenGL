#Reconstruir um antigo símbolo conhecido como "Insígnia de Malta", usado para desbloquear o “Portal dos Pixels”. Para isso, crie uma função chamada desenharInsignia() que monte uma figura simétrica utilizando
#apenas retângulos e triângulos. Ao pressionar a tecla “ C” deve alterar as cores do símbolo aleatoriamente (como se ele ganhasse “energia mágica”).
#errado

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import sys
import random as rd

r = 1
g = 0
b = 0

def teclado(tecla, x, y):
  if tecla == b'c' or tecla == b'C':
    rd_cor()
    glut.glutPostRedisplay()

  elif tecla == b'\x1b':
    glut.glutDestroyWindow(glut.glutGetWindow())
    sys.exit(0)

def rd_cor():
  global r, g, b
  r = rd.random()
  g = rd.random()
  b = rd.random()

def desenharInsignia(): #montados via geogebra
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(r, g, b)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.3, 0.7)
  gl.glVertex2f(0.0, 0.5)

  gl.glVertex2f(-0.3, 0.7)
  gl.glVertex2f(0.0, 0.5)
  gl.glVertex2f(0.0, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(-0.7, 0.3)
  gl.glVertex2f(-0.5, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(-0.5, 0.0)
  gl.glVertex2f(-0.7, -0.3)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.0, -0.5)
  gl.glVertex2f(0.3, -0.7)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.0, -0.5)
  gl.glVertex2f(-0.3, -0.7)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.7, 0.3)
  gl.glVertex2f(0.5, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.5, 0.0)
  gl.glVertex2f(0.7, -0.3)

  gl.glEnd()

def draw():
  gl.glClearColor(1.0, 1.0, 1.0, 1.0)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)

  desenharInsignia()
  gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("A Insígnia de malta")
glut.glutReshapeWindow(500, 500)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
