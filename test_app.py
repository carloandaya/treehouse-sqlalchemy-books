import app
import unittest
from datetime import date


class AppTest(unittest.TestCase):
    def test_clean_date(self):
        my_date = app.clean_date("January 31, 2020")
        self.assertIsInstance(my_date, date)
        self.assertEqual(my_date, date(2020, 1, 31))

    def test_clean_price(self):
        my_price = app.clean_price("50.00")
        self.assertEqual(my_price, 5000)

    def test_clean_id(self): 
        my_id = app.clean_id(3, [1, 3, 5])
        self.assertEqual(my_id, 3)

    def test_choice_validator(self):
        self.assertTrue(app.is_update_delete_choice_valid(1))
        self.assertTrue(app.is_update_delete_choice_valid(2))
        self.assertTrue(app.is_update_delete_choice_valid(3))
        self.assertFalse(app.is_update_delete_choice_valid(4))
        self.assertFalse(app.is_update_delete_choice_valid(0))