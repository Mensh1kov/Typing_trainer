from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


def get_sentence():
    sentences = [
        "Возможно ли найти компромисс между своими интересами и интересами других людей?",
        "Лето - самое прекрасное время года для путешествий и отдыха на природе.",
        "Стоит ли начинать новый бизнес в условиях экономического кризиса?",
        "Сегодняшние молодые поколения интересуются технологиями и социальными сетями.",
        "Когда я был ребенком, я любил играть в футбол с друзьями на улице.",
        "Любовь и доверие - важные составляющие крепких отношений между людьми.",
        "Один из лучших способов расслабиться - прогулка на свежем воздухе.",
        "Успех в жизни зависит не только от удачи, но и от упорного труда и настойчивости.",
        "Лучший способ изучить новый язык - погрузиться в языковую среду и общаться с носителями языка.",
        "Музыка - это универсальный язык, который может объединить людей из разных культур и стран."]
    random_sentence = random.choice(sentences)
    return random_sentence


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_m = QtWidgets.QLabel(self.centralwidget)
        self.label_m.setGeometry(QtCore.QRect(30, 30, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_m.setFont(font)
        self.label_m.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_m.setWordWrap(True)
        self.label_m.setObjectName("label_m")
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_speed.setGeometry(QtCore.QRect(220, 30, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_speed.setWordWrap(True)
        self.label_speed.setObjectName("label_speed")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 150, 1000, 450))
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("border: 1px solid black;")
        self.textEdit.setObjectName("textEdit")
        self.label_sent = QtWidgets.QLabel(self.widget)
        self.label_sent.setGeometry(QtCore.QRect(0, 250, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_sent.setFont(font)
        self.label_sent.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_sent.setWordWrap(True)
        self.label_sent.setObjectName("label_sent")
        self.lcdNumber_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_time.setGeometry(QtCore.QRect(920, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lcdNumber_time.setFont(font)
        self.lcdNumber_time.setStyleSheet("border: none;")
        self.lcd_value = 0
        self.lcdNumber_time.setProperty("intValue", self.lcd_value)
        self.lcdNumber_time.setObjectName("lcdNumber_time")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(500, 660, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("border: 1px solid black;")
        self.pushButton_start.setObjectName("pushButton_start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textEdit.textChanged.connect(self.on_text_changed)
        self.pushButton_start.clicked.connect(self.start_button_clicked)
        self.mistakes = 0
        self.finish = False
        self.widget.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_lcd)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_m.setText(_translate("MainWindow", "Ошибки:"))
        self.label_speed.setText(_translate("MainWindow", "Скорость:"))
        self.label_sent.setText(_translate("MainWindow", "Нажмите на Start"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))

    def start_button_clicked(self):
        self.label_sent.setText(get_sentence())
        self.textEdit.setText("")
        self.lcd_value = 0
        self.timer.start(1000)
        self.widget.setEnabled(True)
        self.pushButton_start.setText("Reset")
        self.mistakes = 0
        self.speed = 0
        self.set_mistakes_speed_label()

    def update_lcd(self):
        self.lcd_value += 1
        self.lcdNumber_time.display(self.lcd_value)

    def set_mistakes_speed_label(self):
        self.label_m.setText(f"Ошибки: {self.mistakes}")
        self.label_speed.setText(f"Скорость: {self.speed}")

    def on_text_changed(self):
        # Получаем текущий текст из TextEdit
        text = self.textEdit.toPlainText()
        # Текст, с которым сравниваем ввод пользователя
        self.target_text = self.label_sent.text()

        cursor = self.textEdit.textCursor()
        current_position = cursor.position()
        if text != self.target_text[:current_position]:
            self.textEdit.setStyleSheet("background-color: red;")
            self.mistakes += 1
        else:
            self.textEdit.setStyleSheet("background-color: white;")

        if text == self.target_text:
            self.complete()

    def complete(self):
        self.timer.stop()
        self.pushButton_start.setText("Start")
        self.label_sent.setText("Congratulations")
        self.speed = len(self.target_text) / (self.lcd_value / 60)
        self.set_mistakes_speed_label()
        self.widget.setEnabled(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
