from PyQt5.QtWidgets import QWidget, QMessageBox


class StatDialog(QMessageBox):
    def __init__(self, widget: QWidget, locale: dict):
        super().__init__(widget)
        self.locale = locale
        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.locale = locale

    def show_stat(self, user: dict):
        self.setWindowTitle(
            f'{self.locale.get("stat")}: {user.get("name")}')
        self.setText(
            f"\n"
            f"{self.locale.get('number_typed_texts')}: {user.get('texts')}\n"
            f"{self.locale.get('speed')}: {user.get('speed')}\n"
            f"{self.locale.get('number_mistakes')}: {user.get('mistakes')}\n"
        )
        self.show()
