import sys, sqlite3, time

from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QPaintEvent
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QScrollArea, QSizePolicy, QOpenGLWidget, QLayout
from PyQt5.QtCore import Qt, QTimer

from math import pi, sin, cos

from main_design import Ui_MainWindow

import OpenGL.GL as gl

sys.setrecursionlimit(1000000)


class GLWidget(QOpenGLWidget):
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
        # glu.gluPerspective(180, 4 / 3, -1000, 1000)
        # gl.glFrustum(120.0, 1.0, -1.0, 1.0, -1.0, 1.0)

        self.draw_system()

        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex3d(0, 0, 0)
        gl.glVertex3d(0, 0.1, 0)
        gl.glEnd()

        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex3d(0, 0, 0)
        gl.glVertex3d(0, 0, 1)
        gl.glEnd()

        gl.glColor3f(0.0, 0.0, 0.1)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex3d(0, 0, 0)
        gl.glVertex3d(0.1, 0, 0)
        gl.glEnd()

        gl.glPopMatrix()

    def draw_system(self):
        for i in range(self.last_index + 1):
            r = 0.002
            gl.glColor3f(0.0, 0.0, 0.0)
            gl.glBegin(gl.GL_LINES)
            gl.glVertex3d(self.coordinates[i][0] * r, self.coordinates[i][1] * r, 0)
            gl.glVertex3d(self.coordinates[i][2] * r, self.coordinates[i][3] * r, 0)
            gl.glEnd()
        if self.last_index != len(self.coordinates) - 1:
            self.last_index += 1
        self.update()


class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setupUi(self)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.initUi()
        # self.get_params()

    def initUi(self):
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
            params[4] = '\n'.join(list(map(lambda x: x[1:-1], params[4].split(','))))
            con.close()
            self.change_edit(True, params)

    def change_edit(self, bool_, params):
        self.lineEdit_axiom.setReadOnly(bool_)
        self.lineEdit_draw.setReadOnly(bool_)
        self.lineEdit_skip.setReadOnly(bool_)
        self.doubleSpinBox_angle.setReadOnly(bool_)
        self.textEdit.setReadOnly(bool_)

        self.lineEdit_axiom.setText(params[0])
        self.doubleSpinBox_angle.setValue(params[1])
        self.lineEdit_draw.setText(params[2])
        self.lineEdit_skip.setText(params[3])
        self.textEdit.setText(params[4])

    def drawing(self):
        self.openGLWidget.last_index = -1
        self.get_params()
        self.get_coordinates()

    def get_params(self):
        self.d = {'вверх': 0, 'вправо': pi / 2, 'вниз': pi, 'влево': 3 * pi / 2}
        self.start_angle = self.d[self.comboBox_direction.currentText()]
        self.axiom = self.lineEdit_axiom.text()
        self.draw = self.lineEdit_draw.text()
        self.skip = self.lineEdit_skip.text()
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
        self.coordinates = []
        x = self.x
        y = self.y
        self.stack = [(self.x, self.y, self.start_angle)]
        angle_cur = self.start_angle
        for i in self.get_generation(self.generation):
            if i in self.draw:
                if i.isupper():
                    self.coordinates.append([x, y, x + self.step * sin(angle_cur), y + self.step * cos(angle_cur)])
                x += self.step * sin(angle_cur)
                y += self.step * cos(angle_cur)
            elif i == '+':
                angle_cur += self.angle
            elif i == '-':
                angle_cur -= self.angle
            elif i == '[':
                self.stack.append((x,
                                   y, angle_cur))
            elif i == ']':
                x = self.stack[-1][0]
                y = self.stack[-1][1]
                angle_cur = self.stack[-1][2]
                self.stack.pop()
        # print(self.coordinates)
        self.openGLWidget.coordinates = self.coordinates[::]

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

    # def mousePressEvent(self, event):
    #     self.x = event.x()
    #     self.y = event.y()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    try:
        ex = MenuWindow(rect.width(), rect.height())
        ex.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e)
