import sys, sqlite3, time

from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush
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
        self.examples = ['Другой вариант'] + list(cur.execute("""SELECT name from systems""").fetchall()[0])
        con.close()

        self.comboBox.insertItems(0, self.examples)
        self.comboBox.currentTextChanged.connect(self.set_params)
        self.confirmPushButton.clicked.connect(self.get_params)

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
        self.axiomLineEdit.setReadOnly(bool_)
        self.drawLineEdit.setReadOnly(bool_)
        self.skipLineEdit.setReadOnly(bool_)
        self.angleSpinBox.setReadOnly(bool_)
        self.textEdit.setReadOnly(bool_)

        self.axiomLineEdit.setText(params[0])
        self.angleSpinBox.setValue(params[1])
        self.drawLineEdit.setText(params[2])
        self.skipLineEdit.setText(params[3])
        self.textEdit.setText(params[4])

    def get_params(self):
        self.axiom = self.axiomLineEdit.text()
        self.draw = self.drawLineEdit.text()
        self.skip = self.skipLineEdit.text()
        self.angle = int(self.angleSpinBox.text()) * pi / 180
        self.ruls = {}
        ruls_ = self.textEdit.toPlainText()
        if ruls_:
            for i in ruls_.split('\n'):
                key, value = i.split(':')
                self.ruls[key] = value
        self.step = int(self.stepSpinBox.text())
        self.generation = int(self.generationSpinBox.text())

    def draw_l_system(self, painter):
        x = self.x
        y = self.y
        angle_cur = 0
        for i in self.get_generation(self.generation):
            if i in self.draw:
                painter.drawLine(x, y, int(x + self.step * sin(angle_cur)), int(y + self.step * cos(angle_cur)))
                x = int(x + self.step * sin(angle_cur))
                y = int(y + self.step * cos(angle_cur))
            elif i == '+':
                angle_cur += self.angle
            elif i == '-':
                angle_cur -= self.angle
        self.update()

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
        return s

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2))
        self.draw_l_system(painter)

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