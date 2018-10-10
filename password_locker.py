
import pyperclip
import string
import random

class Password:

    # this class generates instance of passwords

    password_list=[]

    def __init__(self, first_name , last_name,email, password):
        #removed docstring for simplicity

        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password

    def generate_password(self):
        '''
        method that generates the passwords for the user
        '''
        char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#$%^&*"

        gen_password = "".join(random.choice(char) for _ in range(8))

        return gen_password


    def save_password(self):
            # saves password into password list
            Password.password_list.append(self)

        #  Decorators allow you to make simple modifications to callable objects like functions, methods, or classes.
    def check_existing_password(self):
            # checks if the password exist with that email and return a booleon
        return Password.password_exists(self)

    @classmethod
    def find_by_email(cls, email):

        for password in cls.password_list:
            if password.email == password:
                return password
#   loops through all the saved password and checks if any matches the emails
    @classmethod
    def password_exists(cls, email):
        # checks if the password exists from the password list
        for password in cls.password_list:
            if password.email == password:
                return True

        return False

    @classmethod
    def display_passwords(cls):

        # returns a password list from the password list
        return cls.password_list

    @classmethod
    def copy_email(cls, password):

        # copy the email for the password found
        password_found = password.find_password(password)
        pyperclip.copy(password_found.password)



