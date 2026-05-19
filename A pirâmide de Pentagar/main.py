#A Pirâmide de Pentagar
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import math

class Pontos:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0

  def set_x(self, x):
    self.x = x

  def set_y(self, y):
    self.y = y

  def set_z(self, z):
    self.z = z


class Faces:
  def __init__(self):
    self.pontos = []
    self.r = 0
    self.g = 0
    self.b = 0
    self.a = 0

  def add_ponto(self, ponto):
    self.pontos.append(ponto)

  def set_r(self, r):
    self.r = r

  def set_g(self, g):
    self.g = g

  def set_b(self, b):
    self.b = b

  def set_a(self, a):
    self.a = a

def desenhar_pirâmide():
  gl.glBegin(gl.GL_POLYGON)
  gl.glColor3f(1, 1, 1, 1)
  for i in range(len(base.pontos)):
    gl.glVertex3f(base.pontos[i].x, base.pontos[i].y, base.pontos[i].z)
  gl.glEnd()
  for i in range(len(base.pontos)):
    if i+1 < len(base.pontos):
      gl.glBegin(gl.GL_POLYGON)
      gl.glColor3f(random.random(), random.random(), random.random(), 1)
      gl.glVertex3f(base.pontos[i].x, base.pontos[i].y, base.pontos[i].z)
      gl.glVertex3f(base.pontos[i+1].x, base.pontos[i+1].y, base.pontos[i+1].z)
      gl.glVertex3f(0, 0.5, 0)
      gl.glEnd()
    else:
      gl.glBegin(gl.GL_POLYGON)
      gl.glColor3f(random.random(), random.random(), random.random(), 1)
      gl.glVertex3f(base.pontos[i].x, base.pontos[i].y, base.pontos[i].z)
      gl.glVertex3f(base.pontos[0].x, base.pontos[0].y, base.pontos[0].z)
      gl.glVertex3f(0, 0.5, 0)
      gl.glEnd()


def mudar_cam(cx, cy, cz, ax, ay, az, vx, vy, vz):
  glu.gluLookAt(cx, cy, cz,
     ax, ay, az,
     vx, vy, vz,)

def teclado(tecla, x, y):
  match tecla[0]:
  #tecla S
    case 115:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      mudar_cam(0, 0.15, -1,
               0, 0.15, 0,
               0, 1, 0)
      desenhar_pirâmide()
      glut.glutSwapBuffers()
    #tecla W
    case 119:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      mudar_cam(0, 0.8, -1,
               0, 0.15, 0,
               0, 1, 0)
      desenhar_pirâmide()
      glut.glutSwapBuffers()
    #tecla a
    case 97:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      mudar_cam(-0.25, 0.5, -1,
               0, 0.15, 0,
               0, 1, 0)
      desenhar_pirâmide()
      glut.glutSwapBuffers()
    #tecla d
    case 100:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 20)
      mudar_cam(0.35, 0.5, -1,
               0, 0.15, 0,
               0, 1, 0)
      desenhar_pirâmide()
      glut.glutSwapBuffers()




def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  mudar_cam(0, 0.15, -1,
            0, 0.15, 0,
            0, 1, 0)
  desenhar_pirâmide()
  glut.glutSwapBuffers()


#criando a base:
base = Faces()
#ponto f
p1 = Pontos()
p1.set_x(-0.3)
p1.set_z(0.1)
base.add_ponto(p1)
#ponto a
p2 = Pontos()
p2.set_x(0)
p2.set_z(0.3)
base.add_ponto(p2)
#ponto b
p3 = Pontos()
p3.set_x(0.3)
p3.set_z(0.1)
base.add_ponto(p3)
#ponto c
p4 = Pontos()
p4.set_x(0.2)
p4.set_z(-0.2)
base.add_ponto(p4)
#ponto d
p5 = Pontos()
p5.set_x(-0.2)
p5.set_z(-0.2)
base.add_ponto(p5)


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
