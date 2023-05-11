from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMenuBar
from trainer.app.view.gui.widgets.menubar.difficulty import Difficulty
from trainer.app.view.gui.widgets.menubar.language import Language
from trainer.app.view.gui.widgets.menubar.mode import Mode
from trainer.app.view.gui.widgets.menubar.user import User


class MenuBar(QMenuBar):
    def __init__(self, window: QMainWindow, locale: dict):
        super().__init__(window)
        self.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.user = User(self, locale.get('user'))
        self.language = Language(self, locale.get('language'))
        self.difficulty = Difficulty(self, locale.get('difficulty'))
        self.mode = Mode(self, locale.get('mode'))

        self.set_locale(locale)
        window.setMenuBar(self)

    def set_locale(self, locale: dict):
        self.user.set_locale(locale.get('user'))
        self.language.set_locale(locale.get('language'))
        self.difficulty.set_locale(locale.get('difficulty'))
        self.mode.set_locale(locale.get('mode'))
