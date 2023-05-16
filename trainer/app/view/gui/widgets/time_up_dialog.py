from PyQt5.QtWidgets import QWidget, QMessageBox


class TimeUpDialog(QMessageBox):
    def __init__(self, widget: QWidget, locale: dict):
        super().__init__(widget)
        self.locale = locale

    def set_locale(self, locale: dict):
        self.locale = locale

    def show_result(self, speed: int, mistakes: int):
        self.setWindowTitle(
            f'{self.locale.get("title")}')
        self.setText(
            f'{self.locale.get("speed")}: {speed}\n'
            f'{self.locale.get("mistakes")}: {mistakes}'
        )
        self.show()
