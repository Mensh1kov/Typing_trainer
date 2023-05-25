import datetime
import re
from typing import Callable
from PyQt5.QtCore import QTimer
from trainer.app.model.utils.data_handler import load_user_by_name, save_user
from trainer.app.model.utils.resource_handler import Level, Locale, \
    load_sentence_by_lvl, load_locale, Mode, load_big_text


class AppModel:
    def __init__(self):
        self.time = 0
        self.lines = []
        self.total_len_input = 0
        self.is_complete = False
        self.is_started = False

        self.mistakes = 0
        self.time_delta = 0
        self.speed = 0
        self.user = None
        self.timer = None
        self.texts_path = 'trainer/resources/texts'
        self.locale_path = 'trainer/resources/locale'
        self.start_time = datetime.datetime.now()

        self.total_session_len_input = 0
        self.total_session_time_typing = .0
        self.total_session_mistakes = 0

        self.lvl = Level.SIMPLE
        self.mode = Mode.NORMAL
        self.locale = Locale.RU

    def set_up_parameters(self):
        self.target_text = self.get_example_text(self.texts_path)
        self.timer_action = None
        self.time_up_action = None

    def calculate_speed(self, len_input: int,
                        time_delta: float) -> int:
        return int(len_input / (time_delta / 60)) if time_delta else 0

    def process_input(self, input_text: str) -> bool:
        if self.mode == Mode.NORMAL:
            return self._process_normal_input(input_text)
        elif self.mode == Mode.TIME:
            return self._process_time_input(input_text)

    def start(self):
        self.speed = 0
        self.mistakes = 0
        self.start_time = datetime.datetime.now()
        if self.mode == Mode.NORMAL:
            pass
        else:
            self.total_len_input = 0
            self.start_timer(60)
        self.is_started = True

    def update_time(self):
        self.time -= 1
        self.timer_action(self.time)
        if self.time <= 0:
            self.stop_timer()
            self.time_up_action()

    def start_timer(self, seconds: int):
        self.time = seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def stop_timer(self):
        self.is_started = False
        if self.timer:
            self.timer.stop()

    def get_example_text(self, path: str):
        if self.mode == Mode.NORMAL:
            self.target_text = load_sentence_by_lvl(path,
                                                    self.lvl, self.locale)
        else:
            if not self.is_started:
                self.target_text = load_big_text(path, self.locale)
                self.lines = re.split(
                    r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
                    self.target_text)

        return self.target_text

    def load_locale(self, locale: Locale):
        self.locale = locale
        return load_locale(self.locale_path, locale)

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

    def is_complete(self) -> bool:
        return self.is_complete

    def is_authorization(self) -> bool:
        return self.user

    def is_started(self) -> bool:
        return self.is_started

    def get_user(self) -> dict:
        return self.user

    def get_speed(self) -> int:
        return self.speed

    def get_mistakes(self) -> int:
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
            self.update_user_stat()
            return True

        if input_text != self.target_text[:len_input]:
            self.mistakes += 1
            self.is_complete = False
            return False
        self.is_complete = False
        return True

    def _process_time_input(self, input_text: str) -> bool:
        len_input = len(input_text)
        delta_time = (datetime.datetime.now() -
                      self.start_time).total_seconds()
        self._update_speed(self.total_len_input + len_input, delta_time)

        if input_text == self.lines[0]:
            self.total_len_input += len_input
            self.is_complete = True
            self.total_session_len_input += len_input
            self.total_session_time_typing += delta_time
            self.total_session_mistakes += self.mistakes
            self.update_user_stat()
            line = self.lines.pop(0)
            if len(self.lines) == 0:
                self.target_text = load_big_text(self.locale)
                self.lines = re.split(
                    r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
                    self.target_text)
            else:
                self.target_text = self.target_text[(len(line) + 1):]

            return True

        if input_text != self.target_text[:len_input]:
            self.mistakes += 1
            self.is_complete = False
            return False

        self.is_complete = False
        return True

    def _update_speed(self, len_input: int, delta_time: float):
        self.speed = self.calculate_speed(len_input, delta_time)
