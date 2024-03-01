import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication,
                             QLineEdit, QDoubleSpinBox,
                             QTextEdit, QPushButton, QTabWidget)

types_of_fiber = ["красивый", "хрупкий", "аоаоаоаооо", "нежный", "жестокий"]


class Example(QWidget):
    def __init__(self, typeOfFiber):
        super().__init__()
        self.w = 500
        self.h = 300
        self.main = None
        self.params = None
        self.tabWidget = None
        self.line_for_answer = None
        self.calc_button = None
        self.title_for_answer = None
        self.type_of_fiber = None
        self.diametr_input = None
        self.title_of_input = None
        self.title_for_box = None
        self.typeOfFiber = typeOfFiber
        self.el_shift = [0, 0]  # сдвиг элементов интерфейса формат: [x, y]
        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle('Ляляляля')
        self.initUI()
        self.show()

    def initUI(self):
        # виджет переключения меню
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, self.w - 20, self.h - 20))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
    # Главная
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("Главная")
        # окно ответа + заголовок
        self.title_for_answer = QLabel(self.main)
        self.title_for_answer.setText('динам. усталость')
        self.title_for_answer.move(10 + self.el_shift[0], 90 + self.el_shift[1])
        self.line_for_answer = QLineEdit(self.main)
        self.line_for_answer.setEnabled(False)
        self.line_for_answer.move(140 + self.el_shift[0], 90 + self.el_shift[1])

        # бутон
        self.calc_button = QPushButton(self.main)
        self.calc_button.setText('калибровка!')

    # Параметры
        self.params = QtWidgets.QWidget()
        self.params.setObjectName("Параметры")

        # выпадающий список типов волокна
        self.title_for_box = QLabel(self.params)
        self.title_for_box.setText('тип волокна')
        self.title_for_box.move(10 + self.el_shift[0], 10 + self.el_shift[1])
        self.title_for_box.setGeometry(10, 13, 100, 20)
        self.type_of_fiber = QComboBox(self.params)
        self.type_of_fiber.addItems(self.typeOfFiber)
        self.type_of_fiber.move(200 + self.el_shift[0], 10 + self.el_shift[1])

        # поле для ввода диаметра
        self.title_of_input = QLabel(self.params)
        self.title_of_input.setText('диаметр волокна')
        self.title_of_input.move(10 + self.el_shift[0], 50 + self.el_shift[1])
        self.diametr_input = QDoubleSpinBox(self.params)
        self.diametr_input.setSingleStep(0.01)
        self.diametr_input.move(200 + self.el_shift[0], 50 + self.el_shift[1])

        # диаметр оболочки волокна
        self.title_of_input = QLabel(self.params)
        self.title_of_input.setText('диаметр оболочки волокна')
        self.title_of_input.move(10 + self.el_shift[0], 90 + self.el_shift[1])
        self.diametr_input = QDoubleSpinBox(self.params)
        self.diametr_input.setSingleStep(0.01)
        self.diametr_input.move(200 + self.el_shift[0], 90 + self.el_shift[1])


        self.tabWidget.addTab(self.main, 'Главная')
        self.tabWidget.addTab(self.params, 'Параметры')


        self.calc_button.move(10 + self.el_shift[0], 130 + self.el_shift[1])
        self.calc_button.clicked.connect(self.calculate)

    def calculate(self):
        # здесь проходят все вычисления и вывод результата после нажатия кнопки
        typw = self.type_of_fiber.currentText()  # берём выбранный тип волокна
        diametr = self.diametr_input.value()  # снимаем значения диаметра

        self.line_for_answer.setText(str(typw) + ' ' + str(diametr))  # сюда выводить инфу


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(types_of_fiber)
    sys.exit(app.exec_())
