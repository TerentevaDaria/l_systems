import sys, sqlite3

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtCore import Qt, QTimer, pyqtSignal

from math import pi, sin, cos

from main_design import Ui_MainWindow

import OpenGL.GL as gl

import numpy as np

sys.setrecursionlimit(1000000)


class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.last_index = -1

        self.coordinates = []

        timer = QTimer(self)
        timer.timeout.connect(self.draw_system)
        timer.start(4)

    def initializeGL(self):
        gl.glClearColor(1, 1, 1, 0)
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glEnable(gl.GL_LIGHTING)

        lightPos = [100, 100, 100, 0]
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_DEPTH_TEST)

        gl.glTranslatef(0.0, 0.0, 0.0)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()
        gl.glLoadIdentity()
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

        self.draw_system()

        gl.glPopMatrix()

    def draw_system(self):
        for i in range(1, self.last_index + 1):
            r = 0.002
            gl.glColor3f(0.0, 0.0, 0.0)
            gl.glBegin(gl.GL_LINES)
            gl.glVertex3d(self.coordinates[i][0][0] * r, self.coordinates[i][0][1] * r, self.coordinates[i][0][2] * r)
            gl.glVertex3d(self.coordinates[i][1][0] * r, self.coordinates[i][1][1] * r, self.coordinates[i][1][2] * r)
            gl.glEnd()
        if self.last_index != len(self.coordinates) - 1:
            self.last_index += 1
        self.update()

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()

    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360 * 16
        while (angle > 360 * 16):
            angle -= 360 * 16
        return angle


class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setupUi(self)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.initUi()

    def initUi(self):
        self.setWindowTitle('L-system')

        self.openGLWidget = GLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(400, 10, 141, 541))
        self.openGLWidget.setObjectName("openGLWidget")

        con = sqlite3.connect('systems.db')
        cur = con.cursor()
        self.examples = ['Другой вариант'] + list(
            map(lambda x: x[0], list(cur.execute("""SELECT name from systems""").fetchall())))
        con.close()

        self.comboBox.insertItems(0, self.examples)
        self.comboBox.currentTextChanged.connect(self.set_params)
        self.pushButton_confirm.clicked.connect(self.drawing)
        self.openGLWidget.resize(self.height - 50, self.height - 50)  # check
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.showMaximized()

    def set_params(self):
        choice = self.comboBox.currentText().lstrip().rstrip()
        if choice == 'Другой вариант':
            default = ['', 90, '', '', '']
            self.change_edit(False, default)
        else:
            con = sqlite3.connect('systems.db')
            cur = con.cursor()
            params = list(cur.execute(f"""SELECT * FROM systems
                            WHERE name='{choice}'""").fetchone()[2:])
            params[3] = '\n'.join(list(map(lambda x: x[1:-1], params[3].split(','))))
            con.close()
            self.change_edit(True, params)

    def change_edit(self, bool_, params):
        self.lineEdit_axiom.setReadOnly(bool_)
        self.lineEdit_draw.setReadOnly(bool_)
        self.doubleSpinBox_angle.setReadOnly(bool_)
        self.textEdit.setReadOnly(bool_)

        self.lineEdit_axiom.setText(params[0])
        self.doubleSpinBox_angle.setValue(params[1])
        self.lineEdit_draw.setText(params[2])
        self.textEdit.setText(params[3])

    def drawing(self):
        self.openGLWidget.last_index = -1
        self.get_params()
        self.get_coordinates()

    def get_params(self):
        self.axiom = self.lineEdit_axiom.text()
        self.draw = self.lineEdit_draw.text()
        self.angle = float(self.doubleSpinBox_angle.text().replace(',', '.')) * pi / 180
        self.ruls = {}
        ruls_ = self.textEdit.toPlainText()
        if ruls_:
            for i in ruls_.split('\n'):
                key, value = i.split(':')
                self.ruls[key] = value
        self.step = int(self.spinBox_step.text())
        self.generation = int(self.spinBox_generation.text())

    def get_coordinates(self):
        self.coordinates = [[np.matrix([[0], [0], [0]]), np.matrix([[0], [0], [0]])]]
        matrix = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.stack = [[self.coordinates[0], matrix]]
        for i in self.get_generation(self.generation):
            if i in self.draw:
                if i.isupper():
                    self.coordinates.append([self.coordinates[-1][1], self.step * matrix.dot(np.matrix([[-1], [0], [0]])) + self.coordinates[-1][1]])
            elif i == '+':
                u_rot = np.matrix([[cos(self.angle), sin(self.angle), 0], [-sin(self.angle), cos(self.angle), 0], [0, 0, 1]])
                matrix = matrix.dot(u_rot)
            elif i == '-':
                u_rot = np.matrix(
                    [[cos(-self.angle), sin(-self.angle), 0], [-sin(-self.angle), cos(-self.angle), 0], [0, 0, 1]])
                matrix = matrix.dot(u_rot)
            elif i == '&':
                l_rot = np.matrix([[cos(self.angle), 0, -sin(self.angle)], [0, 1, 0], [sin(self.angle), 0, cos(self.angle)]])
                matrix = matrix.dot(l_rot)
            elif i == '^':
                l_rot = np.matrix([[cos(-self.angle), 0, -sin(-self.angle)], [0, 1, 0], [sin(-self.angle), 0, cos(-self.angle)]])
                matrix = matrix.dot(l_rot)
            elif i == '\\':
                h_rot = np.matrix([[1, 0, 0], [0, cos(self.angle), -sin(self.angle)], [0, sin(self.angle), cos(self.angle)]])
                matrix = matrix.dot(h_rot)
            elif i == '/':
                h_rot = np.matrix([[1, 0, 0], [0, cos(-self.angle), -sin(-self.angle)], [0, sin(-self.angle), cos(-self.angle)]])
                matrix = matrix.dot(h_rot)
            elif i == '|':
                u_rot = np.matrix([[cos(pi), sin(pi), 0], [-sin(pi), cos(pi), 0], [0, 0, 1]])
                matrix = matrix.dot(u_rot)
            elif i == '[':
                self.stack.append([self.coordinates[-1][1], matrix])
            elif i == ']':
                matrix = self.stack[-1][1]
                self.coordinates.append([self.stack[-1][0], self.stack[-1][0]])
                self.stack.pop()
        self.openGLWidget.coordinates = list(map(lambda x: [[x[0][0][0], x[0][1][0], x[0][2][0]], [x[1][0][0], x[1][1][0], x[1][2][0]]], self.coordinates[::]))

    def get_generation(self, n):
        s = self.axiom
        for i in range(n):
            s1 = ''
            for j in s:
                if j in self.ruls:
                    s1 += self.ruls[j]
                else:
                    s1 += j
            s = s1[::]
        j = 0
        for i in range(len(s)):
            if s[i] not in ['+', '-']:
                j = i
                break
        return s[j:]


if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    ex = MenuWindow(rect.width(), rect.height())
    ex.show()
    sys.exit(app.exec())
