from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.main_widget.setObjectName("main_widget")
        self.input_and_example_widget = QtWidgets.QWidget(self.main_widget)
        self.input_and_example_widget.setGeometry(QtCore.QRect(50, 100, 700, 150))
        self.input_and_example_widget.setObjectName("input_and_example_widget")
        self.input = QtWidgets.QLineEdit(self.input_and_example_widget)
        self.input.setGeometry(QtCore.QRect(0, 0, 700, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.example = QtWidgets.QLabel(self.input_and_example_widget)
        self.example.setGeometry(QtCore.QRect(3, 35, 694, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.example.setFont(font)
        self.example.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.example.setObjectName("example")
        self.info_widget = QtWidgets.QWidget(self.main_widget)
        self.info_widget.setGeometry(QtCore.QRect(50, 30, 700, 51))
        self.info_widget.setObjectName("info_widget")
        self.mistakes = QtWidgets.QLabel(self.info_widget)
        self.mistakes.setGeometry(QtCore.QRect(0, 0, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mistakes.setFont(font)
        self.mistakes.setObjectName("mistakes")
        self.speed = QtWidgets.QLabel(self.info_widget)
        self.speed.setGeometry(QtCore.QRect(200, 0, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speed.setFont(font)
        self.speed.setObjectName("speed")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.user = QtWidgets.QMenu(self.menubar)
        self.user.setObjectName("user")
        self.language = QtWidgets.QMenu(self.menubar)
        self.language.setObjectName("language")
        self.difficulty = QtWidgets.QMenu(self.menubar)
        self.difficulty.setObjectName("difficulty")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.change_user = QtWidgets.QAction(MainWindow)
        self.change_user.setObjectName("change_user")
        self.statistics = QtWidgets.QAction(MainWindow)
        self.statistics.setObjectName("statistics")
        self.Russian = QtWidgets.QAction(MainWindow)
        self.Russian.setObjectName("Russian")
        self.English = QtWidgets.QAction(MainWindow)
        self.English.setObjectName("English")
        self.simple = QtWidgets.QAction(MainWindow)
        self.simple.setObjectName("simple")
        self.medium = QtWidgets.QAction(MainWindow)
        self.medium.setObjectName("medium")
        self.hard = QtWidgets.QAction(MainWindow)
        self.hard.setObjectName("hard")
        self.legendary = QtWidgets.QAction(MainWindow)
        self.legendary.setObjectName("legendary")
        self.user.addAction(self.change_user)
        self.user.addAction(self.statistics)
        self.language.addAction(self.Russian)
        self.language.addAction(self.English)
        self.difficulty.addAction(self.simple)
        self.difficulty.addAction(self.medium)
        self.difficulty.addAction(self.hard)
        self.difficulty.addAction(self.legendary)
        self.menubar.addAction(self.user.menuAction())
        self.menubar.addAction(self.language.menuAction())
        self.menubar.addAction(self.difficulty.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.example.setText(_translate("MainWindow", "Мама мыла раму"))
        self.mistakes.setText(_translate("MainWindow", "Ошибки:"))
        self.speed.setText(_translate("MainWindow", "Скорость:"))
        self.user.setTitle(_translate("MainWindow", "Пользователь"))
        self.language.setTitle(_translate("MainWindow", "Язык"))
        self.difficulty.setTitle(_translate("MainWindow", "Сложность"))
        self.change_user.setText(_translate("MainWindow", "Сменить пользователя"))
        self.statistics.setText(_translate("MainWindow", "Статистика"))
        self.Russian.setText(_translate("MainWindow", "Русский"))
        self.English.setText(_translate("MainWindow", "Английский"))
        self.simple.setText(_translate("MainWindow", "Просто"))
        self.medium.setText(_translate("MainWindow", "Средне"))
        self.hard.setText(_translate("MainWindow", "Сложно"))
        self.legendary.setText(_translate("MainWindow", "Легендарно"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
