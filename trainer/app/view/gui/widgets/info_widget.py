from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtCore, QtGui


class InfoWidget(QWidget):
    def __init__(self, widget: QWidget, locale: dict):
        super().__init__(widget)
        self.locale = locale
        font = QtGui.QFont()
        font.setPointSize(12)

        self.setGeometry(QtCore.QRect(50, 30, 700, 51))

        self.mistakes = QtWidgets.QLabel(self)
        self.mistakes.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.mistakes.setFont(font)

        self.speed = QtWidgets.QLabel(self)
        self.speed.setGeometry(QtCore.QRect(200, 0, 150, 30))
        self.speed.setFont(font)

        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.locale = locale
        self.mistakes.setText(locale.get('mistakes'))
        self.speed.setText(locale.get('speed'))

    def set_mistakes(self, mistakes: int):
        self.mistakes.setText(f'{self.locale.get("mistakes")}: {mistakes}')

    def set_speed(self, speed: int):
        self.speed.setText(f'{self.locale.get("speed")}: {speed}')
