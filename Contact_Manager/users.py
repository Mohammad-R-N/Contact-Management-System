from validators import *
from utils import *
from dataclasses import dataclass
import pickle
import pathlib
import os

@dataclass
class User:
    username:str
    password:str

    @classmethod
    def create_user(cls,username,password):

        if not username_validation(username):
            print("This name is taken.")
        elif not password_validation(password):
            print("Password'lenght should be atleast 8 with numbers and special chars")
        else:
            user_file=os.path.join("data","users.pickle")
            info_file=os.Path(user_file)
            if info_file:
                with open(user_file,"rb") as file:
                    info = pickle.load(file)
                    info.append(cls(username,password))
                    with open(user_file,"wb")as file2:
                        pickle.dump(user_file,file2)
            else:
                with open(user_file,"wb") as file:
                    pickle.dump([cls(username,password)],file)

            print("Account created successfully")
            
        
    @staticmethod
    def authenticate_user(username,password):
        #? bool
        pass

    def modify_user():
        islogin=User.authenticate_user()
        if islogin:
            new_username=get_input()
            new_password=get_input()