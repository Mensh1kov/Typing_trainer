import unittest

from trainer.app.model.utils.data_handler import *


class TestDataHandler(unittest.TestCase):
    def test_create_new_user(self):
        name = 'Ivan'
        user = create_new_user(name)
        self.assertEqual(user['name'], name)
        self.assertEqual(user['texts'], 0)
        self.assertEqual(user['speed'], 0)
        self.assertEqual(user['mistakes'], 0)


if __name__ == '__main__':
    unittest.main()
