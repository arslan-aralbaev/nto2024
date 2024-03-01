# Разработан визуальный интерфейс:
#  - Имеется кнопка начала измерения.
#  - Имеется поле ввода расстояния между губками.
#  - Имеется поле вывода результата измерения.
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication,
                             QLineEdit, QDoubleSpinBox,
                             QTextEdit, QPushButton,
                             QTabWidget)

types_of_fiber = ["красивый", "хрупкий", "аоаоаоаооо", "нежный", "жестокий"]


class Example(QWidget):
    def __init__(self, typeOfFiber):
        super().__init__()
        self.params = None
        self.main = None
        self.tabWidget = None
        self.line_for_answer = None
        self.calc_button = None
        self.title_for_answer = None
        self.rast_input = None
        self.title_of_input = None
        self.el_shift = [0, 0]  # сдвиг элементов интерфейса формат: [x, y]
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Начать измеренияяяяяя!!!')
        self.initUI()
        self.show()

    def initUI(self):
        # виджет переключения меню
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 361))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        # Меню
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("Главная")

        # Параметры
        self.params = QtWidgets.QWidget()
        self.params.setObjectName("Параметры")

        # 1) поле для ввода диаметра
        self.title_of_input = QLabel(self.params)
        self.title_of_input.setText('расстояния между губками')
        self.title_of_input.move(10 + self.el_shift[0], 10 + self.el_shift[1])
        self.rast_input = QDoubleSpinBox(self.params)
        self.rast_input.setSingleStep(0.01)
        self.rast_input.move(200 + self.el_shift[0], 10 + self.el_shift[1])

        # окно ответа + заголовок
        self.title_for_answer = QLabel(self)
        self.title_for_answer.setText('Результат')
        self.title_for_answer.move(10 + self.el_shift[0], 50 + self.el_shift[1])
        self.line_for_answer = QLineEdit(self)
        self.line_for_answer.setEnabled(False)
        self.line_for_answer.move(140 + self.el_shift[0], 50 + self.el_shift[1])

        # бутон
        self.calc_button = QPushButton(self)
        self.calc_button.setText('Начать измерения!')
        self.calc_button.move(10 + self.el_shift[0], 90 + self.el_shift[1])
        self.calc_button.clicked.connect(self.result)

    def result(self):
        rast = self.rast_input.value()  # снимаем значения диаметра

        self.line_for_answer.setText(str(rast)[:4])  # сюда выводить инфу


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(types_of_fiber)
    sys.exit(app.exec_())
