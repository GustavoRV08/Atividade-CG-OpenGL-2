#O Bloco de Pedra de Koralon
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import math

class Camera():
  def __init__(self):
    self.cx = 0; self.cy = 0.15; self.cz = -1
    self.ax = 0; self.ay = 0.15; self.az = 0
    self.vx = 0; self.vy = 1; self.vz = 0

cam = Camera()

def desenhar_paralelepipedo():
  #face 1 (base)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0.2, 0.0, 0.4)
  gl.glVertex3f(-0.2, 0.0, 0.4)
  gl.glVertex3f(-0.2, 0.0, -0.4)
  gl.glVertex3f(0.2, 0.0, -0.4)
  gl.glEnd()
  #face 2 (frente)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0.2, 0.0, 0.4)
  gl.glVertex3f(-0.2, 0.0, 0.4)
  gl.glVertex3f(-0.2, 0.3, 0.4)
  gl.glVertex3f(0.2, 0.3, 0.4)
  gl.glEnd()
  #face 3 (trás)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0.2, 0.0, -0.4)
  gl.glVertex3f(-0.2, 0.0, -0.4)
  gl.glVertex3f(-0.2, 0.3, -0.4)
  gl.glVertex3f(0.2, 0.3, -0.4)
  gl.glEnd()
  #face 4 (esquerda)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(-0.2, 0.0, -0.4)
  gl.glVertex3f(-0.2, 0.0, 0.4)
  gl.glVertex3f(-0.2, 0.3, 0.4)
  gl.glVertex3f(-0.2, 0.3, -0.4)
  gl.glEnd()
  #face 5 (direita)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0.2, 0.0, -0.4)
  gl.glVertex3f(0.2, 0.0, 0.4)
  gl.glVertex3f(0.2, 0.3, 0.4)
  gl.glVertex3f(0.2, 0.3, -0.4)
  gl.glEnd()
  #face 6 (topo)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0.2, 0.3, 0.4)
  gl.glVertex3f(-0.2, 0.3, 0.4)
  gl.glVertex3f(-0.2, 0.3, -0.4)
  gl.glVertex3f(0.2, 0.3, -0.4)
  gl.glEnd()

def mudar_cam():
  glu.gluLookAt(cam.cx, cam.cy, cam.cz,
     cam.ax, cam.ay, cam.az,
     cam.vx, cam.vy, cam.vz,)


def teclado(tecla, x, y):
  match tecla[0]:
    case 119:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cy += 0.05;
      mudar_cam()
      desenhar_paralelepipedo()
      glut.glutSwapBuffers()

    case 115:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cy -= 0.05;
      mudar_cam()
      desenhar_paralelepipedo()
      glut.glutSwapBuffers()

    case 100:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cx += 0.05;
      mudar_cam()
      desenhar_paralelepipedo()
      glut.glutSwapBuffers()

    case 97:
      gl.glLoadIdentity()
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)
      glu.gluPerspective(60, 1, 0, 10)
      cam.cx -= 0.05;
      mudar_cam()
      desenhar_paralelepipedo()
      glut.glutSwapBuffers()



def display():
  glut.glutSwapBuffers()
  gl.glClearColor(0.5, 0.0, 0.5, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  mudar_cam()
  desenhar_paralelepipedo()
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()

