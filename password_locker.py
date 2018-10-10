
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
