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
            self.timer.start(1000)

        input_ = self.view.input_example_widget.input
        if self.is_correct_input(input_.text()):
            input_.setStyleSheet("background-color: white;")
        else:
            input_.setStyleSheet("background-color: red;")
            self.view.info_widget.set_mistakes(self.model.mistakes)

        if self.model.is_complete:
            self.complete()

    def is_correct_input(self, input_text: str) -> bool:
        return self.model.process_input(input_text)

    def complete(self):
        self.view.input_example_widget.example.setText(self.model.get_example_text())
        self.clear_input()
        self.reset_time()
        self.stop_timer()

    def clear_input(self):
        self.view.input_example_widget.input.setText("")

    def reset_time(self):
        self.time = 0

    def stop_timer(self):
        self.timer.stop()

    def update_speed(self):
        self.time += 1
        text = self.view.input_example_widget.input.text()
        speed = self.model.calculate_speed(text, self.time)
        self.view.info_widget.set_speed(speed)
