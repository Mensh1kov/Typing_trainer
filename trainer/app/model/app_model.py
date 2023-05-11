import datetime
import threading
import time
from typing import Callable

from trainer.app.model.utils.data_handler import load_user_by_name, save_user
from trainer.app.model.utils.resource_handler import Level, Locale, load_sentence_by_lvl, load_locale, Mode


class AppModel:
    def __init__(self):
        self.is_complete = False
        self.is_started = False

        self.mistakes = 0
        self.time_delta = 0
        self.speed = 0
        self.user = None
        self.timer = None
        self.start_time = datetime.datetime.now()

        self.lvl = Level.SIMPLE
        self.mode = Mode.NORMAL
        self.locale = Locale.RU

        self.total_session_len_input = 0
        self.total_session_time_typing = .0
        self.total_session_mistakes = 0
        self.target_text = self.get_example_text()
        self.timer_action = None
        self.time_up_action = None

    def calculate_speed(self, len_input: int,
                        time_delta: float) -> int:
        return int(len_input / (time_delta / 60)) if time_delta else 0

    def process_input(self, input_text: str) -> bool:
        if self.mode == Mode.NORMAL:
            return self._process_normal_input(input_text)

    def start(self):
        if self.mode == Mode.NORMAL:
            self.start_time = datetime.datetime.now()
        else:
            self.start_timer(5)
            self.is_started = True

    def start_timer(self, seconds: int):
        self.timer = threading.Timer(1.0, lambda: self.start_timer(seconds - 1))
        self.timer.daemon = True
        self.timer.start()
        self.timer_action(seconds)

        if seconds <= 0:
            self.timer.cancel()
            self.is_started = False
            self.time_up_action()

    def stop_timer(self):
        self.is_started = False
        if self.timer:
            self.timer.cancel()

    def get_example_text(self):
        self.target_text = load_sentence_by_lvl(self.lvl, self.locale)
        return self.target_text

    def load_locale(self, locale: Locale):
        self.locale = locale
        return load_locale(locale)

    def set_level(self, lvl: Level):
        self.lvl = lvl

    def set_mode(self, mode: Mode):
        self.stop_timer()
        self.mode = mode

    def set_timer_action(self, action: Callable[[int], None]):
        self.timer_action = action

    def set_time_up_action(self, action: Callable[[], None]):
        self.time_up_action = action

    def change_user(self, name: str):
        self.stop_timer()
        self.save_user()
        if name:
            self.user = load_user_by_name(name)
            self.reset_session()

    def is_complete(self):
        return self.is_complete

    def is_authorization(self):
        return self.user

    def is_started(self):
        return self.is_started

    def get_user(self) -> dict:
        return self.user

    def get_speed(self):
        return self.speed

    def get_mistakes(self):
        return self.mistakes

    def save_user(self):
        if self.user:
            save_user(self.user)

    def reset_session(self):
        self.total_session_len_input = 0
        self.total_session_time_typing = .0
        self.mistakes = 0
        self.speed = 0

    def update_user_stat(self):
        if self.user:
            self.user['speed'] = self.calculate_speed(
                self.total_session_len_input, self.total_session_time_typing)
            self.user['mistakes'] = self.total_session_mistakes

    def _process_normal_input(self, input_text: str) -> bool:
        len_input = len(input_text)
        delta_time = (datetime.datetime.now() -
                      self.start_time).total_seconds()
        self._update_speed(len_input, delta_time)

        if input_text == self.target_text:
            self.is_complete = True
            self.is_started = False
            self.total_session_len_input += len_input
            self.total_session_time_typing += delta_time
            self.total_session_mistakes += self.mistakes
            self.user['texts'] += 1
            self.mistakes = 0
            self.update_user_stat()
            return True

        if input_text != self.target_text[:len_input]:
            self.mistakes += 1
            self.is_complete = False
            return False
        self.is_complete = False
        return True

    def _update_speed(self, len_input: int, delta_time: float):
        self.speed = self.calculate_speed(len_input, delta_time)
