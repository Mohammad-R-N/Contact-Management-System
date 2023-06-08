from users import *
from contacts import *
from utils import *
import pickle
import hashlib
if __name__=="__main__":

    while True:
        print("1.Sign in\n2.Sign Up\n3.Modify User\n4.EXIT")
        user_order=get_input("Enter your order: ")

        if user_order == "1":

            username=get_input("Enter your username: ")
            password=get_input("Enter your password: ")
            islogin = User.authenticate_user(username,password)
            if islogin:
                print("welcome!")
                uid=username#+hashlib.sha256(password.encode("utf-8")).hexdigest()[2:6]
                users_contact(uid)
            else:
                print("Invalid user information!")


        elif user_order == "2":

            username=get_input("Enter your username: ")
            password=get_input("Enter your password: ")
            User.create_user(username,password)


        elif user_order == "3":
            
            User.modify_user()


        elif user_order =="4":
            exit()