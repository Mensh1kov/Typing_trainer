from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class InputExampleWidget(QWidget):
    def __init__(self, widget: QWidget):
        super().__init__(widget)
        font = QtGui.QFont()
        font.setPointSize(12)

        self.setGeometry(QtCore.QRect(50, 100, 700, 330))

        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(QtCore.QRect(0, 0, 700, 30))
        self.input.setFont(font)

        self.example = QtWidgets.QLabel(self)
        self.example.setGeometry(QtCore.QRect(3, 35, 694, 300))
        self.example.setFont(font)
        self.example.setWordWrap(True)
        self.example.setAlignment(QtCore.Qt.AlignLeading |
                                  QtCore.Qt.AlignLeft |
                                  QtCore.Qt.AlignTop)
