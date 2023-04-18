from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtCore, QtGui


class InfoWidget:
    def __init__(self, widget: QWidget, locale: dict):
        self.locale = locale
        self.info_widget = QtWidgets.QWidget(widget)
        self.info_widget.setGeometry(QtCore.QRect(50, 30, 700, 51))
        self.info_widget.setObjectName("info_widget")
        self.mistakes = QtWidgets.QLabel(self.info_widget)
        self.mistakes.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.mistakes.setFont(self.font)
        self.mistakes.setObjectName("mistakes")
        self.speed = QtWidgets.QLabel(self.info_widget)
        self.speed.setGeometry(QtCore.QRect(200, 0, 150, 30))
        self.speed.setFont(self.font)
        self.speed.setObjectName("speed")
        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.locale = locale
        self.mistakes.setText(locale.get('mistakes'))
        self.speed.setText(locale.get('speed'))

    def set_mistakes(self, mistakes: int):
        self.mistakes.setText(f'{self.locale.get("mistakes")} {mistakes}')

    def set_speed(self, speed: int):
        self.speed.setText(f'{self.locale.get("speed")} {speed}')
