from validators import *
from utils import *
from dataclasses import dataclass
import pickle
import pathlib


@dataclass
class User:
    username:str
    password:str

    @classmethod
    def create_user(cls,username,password):
        if not username_validation():
            print("This name is taken.")
        elif not password_validation():
            print("Password'lenght should be atleast 8 with numbers and special chars")
        else:
            print("Account created successfully")
            return cls(username,password)
        
    @staticmethod
    def authenticate_user(username,password):
        #? bool
        pass

    def modify_user():
        islogin=User.authenticate_user()
        if islogin:
            new_username=get_input()
            new_password=get_input()
