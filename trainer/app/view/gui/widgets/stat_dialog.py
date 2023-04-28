from PyQt5.QtWidgets import QWidget, QMessageBox


class StatDialog:
    def __init__(self, widget: QWidget, locale: dict):
        self.dialog = QMessageBox(widget)
        self.locale = locale
        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.locale = locale

    def show_stat(self, user: dict):
        self.dialog.setWindowTitle(
            f'{self.locale.get("stat")}: {user.get("name")}')
        self.dialog.setText(
            f"\n"
            f"{self.locale.get('number_typed_texts')}: {user.get('texts')}\n"
            f"{self.locale.get('speed')}: {user.get('speed')}\n"
            f"{self.locale.get('number_mistakes')}: {user.get('mistakes')}\n"
        )
        self.dialog.show()
