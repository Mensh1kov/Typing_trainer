from resource_handler import Level, Locale, load_sentence_by_lvl, load_locale


class AppModel:
    def __init__(self):
        self.mistakes = 0
        self.lvl = Level.SIMPLE
        self.is_complete = False
        self.locale = Locale.RU
        self.target_text = self.get_example_text()

    def calculate_speed(self, input_text: str, time: int) -> int:
        return int(len(input_text) / (time / 60)) if time else 0

    def process_input(self, input_text: str) -> bool:
        if input_text == self.target_text:
            self.is_complete = True
            return True

        if input_text != self.target_text[:len(input_text)]:
            self.mistakes += 1
            self.is_complete = False
            return False
        self.is_complete = False
        return True

    def get_example_text(self):
        self.target_text = load_sentence_by_lvl(self.lvl, self.locale)
        return self.target_text

    def get_locale(self, locale: Locale):
        self.set_locale(locale)
        return load_locale(locale)

    def set_locale(self, locale: Locale):
        self.locale = locale

    def set_level(self, lvl: Level):
        self.lvl = lvl
