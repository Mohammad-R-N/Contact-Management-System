from users import *
from contacts import *
from utils import *

if __name__=="__main__":
    while True:
        print("1.Sign in\n2.Sign Up\n3.Modify User\n4.EXIT")
        user_order=get_input("Enter your order: ")

        if user_order == "1":
            username=get_input("Enter your username.")
            password=get_input("Enter your password.")
            islogin = User.authenticate_user(username,password)
            if islogin:
                print("welcome!")
                users_contact()
            else:
                print("Invalid user information!")

        elif user_order == "2":
            User.create_user()

        elif user_order == "3":
            User.modify_user()

        elif user_order =="4":
            exit()