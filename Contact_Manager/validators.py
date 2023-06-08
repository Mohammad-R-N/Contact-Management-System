import re
from utils import *
import pickle
import os

def username_validation(username:str)->bool:

    user_file=os.path.join("data","users.pickle")
    istaken=False
    isvalid=False
    if os.path.exists(user_file):
        with open (user_file,"rb")as file:
            user_data=pickle.load(file)
            for find in user_data:
                if find.username == username:
                    istaken = True
        if istaken:
            return False
        else:
            isvalid=re.match(r"^[a-zA-Z][a-zA-Z0-9_.-]{,20}$",username)
    else:
        isvalid=re.match(r"^[a-zA-Z][a-zA-Z0-9_.-]{,20}$",username)
    return bool(isvalid)


def password_validation(password:str)->bool:

    isvalid=re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$",password)
    return bool(isvalid)


def email_validation(email:str)->bool:

    isvalid=re.match(r"^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",email)
    return bool(isvalid)


def phone_validation(phone:str)->bool:

    isvalid=re.match(r"^(09(\d{9}))$",phone)
    return bool(isvalid)