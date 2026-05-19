#torre do vórtice
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu


def desenhar_cone():
  gl.glClearColor(0.3, 0.5, 0.3, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glColor3f(1, 1, 1)
  glut.glutWireCone(0.5, 0.7, 100, 1)
  glu.gluPerspective(60, 1, 1, 10)
  glu.gluLookAt(0, -2, 2,
                 0, 0, 0.35,
                 0, 0, 1,)
  ''''
  #frontal
  gl.glClearColor(0.3, 0, 0.3, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glColor3f(1, 1, 1)
  glut.glutWireCone(0.5, 0.7, 100, 1)
  glu.gluPerspective(60, 1, 1, 10)
  glu.gluLookAt(0, -2, 0,
                 0, 0, 0.35,
                 0, 0, 1,)

  #lateral
  gl.glClearColor(0.3, 0, 0.3, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glColor3f(1, 1, 1)
  glut.glutWireCone(0.5, 0.7, 100, 1)
  glu.gluPerspective(60, 1, 1, 10)
  glu.gluLookAt(0, -2, 0,
                 0, 0, 0.35,
                 0, 0, 1,)

  #superior
  gl.glClearColor(0.3, 0.5, 0.3, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glColor3f(1, 1, 1)
  glut.glutWireCone(0.5, 0.7, 100, 1)
  glu.gluPerspective(60, 1, 1, 10)
  glu.gluLookAt(0, -2, 2,
                 0, 0, 0.35,
                 0, 0, 1,)
  '''
  glut.glutSwapBuffers()


def display():
  glut.glutSwapBuffers()
  desenhar_cone()




glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()




