from validators import *
from utils import *
from dataclasses import dataclass
import pickle
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
            print("Password's lenght should be atleast 8 with numbers and special chars")
        else:
            user_file=os.path.join("data","users.pickle")
            if os.path.exists(user_file):
                with open(user_file,"rb") as file:
                    info = pickle.load(file)
                    info.append(cls(username,password))
                    with open(user_file,"wb")as file2:
                        pickle.dump(info,file2) 
            else:
                with open(user_file,"wb") as file:
                    pickle.dump([cls(username,password)],file)

            print("Account created successfully")
            
        
    @classmethod
    def authenticate_user(cls,username,password):

        user_file=os.path.join("data","users.pickle")
        if os.path.exists(user_file):
            with open(user_file,"rb") as file:
                user_data=pickle.load(file)
                if cls(username,password) in user_data:
                    return True
        else:
            return False


    @classmethod
    def modify_user(cls):

        username=get_input("Enter your username: ")
        password=get_input("Enter your password: ")
        islogin = User.authenticate_user(username,password)
        if islogin:
            contact_file=os.path.join("data","contacts.pickle")
            user_file=os.path.join("data","users.pickle")
            print("welcome!")
            with open(user_file,"rb") as file:
                user_data=pickle.load(file)
                user_index=user_data.index(cls(username,password))
                new_username=get_input("Enter your new username: ")
                new_password=get_input("Enter your new Password: ")
                
                if not username_validation(new_username):
                    print("This name is taken.")
                elif not password_validation(new_password):
                    print("Password's lenght should be atleast 8 with numbers, UPPERcase alpha, lowercase alpha and special chars")
                else:
                    user_data[user_index].username=new_username
                    user_data[user_index].password=new_password
                    with open (user_file,"wb") as file:
                        pickle.dump(user_data,file)
                    with open(contact_file,"rb") as file1:
                        info=pickle.load(file1)
                        for index,obj in enumerate(info) :
                            if obj.user==username:
                                info[index].user=new_username
                        with open (contact_file,"wb") as file2:
                            pickle.dump(info,file2)
                    print("Account modified successfully")
                
        else:
            print("Invalid user information!")
