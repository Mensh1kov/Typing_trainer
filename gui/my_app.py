from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from gui.widgets.info_widget import InfoWidget
from gui.widgets.input_example_widget import InputExampleWidget
from gui.widgets.menubar.menubar import MenuBar
from localizator import load_locale


class MyApp:
    def __init__(self, main_window: QMainWindow):
        locale = load_locale('ru')
        main_window.setWindowTitle(locale.get('window_title'))
        main_window.setObjectName("MainWindow")
        main_window.setFixedSize(800, 600)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.input_example_widget = InputExampleWidget(self.central_widget)
        self.info_widget = InfoWidget(self.central_widget, locale.get('info_widget'))
        self.input_example_widget.set_mistakes_action(self.info_widget.set_mistakes)
        self.input_example_widget.set_speed_action(self.info_widget.set_speed)
        self.menubar = MenuBar(main_window, locale.get('menubar'))
        main_window.setCentralWidget(self.central_widget)

