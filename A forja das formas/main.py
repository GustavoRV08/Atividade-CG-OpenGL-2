#A Forja das Formas
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


class Camera():
  def __init__(self):
    self.cx = 0.0; self.cy = 0; self.cz = -1
    self.ax = 0; self.ay = 0; self.az = 0
    self.vx = 0; self.vy = 1; self.vz = 0

cam = Camera()

def desenhar_ampulheta():
  for i in range(len(bases)):
    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glColor3f(1, 1, 0, 1)
    for j in range(len(bases[i].pontos)):
      gl.glVertex3f(bases[i].pontos[j].x, bases[i].pontos[j].y, bases[i].pontos[j].z)
    gl.glEnd()

  for i in range(len(bases)):
    for j in range(len(bases[i].pontos)):
      if j+1 < len(bases[i].pontos):
        gl.glBegin(gl.GL_LINE_LOOP)
        gl.glColor3f(1, 1, 0, 1)
        gl.glVertex3f(bases[i].pontos[j].x, bases[i].pontos[j].y, bases[i].pontos[j].z)
        gl.glVertex3f(bases[i].pontos[j+1].x, bases[i].pontos[j+1].y, bases[i].pontos[j+1].z)
        gl.glVertex3f(0, 0, 0)
        gl.glEnd()
      else:
        gl.glBegin(gl.GL_LINE_LOOP)
        gl.glColor3f(1, 1, 0, 1)
        gl.glVertex3f(bases[i].pontos[j].x, bases[i].pontos[j].y, bases[i].pontos[j].z)
        gl.glVertex3f(bases[i].pontos[0].x, bases[i].pontos[0].y, bases[i].pontos[0].z)
        gl.glVertex3f(0, 0, 0)
        gl.glEnd()


def mudar_cam():
  glu.gluLookAt(cam.cx, cam.cy, cam.cz,
                cam.ax, cam.ay, cam.az,
                cam.vx, cam.vy, cam.vz,)

def teclado(tecla, x, y):
  match tecla[0]:
  #tecla S
    case 115:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cy -= 0.05
      mudar_cam()
      desenhar_ampulheta()
      glut.glutSwapBuffers()
    #tecla W
    case 119:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cy += 0.05
      mudar_cam()
      desenhar_ampulheta()
      glut.glutSwapBuffers()
    #tecla a
    case 97:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cx -= 0.05
      mudar_cam()
      desenhar_ampulheta()
      glut.glutSwapBuffers()
    #tecla d
    case 100:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 20)
      cam.cx += 0.05
      mudar_cam()
      desenhar_ampulheta()
      glut.glutSwapBuffers()




def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  mudar_cam()
  desenhar_ampulheta()
  glut.glutSwapBuffers()


bases = []
#criando as bases:
#base 1
bases.append(Faces())
#ponto a
p1 = Pontos()
p1.set_x(-0.2)
p1.set_z(0.2)
p1.set_y(-0.5)
bases[0].add_ponto(p1)
#ponto b
p2 = Pontos()
p2.set_x(0.2)
p2.set_z(0.2)
p2.set_y(-0.5)
bases[0].add_ponto(p2)
#ponto c
p3 = Pontos()
p3.set_x(0.2)
p3.set_z(-0.2)
p3.set_y(-0.5)
bases[0].add_ponto(p3)
#ponto d
p4 = Pontos()
p4.set_x(-0.2)
p4.set_z(-0.2)
p4.set_y(-0.5)
bases[0].add_ponto(p4)

#base 2
bases.append(Faces())
#ponto a
p5 = Pontos()
p5.set_x(-0.2)
p5.set_z(0.2)
p5.set_y(0.5)
bases[1].add_ponto(p5)
#ponto b
p6 = Pontos()
p6.set_x(0.2)
p6.set_z(0.2)
p6.set_y(0.5)
bases[1].add_ponto(p6)
#ponto c
p7 = Pontos()
p7.set_x(0.2)
p7.set_z(-0.2)
p7.set_y(0.5)
bases[1].add_ponto(p7)
#ponto d
p8 = Pontos()
p8.set_x(-0.2)
p8.set_z(-0.2)
p8.set_y(0.5)
bases[1].add_ponto(p8)


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
