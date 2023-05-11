from PyQt5.QtWidgets import QInputDialog, QWidget


class UserDialog(QInputDialog):
    def __init__(self, widget: QWidget, locale: dict):
        super().__init__(widget)
        self.widget = widget
        self.set_locale(locale)

    def set_locale(self, locale: dict):
        self.title = locale.get('title')
        self.description = locale.get('description')

    def get_text(self) -> (str, bool):
        return self.getText(self.widget, self.title, self.description)
