from dataclasses import dataclass
import pickle
import pathlib
import csv
from utils import *


@dataclass
class Contacts:
    name:str
    email:str
    phone:str

    @classmethod
    def add_contact(cls,name,email,phone):
        return cls(name,email,phone)

    def edit_contact(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        return "DONE"
    
    def delete_contact(self):
        #?delete by name
        pass

def view_all_contacts():
    #?list of user's contacts
    pass


def search_contact():
    #?email or name
    pass

def contact_category():
    pass

def export_contacts():
    pass

def import_contacts():
    pass

def reminder():
    pass


def users_contact():
    while True:
        print("1.Add contact\n2.Edit contact\n3.Delete contact\n4.View all contacts\n5.Search contact\n6.Cantact category\n7.Reminder\n8.Import contact\n9.Export contact\n10.EXIT")
        user_order=get_input("Enter your order: ")
        if user_order=="1":
            Contacts.add_contact()
        elif user_order=="2":
            pass
        elif user_order=="3":
            pass
        elif user_order=="4":
            pass
        elif user_order=="5":
            pass
        elif user_order=="6":
            pass
        elif user_order=="7":
            pass
        elif user_order=="8":
            pass
        elif user_order=="9":
            pass
        elif user_order=="10":
            exit()