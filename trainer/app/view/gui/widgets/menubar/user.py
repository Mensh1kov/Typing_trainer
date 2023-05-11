from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMenu


class User(QMenu):
    def __init__(self, menubar: QMenuBar, locale: dict):
        super().__init__(menubar)
        self.change_user = QtWidgets.QAction(menubar.window())
        self.statistics = QtWidgets.QAction(menubar.window())
        self.addAction(self.change_user)
        self.addAction(self.statistics)
        self.set_locale(locale)
        menubar.addAction(self.menuAction())

    def set_locale(self, locale: dict):
        self.setTitle(locale.get('title'))
        self.change_user.setText(locale.get('change_user'))
        self.statistics.setText(locale.get('statistics'))
