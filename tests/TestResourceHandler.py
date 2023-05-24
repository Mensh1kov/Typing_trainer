import os
import unittest

from trainer.app.model.utils.resource_handler import *
from . import resource_folder


class TestResourceHandler(unittest.TestCase):
    def test_load_sentence_by_lvl(self):
        data = load_sentence_by_lvl(os.path.join(resource_folder,
                                                 'texts'),
                                    Level.SIMPLE, Locale.RU)
        self.assertTrue(data)

    def test_load_big_text(self):
        data = load_big_text(os.path.join(resource_folder, 'texts'),
            Locale.RU)
        self.assertTrue(data)

    def test_load_locale(self):
        locale = load_locale(os.path.join(resource_folder, 'locale'),
                             Locale.RU)
        self.assertTrue(locale)
