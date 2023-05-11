import datetime

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
        self.start_time = datetime.datetime.now()

        self.lvl = Level.SIMPLE
        self.mode = Mode.NORMAL
        self.locale = Locale.RU

        self.target_text = self.get_example_text()

    def calculate_speed(self, len_input: int,
                        time_delta: datetime.timedelta) -> int:
        time = time_delta.total_seconds()
        return int(len_input / (time / 60)) if time else 0

    def process_input(self, input_text: str) -> bool:
        if self.mode == Mode.NORMAL:
            return self._process_normal_input(input_text)

    def start(self):
        self.start_time = datetime.datetime.now()
        self.is_started = True

    def get_example_text(self):
        self.target_text = load_sentence_by_lvl(self.lvl, self.locale)
        return self.target_text

    def load_locale(self, locale: Locale):
        self.locale = locale
        return load_locale(locale)

    def set_level(self, lvl: Level):
        self.lvl = lvl

    def set_mode(self, mode: Mode):
        self.mode = mode

    def change_user(self, name: str):
        self.save_user()
        if name:
            self.user = load_user_by_name(name)

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

    def save_user(self):
        if self.user:
            save_user(self.user)

    def _process_normal_input(self, input_text: str) -> bool:
        len_input = len(input_text)
        self._update_speed(len_input)

        if input_text == self.target_text:
            self.is_complete = True
            self.is_started = False
            return True

        if input_text != self.target_text[:len_input]:
            self.mistakes += 1
            self.is_complete = False
            return False
        self.is_complete = False
        return True

    def _update_speed(self, len_input: int):
        self.speed = self.calculate_speed(
            len_input, datetime.datetime.now() - self.start_time)
