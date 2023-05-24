import unittest

from trainer.app.model.utils.resource_handler import *


class TestResourceHandler(unittest.TestCase):
    def test_load_sentence_by_lvl(self):
        data = load_sentence_by_lvl('C:/Users/rasba/Documents/Programming'
                                    '/Python/keyboard '
                                    'simulator/trainer/resources/texts',
                                    Level.SIMPLE, Locale.RU)
        self.assertTrue(data)

    def test_load_big_text(self):
        data = load_big_text(
            'C:/Users/rasba/Documents/Programming/Python/keyboard '
            'simulator/trainer/resources/texts',
            Locale.RU)
        self.assertTrue(data)

    def test_load_locale(self):
        locale = load_locale('C:/Users/rasba/Documents/Programming/Python'
                             '/keyboard simulator/trainer/resources/locale',
                             Locale.RU)
        self.assertTrue(locale)
