from PyQt5.QtCore import QTimer

from app_model import AppModel
from gui.app_view import AppView


class AppController:
    def __init__(self, model: AppModel, view: AppView):
        self.model = model
        self.view = view
        self.view.input_example_widget.input.textChanged.connect(
            lambda: self.on_text_changed())
        self.view.input_example_widget.example.setText(model.get_example_text())
        self.time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_speed)

    def on_text_changed(self):
        if not self.timer.isActive():
            self.timer.start()
        input_ = self.view.input_example_widget.input
        if self.model.process_input(input_.text()):
            input_.setStyleSheet("background-color: white;")
        else:
            input_.setStyleSheet("background-color: red;")

        if self.model.is_complete:
            self.view.input_example_widget.example.setText(self.model.get_example_text())
            input_.setText("")
            self.timer.stop()

    def update_speed(self):
        text = self.view.input_example_widget.input.text()
        speed = self.model.calculate_speed(text, self.time)
        self.view.info_widget.set_speed(speed)
