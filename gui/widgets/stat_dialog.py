from PyQt5.QtWidgets import QWidget, QMessageBox


class StatDialog:
    def __init__(self, widget: QWidget, locale: dict):
        self.dialog = QMessageBox(widget)
        self.locale = locale
        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.locale = locale

    def show_stat(self, stat: dict):
        self.dialog.setWindowTitle(
            f'{self.locale.get("stat")}: {stat.get("user")}')
        self.dialog.setText(
            f"\n"
            f"{self.locale.get('number_typed_texts')}: {stat.get('texts')}\n"
            f"{self.locale.get('speed')}: {stat.get('speed')}\n"
            f"{self.locale.get('number_mistakes')}: {stat.get('mistakes')}\n"
        )
        self.dialog.show()
