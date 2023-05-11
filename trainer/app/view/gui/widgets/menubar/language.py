from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMenu


class Language(QMenu):
    def __init__(self, menubar: QMenuBar, locale: dict):
        super().__init__(menubar)
        self.Russian = QtWidgets.QAction(menubar.window())
        self.English = QtWidgets.QAction(menubar.window())

        self.Russian.setCheckable(True)
        self.English.setCheckable(True)

        self.addAction(self.Russian)
        self.addAction(self.English)
        self.set_locale(locale)
        menubar.addAction(self.menuAction())

    def set_locale(self, locale: dict):
        self.setTitle(locale.get('title'))
        self.Russian.setText(locale.get('ru'))
        self.English.setText(locale.get('en'))
