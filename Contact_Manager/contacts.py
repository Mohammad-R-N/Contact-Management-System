from dataclasses import dataclass,field
from validators import *
import pickle
import csv
from utils import *


@dataclass
class Contacts:

    name:str
    email:str
    phone:str
    user:str
    category:str = field(default='')
    reminder:str = field(default='')

    @classmethod
    def add_contact(cls,name,email,phone,user,category='',reminder=''):

        if not email_validation(email):
            print("Invalid Email!")
        elif not phone_validation(phone):
            print("Invalid Phone Number!")
        else:
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                with open(contact_file,"rb") as file:
                    info = pickle.load(file)
                    info.append(cls(name,email,phone,user,category,reminder))
                    with open(contact_file,"wb")as file2:
                        pickle.dump(info,file2)
                        print("Contact created")
            else:
                with open(contact_file,"wb") as file:
                    pickle.dump([cls(name,email,phone,user,category,reminder)],file)
                    print("Contact created")


    @classmethod
    def edit_contact(cls,name,user):

        contact_file=os.path.join("data","contacts.pickle")
        with open(contact_file,"rb") as file:
            info = pickle.load(file)
            for index,obj in enumerate(info):
                if obj.name==name and obj.user==user:
                    new_name=get_input("Enter Contact's new name: ")
                    new_email=get_input("Enter Contact's new email: ")
                    new_phone=get_input("Enter Contact's new phone: ")
                    if not email_validation(new_email):
                        print("Invalid Email!")
                    elif not phone_validation(new_phone):
                        print("Invalid Phone Number!")
                    else:
                        new_category=get_input("Category (optional): ")
                        new_reminder=get_input("Reminder (optional): ")
                        info[index].name=new_name
                        info[index].email=new_email
                        info[index].phone=new_phone
                        info[index].category=new_category
                        info[index].reminder=new_reminder
                        with open(contact_file,"wb")as file2:
                            pickle.dump(info,file2)
                        print("Edited successfully")
                        

    @classmethod
    def delete_contact(cls,name,user):

        contact_file=os.path.join("data","contacts.pickle")
        with open(contact_file,"rb") as file:
            info = pickle.load(file)
            for index,obj in enumerate(info):
                if obj.name==name and obj.user==user:
                    del info[index]
                    with open(contact_file,"wb")as file2:
                        pickle.dump(info,file2)                    



def view_all_contacts(user):
        
        contact_file=os.path.join("data","contacts.pickle")
        users_contact=[]
        with open(contact_file,"rb") as file:    
            info = pickle.load(file)
            for obj in info:
                if obj.user == user:
                    users_contact.append(f'''name:{obj.name} - email:{obj.email} - phone:{obj.phone} - category:{obj.category} - reminder:{obj.reminder}\n''')
        print("========================CONTACTS==========================")
        print(*users_contact)            
        print("==========================================================")


def search_contact_by_name(user):

    name=get_input("Enter Contact's name: ")
    contact_file=os.path.join("data","contacts.pickle")
    with open(contact_file,"rb") as file:    
        info = pickle.load(file)
        for obj in info:
            if obj.name == name and obj.user==user:
                print(f'''name:{obj.name} - email:{obj.email} - phone:{obj.phone} - category:{obj.category} - reminder:{obj.reminder}\n''')
                break
        else:
            print("Not found")    


def search_contact_by_email(user):

    email=get_input("Enter Contact's email: ")
    contact_file=os.path.join("data","contacts.pickle")
    with open(contact_file,"rb") as file:    
        info = pickle.load(file)
        for obj in info:
            if obj.name == email and obj.user==user:
                print(f'''name:{obj.name} - email:{obj.email} - phone:{obj.phone} - category:{obj.category} - reminder:{obj.reminder}\n''')
                break
        else:
            print("Not found")    


def category_group(user_category,user):
        
        contact_file=os.path.join("data","contacts.pickle")
        users_contact_by_category=[]
        with open(contact_file,"rb") as file:    
            info = pickle.load(file)
            for obj in info:
                if obj.category == user_category and obj.user==user:
                    users_contact_by_category.append(f'''name:{obj.name} - email:{obj.email} - phone:{obj.phone} - category:{obj.category} - reminder:{obj.reminder}\n''')
        print(f"========================{user_category}==========================")
        print(*users_contact_by_category)            
        print("==========================================================")


def export_contacts(user):

    contact_file=os.path.join("data","contacts.pickle")
    export_file=os.path.join("exports",f"{user}.csv")
    export_list=[]
    with open(contact_file,"rb") as pickle_file:
        info=pickle.load(pickle_file)
        for obj in info:
            if obj.user==user:
                export_list.append([obj.name,obj.phone,obj.email,obj.category,obj.reminder])    
    with open(export_file,"w") as csv_file:
        csv_write=csv.writer(csv_file)
        csv_write.writerows(export_list)


def import_contacts(user):

    import_file=os.path.join("imports",f"{user}.csv")
    with open(import_file,"r") as csv_file:
        csv_read=csv.reader(csv_file)
        for line in csv_read:
            Contacts.add_contact(line[0],line[1],line[2],user,line[3],line[4])


def reminder(user):

    contact_file=os.path.join("data","contacts.pickle")
    contacts_with_reminder=[]
    with open(contact_file,"rb") as file:    
        info = pickle.load(file)
        for find in info:
            if find.reminder!='' and find.user==user:
                contacts_with_reminder.append(f"""reminder:{find.reminder}\nname:{find.name} - phone:{find.phone}\n""")
    print("========================REMINDER==========================")
    print(*contacts_with_reminder)            
    print("==========================================================")


def users_contact(uid):
    while True:
        print("1.Add contact\n2.Edit contact\n3.Delete contact\n4.View all contacts\n5.Search contact\n6.Category Group\n7.Reminder\n8.Import contact\n9.Export contact\n10.EXIT")
        user_order=get_input("Enter your order: ")

        if user_order=="1":
            print("Add contact panel.")
            name=get_input("Enter Contact's name: ")
            email=get_input("Enter Contact's email: ")
            phone=get_input("Enter Contact's Phone: ")
            user=uid
            Contacts.add_contact(name,email,phone,user)


        elif user_order=="2":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Edit panel.")
                name=get_input("Enter Contact's name: ")
                Contacts.edit_contact(name,uid)
            else:
                print("Empty")


        elif user_order=="3":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Delete panel.")
                name=get_input("Enter Contact's name: ")
                Contacts.delete_contact(name,uid)
            else:
                print("Empty")


        elif user_order=="4":
            print("View panel")
            view_all_contacts(uid)


        elif user_order=="5":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Search panel.")
                name_or_email=get_input("1.Search by name\n2.Search by email: ")
                if name_or_email=="1":
                    search_contact_by_name(uid)
                elif name_or_email=="2":
                    search_contact_by_email(uid)
                else:
                    print("Invalid input, Try again!")
            else:
                print("Empty")


        elif user_order=="6":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Category Group panel.")
                user_category=get_input("What is your group name?")
                category_group(user_category,uid)
            else:
                print("Empty")      


        elif user_order=="7":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Reminder panel.")
                reminder(uid)
            else:
                print("Empty") 


        elif user_order=="8":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Import panel.")
                import_contacts(uid)
            else:
                print("Empty")             
    

        elif user_order=="9":
            contact_file=os.path.join("data","contacts.pickle")
            if os.path.exists(contact_file):
                print("Export panel.")
                export_contacts(uid)
            else:
                print("Empty")             
            

        elif user_order=="10":
            exit()