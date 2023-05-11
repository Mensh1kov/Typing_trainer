from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMenu


class Difficulty(QMenu):
    def __init__(self, menubar: QMenuBar, locale: dict):
        super().__init__(menubar)

        self.simple = QtWidgets.QAction(menubar.window())
        self.simple.setCheckable(True)

        self.medium = QtWidgets.QAction(menubar.window())
        self.medium.setCheckable(True)

        self.hard = QtWidgets.QAction(menubar.window())
        self.hard.setCheckable(True)

        self.legendary = QtWidgets.QAction(menubar.window())
        self.legendary.setCheckable(True)

        self.addAction(self.simple)
        self.addAction(self.medium)
        self.addAction(self.hard)
        self.addAction(self.legendary)

        self.set_locale(locale)
        menubar.addAction(self.menuAction())

    def set_locale(self, locale: dict):
        self.setTitle(locale.get('title'))
        self.simple.setText(locale.get('simple'))
        self.medium.setText(locale.get('medium'))
        self.hard.setText(locale.get('hard'))
        self.legendary.setText(locale.get('legendary'))
