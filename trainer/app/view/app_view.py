from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from trainer.app.view.gui.widgets.info_widget import InfoWidget
from trainer.app.view.gui.widgets.input_example_widget \
    import InputExampleWidget
from trainer.app.view.gui.widgets.menubar.menubar import MenuBar
from trainer.app.view.gui.widgets.stat_dialog import StatDialog
from trainer.app.view.gui.widgets.time_up_dialog import TimeUpDialog
from trainer.app.view.gui.widgets.user_dialog import UserDialog


class AppView:
    def __init__(self, main_window: QMainWindow, locale: dict):
        self.main_window = main_window
        main_window.setWindowTitle(locale.get('window_title'))
        main_window.setFixedSize(800, 600)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.user_dialog = UserDialog(main_window, locale.get('user_dialog'))
        self.stat_dialog = StatDialog(main_window, locale.get('stat_dialog'))
        self.time_up_dialog = TimeUpDialog(main_window,
                                           locale.get('time_up_dialog'))
        self.input_example_widget = InputExampleWidget(self.central_widget)
        self.info_widget = InfoWidget(self.central_widget,
                                      locale.get('info_widget'))
        self.menubar = MenuBar(main_window, locale.get('menubar'))

        main_window.setCentralWidget(self.central_widget)

    def set_locale(self, locale: dict):
        self.main_window.setWindowTitle(locale.get('window_title'))
        self.user_dialog.set_locale(locale.get('user_dialog'))
        self.stat_dialog.set_locale(locale.get('stat_dialog'))
        self.info_widget.set_locale(locale.get('info_widget'))
        self.menubar.set_locale(locale.get('menubar'))
        self.time_up_dialog.set_locale(locale.get('time_up_dialog'))
