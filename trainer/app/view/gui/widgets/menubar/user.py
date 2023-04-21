from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar


class User:
    def __init__(self, menubar: QMenuBar, locale: dict):
        self.user = QtWidgets.QMenu(menubar)
        self.user.setObjectName("user")
        self.change_user = QtWidgets.QAction(menubar.window())
        self.change_user.setObjectName("change_user")
        self.statistics = QtWidgets.QAction(menubar.window())
        self.statistics.setObjectName("statistics")
        self.user.addAction(self.change_user)
        self.user.addAction(self.statistics)
        self.set_locale(locale)
        menubar.addAction(self.user.menuAction())

    def set_locale(self, locale: dict):
        self.user.setTitle(locale.get('title'))
        self.change_user.setText(locale.get('change_user'))
        self.statistics.setText(locale.get('statistics'))
