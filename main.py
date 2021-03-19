import sys
import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtCore import Qt, QTimer, pyqtSignal

from math import pi, sin, cos

import OpenGL.GL as gl

import numpy as np

sys.setrecursionlimit(1000000)


class Ui_MainWindow(object):
    """дизайн приложения"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_draw = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_draw.setObjectName("lineEdit_draw")
        self.horizontalLayout_3.addWidget(self.lineEdit_draw)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_step = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_step.setMinimum(1)
        self.spinBox_step.setMaximum(100)
        self.spinBox_step.setObjectName("spinBox_step")
        self.horizontalLayout_4.addWidget(self.spinBox_step)
        self.gridLayout.addLayout(self.horizontalLayout_4, 15, 0, 1, 1)
        self.lineEdit_axiom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_axiom.setObjectName("lineEdit_axiom")
        self.gridLayout.addWidget(self.lineEdit_axiom, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.doubleSpinBox_angle = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_angle.setDecimals(1)
        self.doubleSpinBox_angle.setMaximum(180.0)
        self.doubleSpinBox_angle.setSingleStep(0.1)
        self.doubleSpinBox_angle.setProperty("value", 90.0)
        self.doubleSpinBox_angle.setObjectName("doubleSpinBox_angle")
        self.horizontalLayout.addWidget(self.doubleSpinBox_angle)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinBox_generation = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_generation.setMaximum(50)
        self.spinBox_generation.setProperty("value", 1)
        self.spinBox_generation.setObjectName("spinBox_generation")
        self.horizontalLayout_6.addWidget(self.spinBox_generation)
        self.gridLayout.addLayout(self.horizontalLayout_6, 16, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton_confirm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout.addWidget(self.pushButton_confirm, 18, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 17, 0, 1, 1)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(400, 10, 141, 541))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 560, 381, 41))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(10, 610, 381, 41))
        self.label_res.setText("")
        self.label_res.setObjectName("label_res")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Аксиома:"))
        self.label_7.setText(_translate("MainWindow", "Использовать для рисования"))
        self.label_2.setText(_translate("MainWindow", "длина шага"))
        self.label_3.setText(_translate("MainWindow", "Угол"))
        self.label_5.setText(_translate("MainWindow", "поколение"))
        self.label_4.setText(_translate("MainWindow", "Правила:"))
        self.pushButton_confirm.setText(_translate("MainWindow", "Построить"))
        self.checkBox.setText(_translate("MainWindow", "Анимация"))


class GLWidget(QOpenGLWidget):
    """работа с графикой"""
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
        """инициализация PyOpenGL"""
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
        """отрисовка кадра"""
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
        """отрисовка отрезков с заданными в self.coordinates координатами в масштабе"""
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
        """задание угла поворота вокруг оси Ох"""
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        """задание угла поворота вокруг оси Оy"""
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        """задание угла поворота вокруг оси Оz"""
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def mousePressEvent(self, event):
        """точка, в которой была зажата кнопка мыши"""
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        """преобразование движения мыши с зажатой кнопкой в углы поворота изображения"""
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
        """нормализация угла поворота"""
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
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
        """начальная настройка приложения"""
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
        """получение и задание новых параметров при изменении текущей L-системы"""
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
        """смена возможности изменять значения виджетов и заполнение их параметрами"""
        self.lineEdit_axiom.setReadOnly(bool_)
        self.lineEdit_draw.setReadOnly(bool_)
        self.doubleSpinBox_angle.setReadOnly(bool_)
        self.textEdit.setReadOnly(bool_)

        self.lineEdit_axiom.setText(params[0])
        self.doubleSpinBox_angle.setValue(params[1])
        self.lineEdit_draw.setText(params[2])
        self.textEdit.setText(params[3])
        self.label_error.setText('')

    def drawing(self):
        """запуск отрисовки при нажатии кнопки Построить"""
        self.label_error.setText('')
        self.openGLWidget.last_index = -1
        self.get_params()
        self.get_coordinates()

    def get_params(self):
        """Получение заданных параметров из виджетов"""
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
        """формирование списка с координатами отрезков"""
        prev = np.matrix([[0], [0], [0]])
        self.coordinates = [[prev, prev]]
        matrix = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.stack = [[prev, matrix]]
        for i in self.get_generation(self.generation):
            if i in self.draw:
                if i.isupper():
                    self.coordinates.append([prev, self.step * matrix.dot(np.matrix([[-1], [0], [0]])) + prev])
                prev = self.step * matrix.dot(np.matrix([[-1], [0], [0]])) + prev
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
                self.stack.append([prev, matrix])
            elif i == ']':
                matrix = self.stack[-1][1]
                prev = self.stack[-1][0]
                self.coordinates.append([self.stack[-1][0], self.stack[-1][0]])
                self.stack.pop()
        self.openGLWidget.last_index = len(self.coordinates) - 1 if not self.checkBox.isChecked() else -1
        self.openGLWidget.coordinates = list(map(lambda x: [[x[0][0][0], x[0][1][0], x[0][2][0]], [x[1][0][0], x[1][1][0], x[1][2][0]]], self.coordinates[::]))

    def get_generation(self, n):
        """получение поколения по его номеру"""
        s = self.axiom
        for i in range(n):
            s1 = ''
            cnt = 0
            for j in s:
                if j in self.ruls:
                    s1 += self.ruls[j]
                    cnt += 1
                else:
                    s1 += j
                if cnt > 1000:
                    self.label_error.setText(f'Превышено допустимое время построения системы.\nЗначение поколения уменьшено до {i}')
                    return s
            s = s1[::]
        return s


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
