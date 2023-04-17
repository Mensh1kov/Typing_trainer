from PyQt5 import QtWidgets
from gui.my_app import MyApp


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    MyApp(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
