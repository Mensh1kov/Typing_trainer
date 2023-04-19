from PyQt5 import QtWidgets
from app.app_controller import AppController
from app.app_model import AppModel
from gui.app_view import AppView

RU = 'ru'


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    model = AppModel()
    view = AppView(main_window, model.get_locale(RU))
    AppController(model, view)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
