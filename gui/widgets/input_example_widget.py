from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class InputExampleWidget:
    def __init__(self, widget: QWidget):
        font = QtGui.QFont()
        font.setPointSize(12)

        self.input_example_widget = QtWidgets.QWidget(widget)
        self.input_example_widget.setGeometry(QtCore.QRect(50, 100, 700, 150))

        self.input = QtWidgets.QLineEdit(self.input_example_widget)
        self.input.setGeometry(QtCore.QRect(0, 0, 700, 30))
        self.input.setFont(font)

        self.example = QtWidgets.QLabel(self.input_example_widget)
        self.example.setGeometry(QtCore.QRect(3, 35, 694, 60))
        self.example.setFont(font)
        self.example.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
