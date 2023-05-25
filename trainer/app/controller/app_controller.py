import random
import sys
from functools import partial

from PyQt5.QtCore import QEvent, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QAction
from trainer.app.model.app_model import AppModel
from trainer.app.view.app_view import AppView
from trainer.app.model.utils.resource_handler import Locale, Level, Mode


class AppController:
    def __init__(self, model: AppModel, view: AppView):
        self.model = model
        self.view = view
        self.player = QMediaPlayer()

        self.setup_view()
        self.setup_model()
        self.update_info_view()
        self.authorization()

    def close_event(self, event: QEvent):
        self.model.save_user()
        event.accept()

    def setup_model(self):
        self.model.set_timer_action(self.update_time_view)
        self.model.set_time_up_action(self.time_up)

    def setup_view(self):
        self.setup_window()
        self.setup_input_example_widget()
        self.setup_menubar()
        self.setup_info_view()

    def setup_info_view(self):
        if self.model.mode == Mode.NORMAL:
            self.view.info_widget.time.setVisible(False)
        else:
            self.view.info_widget.time.setVisible(True)

    def setup_window(self):
        self.view.main_window.closeEvent = self.close_event

    def setup_input_example_widget(self):
        self.view.input_example_widget.example.setText(
            self.model.get_example_text('trainer/resources/texts'))
        self.view.input_example_widget.input.textChanged.connect(
            lambda: self.on_text_changed())

    def setup_menubar(self):
        self.setup_difficulty_menu()
        self.setup_language_menu()
        self.setup_user_menu()
        self.setup_mode_menu()

    def setup_user_menu(self):
        user = self.view.menubar.user
        user.change_user.triggered.connect(self.change_user_dialog)
        user.statistics.triggered.connect(self.show_stat)

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

    def setup_mode_menu(self):
        mode = self.view.menubar.mode

        self.mode_map = {
            Mode.NORMAL: mode.normal,
            Mode.TIME: mode.time
        }

        for mode_, action in self.mode_map.items():
            action.triggered.connect(partial(self.on_mode_changed, mode_))

        self.selected_mode_action = self.mode_map.get(
            self.model.mode)
        self.set_action_checked(self.selected_mode_action, True)

    def on_locale_changed(self, locale: Locale):
        new = self.language_map.get(locale)
        old = self.selected_language_action
        self.selected_language_action = new
        self.set_locale(locale)
        self.switch_action(old, new)
        self.complete()

    def on_level_changed(self, lvl: Level):
        new = self.difficulty_map.get(lvl)
        old = self.selected_difficulty_action
        self.selected_difficulty_action = new
        self.set_level(lvl)
        self.switch_action(old, new)
        self.complete()

    def on_mode_changed(self, mode: Mode):
        self.player.stop()
        new = self.mode_map.get(mode)
        old = self.selected_mode_action
        self.selected_mode_action = new
        self.set_mode(mode)
        self.switch_action(old, new)
        self.complete()
        self.setup_info_view()

    def switch_action(self, old: QAction, new: QAction):
        self.set_action_checked(old, False)
        self.set_action_checked(new, True)

    def set_action_checked(self, action: QAction, checked: bool):
        action.setChecked(checked)

    def set_locale(self, locale: Locale):
        self.view.set_locale(self.model.load_locale(locale))

    def set_level(self, lvl: Level):
        self.model.set_level(lvl)

    def set_mode(self, mode: Mode):
        self.model.set_mode(mode)

    def on_text_changed(self):
        if not self.model.is_started:
            if self.model.mode == Mode.TIME:
                self.music_player()
            self.model.start()
            self.update_info_view()
        input_ = self.view.input_example_widget.input
        if self.is_correct_input(input_.text()):
            input_.setStyleSheet("background-color: white;")
        else:
            input_.setStyleSheet("background-color: red;")

        if self.model.is_complete:
            self.complete()
        else:
            self.update_info_view()

    def update_info_view(self):
        self.update_mistakes()
        self.update_speed()

    def update_time_view(self, seconds: int):
        self.view.info_widget.set_time(seconds)

    def time_up(self):
        self.player.stop()
        speed = self.model.get_speed()
        mistakes = self.model.get_mistakes()
        self.view.time_up_dialog.show_result(speed, mistakes)
        self.complete()

    def authorization(self):
        while not self.model.is_authorization():
            name, ok = self.get_user_input_dialog()
            if ok:
                self.change_user(name)
            else:
                sys.exit()

    def change_user_dialog(self):
        name, ok = self.get_user_input_dialog()
        if ok:
            self.change_user(name)
            self.update_info_view()

    def change_user(self, name: str):
        self.model.change_user(name)

    def get_user_input_dialog(self) -> (str, bool):
        return self.view.user_dialog.get_text()

    def show_stat(self):
        user = self.model.get_user()
        if user:
            self.view.stat_dialog.show_stat(user)

    def is_correct_input(self, input_text: str) -> bool:
        return self.model.process_input(input_text)

    def complete(self):
        self.set_new_example()
        self.clear_input()

    def set_new_example(self):
        self.view.input_example_widget.example.setText(
            self.model.get_example_text('trainer/resources/texts'))

    def clear_input(self):
        input = self.view.input_example_widget.input
        input.blockSignals(True)
        input.clear()
        input.blockSignals(False)

    def update_speed(self):
        self.view.info_widget.set_speed(self.model.get_speed())

    def update_mistakes(self):
        self.view.info_widget.set_mistakes(self.model.get_mistakes())

    def music_player(self):
        playlist = QMediaPlaylist(self.player)
        music = random.choice(["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3"])
        media = QMediaContent(
            QUrl.fromLocalFile(f'trainer/resources/music/{music}'))
        playlist.addMedia(media)
        playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(playlist)
        self.player.play()
