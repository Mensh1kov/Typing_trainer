from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from sentence import get_sentence


class InputExampleWidget:
    def __init__(self, widget: QWidget):
        self.input_and_example_widget = QtWidgets.QWidget(widget)
        self.input_and_example_widget.setGeometry(QtCore.QRect(50, 100, 700, 150))
        self.input_and_example_widget.setObjectName("input_and_example_widget")
        self.input = QtWidgets.QLineEdit(self.input_and_example_widget)
        self.input.setGeometry(QtCore.QRect(0, 0, 700, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.input.textChanged.connect(lambda: self.on_text_changed())
        self.example = QtWidgets.QLabel(self.input_and_example_widget)
        self.example.setGeometry(QtCore.QRect(3, 35, 694, 60))
        self.example.setFont(font)
        self.example.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.example.setObjectName("example")
        self.example.setText(get_sentence())
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_inf)
        self.lcd_value = 0
        self.mistakes = 0
        self.mistakes_action = None
        self.speed_action = None

    def on_text_changed(self):
        if not self.timer.isActive():
            self.timer.start(1000)
        self.text = self.input.text()
        target_text = self.example.text()
        current_position = self.input.cursorPosition()

        if self.text != target_text[:current_position]:
            self.input.setStyleSheet("background-color: red;")
            self.mistakes += 1

            if self.mistakes_action:
                self.mistakes_action(self.mistakes)
        else:
            self.input.setStyleSheet("background-color: white;")

        if self.text == target_text:
            self.lcd_value = 0
            self.example.setText(get_sentence())
            self.input.setText('')
            self.timer.stop()

    def update_inf(self):
        self.lcd_value += 1
        if self.speed_action:
            self.speed_action(int(len(self.input.text()) / (self.lcd_value / 60)))

    def set_mistakes_action(self, action):
        self.mistakes_action = action

    def set_speed_action(self, action):
        self.speed_action = action
