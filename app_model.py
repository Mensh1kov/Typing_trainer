from sentence import get_sentence_by_lvl, Levels


class AppModel:
    def __init__(self):
        self.mistakes = 0
        self.target_text = "A"
        self.is_complete = False
        self.lvl = Levels.SIMPLE

    def calculate_speed(self, input_text: str, time: int) -> int:
        return int(len(input_text) / (time / 600)) if time else 0

    def process_input(self, input_text: str) -> bool:
        if input_text == self.target_text:
            self.is_complete = True
            return True
        t = self.target_text[:len(input_text)]
        if input_text != self.target_text[:len(input_text)]:
            self.mistakes += 1
            self.is_complete = False
            return False
        self.is_complete = False
        return True

    def get_example_text(self):
        self.target_text = get_sentence_by_lvl(self.lvl)
        return self.target_text

