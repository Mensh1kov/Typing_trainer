from PyQt5 import QtWidgets
from app_controller import AppController
from app_model import AppModel
from gui.app_view import AppView
from localizator import load_locale


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    view = AppView(main_window, load_locale('ru'))
    model = AppModel()
    AppController(model, view)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
