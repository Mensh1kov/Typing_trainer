from PyQt5 import QtWidgets
from trainer.app.controller.app_controller import AppController
from trainer.app.model.app_model import AppModel
from trainer.app.view.app_view import AppView

RU = 'ru'


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    model = AppModel()
    view = AppView(main_window, model.load_locale(model.locale))
    AppController(model, view)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
