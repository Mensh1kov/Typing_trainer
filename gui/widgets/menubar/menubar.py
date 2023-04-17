from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from gui.widgets.menubar.difficulty import Difficulty
from gui.widgets.menubar.language import Language
from gui.widgets.menubar.user import User


class MenuBar:
    def __init__(self, window: QMainWindow, locale: dict):
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.user = User(self.menubar, locale)
        self.language = Language(self.menubar, locale)
        self.difficulty = Difficulty(self.menubar, locale)
        self.set_locale(locale)
        window.setMenuBar(self.menubar)

    def set_locale(self, locale: dict):
        self.user.set_locale(locale.get('user'))
        self.language.set_locale(locale.get('language'))
        self.difficulty.set_locale(locale.get('difficulty'))
