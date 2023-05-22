import unittest
import app
from datetime import date


class AppTest(unittest.TestCase):
    def test_clean_date(self):
        my_date = app.clean_date("January 31, 2020")
        self.assertIsInstance(my_date, date)
        self.assertEqual(my_date, date(2020, 1, 31))
