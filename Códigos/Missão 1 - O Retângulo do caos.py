#Crie um retângulo com largura e altura fornecidas pelo usuário. Ao pressionar a barra de espaço, gere uma nova combinação aleatória de cores para o retângulo e o fundo da janela.

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random as rd
import sys

r1 = 1
g1 = 1
b1 = 1
r2 = 0
g2 = 0
b2 = 0


def rd_cor(): #função do CAOS! é nela que os valores da randomização ocorrem
    global r1, g1, b1, r2, g2, b2
    r1 = rd.random()
    g1 = rd.random()
    b1 = rd.random()
    r2 = rd.random()
    g2 = rd.random()
    b2 = rd.random()


def teclado(tecla, x, y): #função que captura o teclado
    if tecla == b" ": #random
        rd_cor()
        glut.glutPostRedisplay()
    elif tecla == b'\x1b': #botão de sair do código
        glut.glutDestroyWindow(glut.glutGetWindow())
        sys.exit(0)

while True:
  l = float(input("Digite a largura do Retangulo (entre 0 e 1): "))
  a = float(input("Digite a altura do Retangulo (entre 0 e 1): "))

  if 0 <= l <= 1 and 0 <= a <= 1:
    break

  else:
    print("Valores inválidos! Tente novamente.\n")


def draw_flat(): #retângulo de cor única
    gl.glClearColor(r2, g2, b2, 1.0)

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(r1, g1, b1)
    gl.glVertex2f(l, a)
    gl.glVertex2f(l, -a)
    gl.glVertex2f(-l, -a)
    gl.glVertex2f(-l, a)
    gl.glEnd()
    gl.glFlush()


def draw_smooth(): #retângulo de cor misturada
    gl.glClearColor(r2, g2, b2, 1.0)

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glShadeModel(gl.GL_SMOOTH)
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(r1, g1, b1)
    gl.glVertex2f(l, a)
    rd_cor()
    gl.glColor3f(r1, g1, b1)
    gl.glVertex2f(l, -a)
    rd_cor()
    gl.glColor3f(r1, g1, b1)
    gl.glVertex2f(-l, -a)
    rd_cor()
    gl.glColor3f(r1, g1, b1)
    gl.glVertex2f(-l, a)
    gl.glEnd()
    gl.glFlush()

while True:
  op = input("1 - Flat\n2 - Smooth\nEscolha uma opção de randomização:")

  if op == "1" or op == "2":
      break
  else:
      print("Opção inválida! Tente novamente.\n")


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("O Retângulo do caos")
glut.glutReshapeWindow(1000, 1000)

if op == "1":
    glut.glutDisplayFunc(draw_flat)

elif op == "2":
    glut.glutDisplayFunc(draw_smooth)

glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
