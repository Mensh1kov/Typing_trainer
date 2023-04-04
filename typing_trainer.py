from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import sentence


class TypingTrainerWindow(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setWindowTitle("Typing Trainer")
        self.lcd_value = 0
        self.mistakes = 0
        self.finish = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_lcd)
        self.build_user_interface()
        self.show()

    def build_user_interface(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(1200, 800)
        self.setMinimumSize(QtCore.QSize(1200, 800))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(self)
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
        self.label_m.setText("Ошибки:")

        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_speed.setGeometry(QtCore.QRect(220, 30, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_speed.setWordWrap(True)
        self.label_speed.setObjectName("label_speed")
        self.label_speed.setText("Скорость:")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 150, 1000, 450))
        self.widget.setObjectName("widget")
        self.widget.setEnabled(False)

        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("border: 1px solid black;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.on_text_changed)

        self.label_sent = QtWidgets.QLabel(self.widget)
        self.label_sent.setGeometry(QtCore.QRect(0, 250, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_sent.setFont(font)
        self.label_sent.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_sent.setWordWrap(True)
        self.label_sent.setObjectName("label_sent")
        self.label_sent.setText("Нажмите на Start")

        self.lcdNumber_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_time.setGeometry(QtCore.QRect(920, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lcdNumber_time.setFont(font)
        self.lcdNumber_time.setStyleSheet("border: none;")
        self.lcdNumber_time.setProperty("intValue", self.lcd_value)
        self.lcdNumber_time.setObjectName("lcdNumber_time")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(500, 660, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("border: 1px solid black;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setText("Start")
        self.pushButton_start.clicked.connect(self.start_button_clicked)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setCentralWidget(self.centralwidget)  # хз для чего

    def start_button_clicked(self):
        self.label_sent.setText(sentence.get_sentence())
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
        self.speed = int(len(self.target_text) / (self.lcd_value / 60))
        print(self.speed)
        self.set_mistakes_speed_label()
        self.widget.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TypingTrainerWindow()
    sys.exit(app.exec_())
