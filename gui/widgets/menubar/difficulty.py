from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar


class Difficulty:
    def __init__(self, menubar: QMenuBar, locale: dict):
        self.difficulty = QtWidgets.QMenu(menubar)
        self.difficulty.setObjectName("difficulty")
        self.simple = QtWidgets.QAction(menubar.window())
        self.simple.setObjectName("simple")
        self.medium = QtWidgets.QAction(menubar.window())
        self.medium.setObjectName("medium")
        self.hard = QtWidgets.QAction(menubar.window())
        self.hard.setObjectName("hard")
        self.legendary = QtWidgets.QAction(menubar.window())
        self.legendary.setObjectName("legendary")
        self.difficulty.addAction(self.simple)
        self.difficulty.addAction(self.medium)
        self.difficulty.addAction(self.hard)
        self.difficulty.addAction(self.legendary)
        menubar.addAction(self.difficulty.menuAction())

    def set_locale(self, locale: dict):
        self.difficulty.setTitle(locale.get('title'))
        self.simple.setText(locale.get('simple'))
        self.medium.setText(locale.get('medium'))
        self.hard.setText(locale.get('hard'))
        self.legendary.setText(locale.get('legendary'))


