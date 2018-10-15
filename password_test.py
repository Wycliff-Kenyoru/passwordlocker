
import pyperclip
import unittest #iporting unitest module
from password import Password #importing password module

class TestPassword(unittest.TestCase):
    # thsi class defines test cases for password class behaviourspython3.6 contact_test.pypython3.6 contact_test.py


    # also helps ccreating test cases

    def setUP(self):
        # method that runs before each test
        self.new_password("wycliff", "kerongo","wycliffkerongogmail.com","110p05124h")
