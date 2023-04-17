from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class InputExampleWidget:
    def __init__(self, widget: QWidget):
        self.input_and_example_widget = QtWidgets.QWidget(widget)
        self.input_and_example_widget.setGeometry(QtCore.QRect(50, 100, 700, 150))
        self.input_and_example_widget.setObjectName("input_and_example_widget")
        self.input = QtWidgets.QLineEdit(self.input_and_example_widget)
        self.input.setGeometry(QtCore.QRect(0, 0, 700, 30))
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.input.setFont(self.font)
        self.input.setObjectName("input")
        self.example = QtWidgets.QLabel(self.input_and_example_widget)
        self.example.setGeometry(QtCore.QRect(3, 35, 694, 60))
        self.example.setFont(self.font)
        self.example.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.example.setObjectName("example")

    def set_example(self, example: str):
        self.example.setText(example)
