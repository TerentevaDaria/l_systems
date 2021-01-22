import sys, sqlite3, time

from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QPaintEvent
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer

from math import pi, sin, cos

from main_design import Ui_MainWindow

sys.setrecursionlimit(1000000)


class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setupUi(self)
        self.width = width
        self.height = height
        self.x = width // 2
        self.y = height // 2
        self.initUi()
        self.get_params()

    def initUi(self):
        con = sqlite3.connect('systems.db')
        cur = con.cursor()
        self.last_i = 0
        self.coordinates = []
        self.flag = False
        self.examples = ['Другой вариант'] + list(
            map(lambda x: x[0], list(cur.execute("""SELECT name from systems""").fetchall())))
        con.close()

        self.comboBox.insertItems(0, self.examples)
        self.comboBox.currentTextChanged.connect(self.set_params)
        self.pushButton_confirm.clicked.connect(self.drawing)

        self.resize(self.width, self.width)
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
        self.last_i = 0
        self.get_params()
        self.get_coordinates()
        self.flag = True

    def get_params(self):
        self.d = {'вверх': pi, 'вправо': pi / 2, 'вниз': 0, 'влево': 3 * pi / 2}
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
        print(self.coordinates)

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

    def draw_l_system(self, painter):
        self.flag = False
        for i in range(0, self.last_i):
            if self.coordinates[i][2]:
                painter.drawLine(*self.coordinates[i])
        QTimer.singleShot(2000, self.update)
        if self.last_i != len(self.coordinates):
            self.flag = True
            self.last_i += 1
        else:
            self.last_i = 0
        self.update()

    def draw_l_system2(self, painter):
        for i in range(0, len(self.coordinates)):
            if self.coordinates[i][2]:
                painter.drawLine(*self.coordinates[i])
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2))

        if self.flag:
            self.draw_l_system(painter)
        else:
            self.draw_l_system2(painter)

        dot_painter = QPainter()
        dot_painter.begin(self)
        dot_painter.setRenderHint(QPainter.Antialiasing)
        dot_painter.setPen(QPen(Qt.red, 3))
        dot_painter.drawLine(self.x, self.y, self.x + 1, self.y)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()


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
