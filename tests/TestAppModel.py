import os
import unittest
from trainer.app.model.app_model import AppModel
from trainer.app.model.utils.resource_handler import Locale, Level, Mode
from . import resource_folder


class TestAppModel(unittest.TestCase):
    def setUp(self):
        self.model = AppModel()

    def test_calculate_speed_with_valid_time_delta(self):
        len_input = 100
        time_delta = 30.0
        expected_speed = int(len_input / (time_delta / 60))
        result = self.model.calculate_speed(len_input, time_delta)
        self.assertEqual(result, expected_speed)

    def test_calculate_speed_with_zero_time_delta(self):
        len_input = 100
        time_delta = 0.0
        result = self.model.calculate_speed(len_input, time_delta)
        self.assertEqual(result, 0)

    def test_process_input_normal_mode(self):
        self.model.mode = Mode.NORMAL
        self.model.target_text = "example input test"
        input_text = "example input"
        result = self.model.process_input(input_text)
        self.assertTrue(result)

    def test_process_input_time_mode(self):
        self.model.mode = Mode.TIME
        self.model.lines = " test example input test"
        self.model.target_text = "example input test"
        input_text = "example input"
        result = self.model.process_input(input_text)
        self.assertTrue(result)

    def test_process_input_invalid_mode(self):
        self.model.mode = "invalid_mode"
        input_text = "example input"
        result = self.model.process_input(input_text)
        self.assertFalse(result)

    def test_start_normal_mode(self):
        self.model.mode = Mode.NORMAL
        self.model.start()
        self.assertEqual(self.model.speed, 0)
        self.assertEqual(self.model.mistakes, 0)
        self.assertIsNotNone(self.model.start_time)
        self.assertTrue(self.model.is_started)

    def test_start_time_mode(self):
        self.model.mode = Mode.TIME
        self.model.start()
        self.assertEqual(self.model.speed, 0)
        self.assertEqual(self.model.mistakes, 0)
        self.assertEqual(self.model.total_len_input, 0)
        self.assertTrue(self.model.is_started)

    def test_get_example_text_normal_mode(self):
        self.model.mode = Mode.NORMAL
        self.model.lvl = Level.MEDIUM
        self.model.locale = Locale.EN
        result = self.model.get_example_text(os.path.join(resource_folder,
                                                          'texts'))
        self.assertTrue(result)

    def test_get_example_text_time_mode(self):
        self.model.mode = Mode.TIME
        self.model.locale = Locale.EN
        result = self.model.get_example_text(os.path.join(resource_folder,
                                                          'texts'))
        self.assertTrue(result)

    def test_set_level(self):
        lvl = Level.HARD
        self.model.set_level(lvl)
        self.assertEqual(self.model.lvl, lvl)

    def test_set_mode(self):
        mode = Mode.NORMAL
        self.model.set_mode(mode)
        self.assertEqual(self.model.mode, mode)
        self.assertFalse(self.model.is_started)

    def test_get_speed(self):
        self.assertEqual(self.model.get_speed(), 0)

        speed = 100
        self.model.speed = speed
        self.assertEqual(self.model.get_speed(), speed)

    def test_get_mistakes(self):
        self.assertEqual(self.model.get_mistakes(), 0)

        mistakes = 13
        self.model.mistakes = mistakes
        self.assertEqual(self.model.get_mistakes(), mistakes)

    def test_reset_session(self):
        self.model.total_session_len_input = 100
        self.model.total_session_time_typing = 10.0
        self.model.mistakes = 5
        self.model.speed = 50
        self.model.reset_session()
        self.assertEqual(self.model.total_session_len_input, 0)
        self.assertEqual(self.model.total_session_time_typing, .0)
        self.assertEqual(self.model.mistakes, 0)
        self.assertEqual(self.model.speed, 0)

    def test_update_user_stat_with_user(self):
        self.model.user = {'speed': 0, 'mistakes': 0}
        self.model.total_session_len_input = 100
        self.model.total_session_time_typing = 10.0
        self.model.total_session_mistakes = 5
        self.model.update_user_stat()
        self.assertEqual(self.model.user['speed'], 600)
        self.assertEqual(self.model.user['mistakes'], 5)
