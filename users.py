#User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
# import book_info as bookinfo

import re
from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date,timedelta,datetime

class User:
    def __init__(self,name,membership_type,email,library_id):
        self.__name = name
        self.__library_id = library_id
        self.__membership_type = membership_type
        self.__email = email
        self.borrowed_list=[] # {}
        pass

    #setter for library username
    def set_username(self,new_name):
        self.__name = new_name

    # getter for library username
    def get_username(self):
        return self.__name
    
    def set_libraryid(self,new_id):
       self.__library_id = new_id
    
    def get_libraryid(self):
        return self.__library_id
    
    #setter for library user membership type
    def set_membership(self,new_membership_type):
        self.__membership_type = new_membership_type

    def get_membership(self):
        return self.__membership_type
    
    #setter for library username
    def set_email(self,new_email):
        self.__name = new_email

    # getter for library username
    def get_email(self):
        return self.__email

def add_users(user_list):
    user_name = input("Enter the library user name:\n ")
    membership = input("Enter your membership type:\n")
    email = input("Enter your email:\n") # can add validation for email format
    id = input("Enter the library id:\n")
    user_obj1 = User(user_name,membership,email,id)
    user_list[id] = user_obj1  #id is the key , the value is the User object
    pass

def view_user_details(user_list):
    if not user_list:
        print("Sorry user list is empty!!")
        
    try:
        user_ip = input("Please enter the user_id")
        if not user_ip:
            raise ValueError
        else:
            if user_ip in user_list:
                user_details = user_list[user_ip]
                print(f"""------- Details of User : {Fore.RED}{user_details.get_username()}{Style.RESET_ALL}-------
                {Fore.BLUE}  Library User : {Fore.YELLOW}{user_details.get_username()}
                {Fore.BLUE}    Library Id : {Fore.YELLOW}{user_details.get_libraryid()}
                {Fore.BLUE}   Email Address: {Fore.YELLOW}{user_details.get_email()}
                {Fore.BLUE} Membership Type: {Fore.YELLOW}{user_details.get_membership()}""")
                print(Style.RESET_ALL)
            else:
                print("Sorry , Id doesnt exist in our system!!")
    except ValueError:
        print("Hello, userid cannot be empty!!")

    except Exception as e:
        print(f"Unexpected error occured :{e}")
    else:
        print("View User details function executed")
    pass

def display_users(user_list):
    if not user_list:
        print("Sorry user list is empty!!")

    print("Displaying all users\n")
    for details in user_list.values():
        print(f"""------- Details of User : {Fore.YELLOW}{details.get_username()}-------
           {Fore.BLUE}   Library User : {Fore.GREEN}{details.get_username()}
           {Fore.BLUE}     Library Id : {Fore.GREEN}{details.get_libraryid()}
           {Fore.BLUE}   Email Address: {Fore.GREEN}{details.get_email()}
           {Fore.BLUE} Membership Type: {Fore.GREEN}{details.get_membership()}""")
        print(Style.RESET_ALL)

def search_users(user_list):
    pass


def user_menu(user_list): # pass user_list param 
    # dictionary will store the key as the book title and the value will be the whole book object
    while True:
        print("\n1. Add User\n2. View User Details\n3. Search User\n4. Display All Users\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_users(user_list)
        elif choice == "2":
            #check_out(library,current_loans) -- handle in book_info or how to handle here
            view_user_details(user_list)
            pass
        elif choice == "3":
            search_users(user_list)
        elif choice == "4":
            display_users(user_list)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
   

