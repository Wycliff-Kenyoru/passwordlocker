
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

    def test_save_password(self):
        # testing if the password object is saved into our password list
        self.new_password.save_password()  # saving new password
        self.assertEqual(len(Password.password_list), 1)

    def test_save_multiple_password(self):
        # checks if we can save multiple passwords to our list
        self.new_password.save_password()
        test_password = Password("Test", "user", "wycliffkerongo@gmail.com", "110p05124h")
        test_password.save_password()
        self.assertEqual(len(Password.password_list), 1)

    def test_delete_password(self):
        # check if we can remove password from our list
        self.password.save_password()
        test_password = Password("Test", "user", "wycliffkerongo@gmail.com", "110p05124h")
        test_password.save_password()
        self.new_password.delete_password()  # deleting password
        self.assertEqual(len(Password.password_list), 1)

    def test_find_by_email(self):
        # checking if the password is in the list and the display the info
        self.new_password.save_password()
        test_password = Password("Test", "user", "duncanarani@gmail.com", "31740141")
        test_password.save_password()
        found_password = Password.find_by_email("31740141")

        self.assertEqual(found_password.email, password.email)

    def test_password_exists(self):
        # checking if we return the booleon if the passoword is not found
        self.new_password.Password()
        test_password = Password("Test", "user", "duncanarani@gmail.com", "31740141")
        test_password.save_password()

        password_exists = Password.password_exists("31740141")
        self.assertTrue(password_exists)

    def test_display_all_passwords(self):
        # this returns alist of all password saved
        self.assertEqual(Password.display_password(), Password.password_list)

    def test.

        copy_email(self)
    # confirm that we are copying the email from the found password
    self.new_password.save_password()
    Password.copy_email("password")

    assertEqual(self.new_password.email, pyperclip.paste())

    if __name__ == '__main__':
        unittest.main()
