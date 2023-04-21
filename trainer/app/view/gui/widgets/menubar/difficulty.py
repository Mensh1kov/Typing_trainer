from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar


class Difficulty:
    def __init__(self, menubar: QMenuBar, locale: dict):
        self.menu = QtWidgets.QMenu(menubar)

        self.simple = QtWidgets.QAction(menubar.window())
        self.simple.setCheckable(True)

        self.medium = QtWidgets.QAction(menubar.window())
        self.medium.setCheckable(True)

        self.hard = QtWidgets.QAction(menubar.window())
        self.hard.setCheckable(True)

        self.legendary = QtWidgets.QAction(menubar.window())
        self.legendary.setCheckable(True)

        self.menu.addAction(self.simple)
        self.menu.addAction(self.medium)
        self.menu.addAction(self.hard)
        self.menu.addAction(self.legendary)

        self.set_locale(locale)
        menubar.addAction(self.menu.menuAction())

    def set_locale(self, locale: dict):
        self.menu.setTitle(locale.get('title'))
        self.simple.setText(locale.get('simple'))
        self.medium.setText(locale.get('medium'))
        self.hard.setText(locale.get('hard'))
        self.legendary.setText(locale.get('legendary'))
