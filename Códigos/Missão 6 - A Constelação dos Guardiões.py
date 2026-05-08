#Construa a “Constelação dos Guardiões”, formada por um conjunto de círculos de diferentes tamanhos, que representam estrelas mágicas conectadas por propósito. Crie uma função desenharEstrela(x, y, raio) para
#desenhar um círculo em uma posição específica. Utilize essa função para montar uma constelação composta por pelo menos 7 estrelas, cada uma com:
#1- Um raio diferente (variação entre 10 e 50) e cores aleatórias gerada a cada execução.
#2- Conexões entre estrelas feitas por linhas finas (use GL_LINES).
#3- Recursos interativos:
#4- Pressionar a tecla "n" para adicionar uma nova estrela com raio e posição aleatórios.
#5- Pressionar a tecla "x" para remover uma das estrelas (pode ser aleatoriamente ou não).
#6- Pressionar a tecla "r" reinicia a constelação.
#7- Pressionar "t" ativa o “modo noturno” (plano de fundo preto e estrelas brilhantes em branco ou amarelo).

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random as rd
import math
import sys

r = 0
g = 0
b = 0

estrela = []
dark = False

def cor():
  global r, g, b
  r = rd.random()
  g = rd.random()
  b = rd.random()

def desenharEstrela(x, y, ray, r, g, b):
   gl.glColor3f(r, g, b)
   gl.glBegin(gl.GL_POLYGON)

   for i in range(20):
      angulo = 2 * math.pi * i / 20
      gl.glVertex2f(x + ray * math.cos(angulo), y + ray * math.sin(angulo))

   gl.glEnd()

def addEstrela():
   x = rd.uniform(-1, 1)
   y = rd.uniform(-1, 1)
   raio = rd.randint(10, 50) / 100.0
   cor()
   estrela.append((x, y, raio, r, g, b))
   glut.glutPostRedisplay()

def removerEstrela():
   if len(estrela) > 0:
      estrela.pop()
      glut.glutPostRedisplay()
   else:
      print("O céu está limpo hoje...")

def reiniciarConstelação():
   estrela.clear()
   for _ in range(7):
      addEstrela()
   glut.glutPostRedisplay()

def dark_mode():
   global dark
   dark = not dark
   glut.glutPostRedisplay()

def teclado(tecla, x, y):
   if tecla == b'\x1b':
      glut.glutDestroyWindow(glut.glutGetWindow())
      sys.exit(0)

   elif tecla == b'n' or tecla == b'N':
      addEstrela()

   elif tecla == b'x' or tecla == b'X':
      removerEstrela()

   elif tecla == b'r' or tecla == b'R':
      reiniciarConstelação()

   elif tecla == b't' or tecla == b'T':
      dark_mode()

def draw():
   if dark:
      gl.glClearColor(0.0, 0.0, 0.0, 1.0)
   else:
      gl.glClearColor(1.0, 1.0, 1.0, 1.0)

   gl.glClear(gl.GL_COLOR_BUFFER_BIT)

   for i in range(len(estrela)):
      x, y, ray, r1, g1, b1 = estrela[i]

      if dark:
         r1, g1, b1 = 1.0, 1.0, 0.0

      desenharEstrela(x, y, ray, r1, g1, b1)

   gl.glBegin(gl.GL_LINES)

   for i in range(len(estrela) - 1):
      x1, y1, _, _, _, _ = estrela[i]
      x2, y2, _, _, _, _ = estrela[i + 1]

      if dark:
         gl.glColor3f(0.8, 0.8, 0.8)
      else:
         gl.glColor3f(0.0, 0.0, 0.0)

      gl.glVertex2f(x1, y1)
      gl.glVertex2f(x2, y2)

   gl.glEnd()

   gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow("Constelação dos Guardiões")
glut.glutReshapeWindow(600, 600)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(teclado)

for _ in range(7):
   addEstrela()

glut.glutMainLoop()
