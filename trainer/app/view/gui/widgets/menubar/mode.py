from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMenu


class Mode(QMenu):
    def __init__(self, menubar: QMenuBar, locale: dict):
        super().__init__(menubar)
        self.normal = QtWidgets.QAction(menubar.window())
        self.time = QtWidgets.QAction(menubar.window())

        self.normal.setCheckable(True)
        self.time.setCheckable(True)

        self.addAction(self.normal)
        self.addAction(self.time)
        self.set_locale(locale)
        menubar.addAction(self.menuAction())

    def set_locale(self, locale: dict):
        self.setTitle(locale.get('title'))
        self.normal.setText(locale.get('normal'))
        self.time.setText(locale.get('time'))
