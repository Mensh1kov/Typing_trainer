from resource_loaders import Level, load_sentence_by_lvl, load_locale


class AppModel:
    def __init__(self):
        self.mistakes = 0
        self.lvl = Level.SIMPLE
        self.target_text = self.get_example_text()
        self.is_complete = False

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
        self.target_text = load_sentence_by_lvl(self.lvl)
        return self.target_text

    def get_locale(self, locale: str):
        return load_locale(locale)

    def set_level(self, lvl: Level):
        self.lvl = lvl

