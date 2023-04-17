from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar


class Language:
    def __init__(self, menubar: QMenuBar, locale: dict):
        self.language = QtWidgets.QMenu(menubar)
        self.language.setObjectName("language")
        self.Russian = QtWidgets.QAction(menubar.window())
        self.Russian.setObjectName("Russian")
        self.English = QtWidgets.QAction(menubar.window())
        self.English.setObjectName("English")
        self.language.addAction(self.Russian)
        self.language.addAction(self.English)
        self.set_locale(locale)
        menubar.addAction(self.language.menuAction())

    def set_locale(self, locale: dict):
        self.language.setTitle(locale.get('title'))
        self.Russian.setText(locale.get('ru'))
        self.English.setText(locale.get('en'))
