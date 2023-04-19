from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar


class Language:
    def __init__(self, menubar: QMenuBar, locale: dict):
        self.menu = QtWidgets.QMenu(menubar)
        self.Russian = QtWidgets.QAction(menubar.window())
        self.English = QtWidgets.QAction(menubar.window())
        self.menu.addAction(self.Russian)
        self.menu.addAction(self.English)
        self.set_locale(locale)
        menubar.addAction(self.menu.menuAction())

    def set_locale(self, locale: dict):
        self.menu.setTitle(locale.get('title'))
        self.Russian.setText(locale.get('ru'))
        self.English.setText(locale.get('en'))
