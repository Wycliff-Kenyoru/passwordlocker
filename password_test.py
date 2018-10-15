
import pyperclip
import unittest #iporting unitest module
from password import Password #importing password module

class TestPassword(unittest.TestCase):
    # thsi class defines test cases for password class behaviourspython3.6 contact_test.pypython3.6 contact_test.py


    # also helps ccreating test cases

    def setUP(self):
        # method that runs before each test
        self.new_password("wycliff", "kerongo","wycliffkerongogmail.com","110p05124h")

    def test_init(self):
        # to test if the object is initialized properly

        self.assertEqual(self.new_password.first_name, "Wycliff")
        self.assertEqual(self.new_password.last_name, "kerongo")
        self.assertEqual(self.new_password.email, "wycliffkerongogmail.com")
        self.assertEqual(self.new_password.password, "110p05124h")

