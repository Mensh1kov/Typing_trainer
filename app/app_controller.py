from functools import partial

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QAction

from app.app_model import AppModel
from app.app_view import AppView
from resource_loaders import Level, Locale


class AppController:
    def __init__(self, model: AppModel, view: AppView):
        self.model = model
        self.view = view

        self.setup_timer()
        self.setup_input_example_widget()
        self.setup_menubar()

        self.selected_language_action = self.view.menubar.language.Russian

    def setup_timer(self):
        self.time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_speed)

    def setup_input_example_widget(self):
        self.view.input_example_widget.example.setText(
            self.model.get_example_text())
        self.view.input_example_widget.input.textChanged.connect(
            lambda: self.on_text_changed())

    def setup_menubar(self):
        self.setup_difficulty_menu()
        self.setup_language_menu()

    def setup_language_menu(self):
        language = self.view.menubar.language

        self.language_map = {
            Locale.RU: language.Russian,
            Locale.EN: language.English
        }

        for locale, action in self.language_map.items():
            action.triggered.connect(partial(self.on_locale_changed, locale))

        self.selected_language_action = self.language_map.get(
            self.model.locale
        )
        self.set_action_checked(self.selected_language_action, True)


    def setup_difficulty_menu(self):
        difficulty = self.view.menubar.difficulty

        self.difficulty_map = {
            Level.SIMPLE: difficulty.simple,
            Level.MEDIUM: difficulty.medium,
            Level.HARD: difficulty.hard,
            Level.LEGENDARY: difficulty.legendary
        }

        for lvl, action in self.difficulty_map.items():
            action.triggered.connect(partial(self.on_level_changed, lvl))

        self.selected_difficulty_action = self.difficulty_map.get(
            self.model.lvl)
        self.set_action_checked(self.selected_difficulty_action, True)

    def on_locale_changed(self, locale: Locale):
        new = self.language_map.get(locale)
        old = self.selected_language_action
        self.selected_language_action = new
        self.set_locale(locale)
        self.switch_action(old, new)


    def on_level_changed(self, lvl: Level):
        new = self.difficulty_map.get(lvl)
        old = self.selected_difficulty_action
        self.selected_difficulty_action = new
        self.set_level(lvl)
        self.switch_action(old, new)
        self.complete()

    def switch_action(self, old: QAction, new: QAction):
        self.set_action_checked(old, False)
        self.set_action_checked(new, True)

    def set_action_checked(self, action: QAction, checked: bool):
        action.setChecked(checked)

    def set_locale(self, locale: Locale):
        self.view.set_locale(self.model.get_locale(locale))

    def set_level(self, lvl: Level):
        self.model.set_level(lvl)

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
