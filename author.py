#Author: A class representing book authors with attributes like name and biography.
#    Author Operations:
#         1. Add a new author
#         2. View author details
#         3. Display all authors

import re
from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date,timedelta,datetime

class Author:
    def __init__(self,name,biography,date_of_birth,awards) :
        self.__name = name
        self.__biography = biography
        self.__date_of_birth = date_of_birth
        self.__awards = awards
        pass

    def set_name(self,new_name):
        self.__name = new_name
    pass

    def get_name(self):
        return self.__name
    pass

    def set_awards(self,award_info):
        self.__awards = award_info
    pass

    def get_awards(self):
        return self.__awards
    pass
    def get_date_of_birth(self):
        return self.__date_of_birth
    pass

    def set_biography(self,new_biography):
        self.__biography = new_biography
    pass

    def get_biography(self):
        return self.__biography 
    pass

def add_author_info(author_list):
    name = input("Enter author name\n")
    bio = input("Enter your biography details\n")
    date_of_birth = input("Enter your Date of Birth\n")
    awards = input("Enter the awards")
    author_obj= Author(name,bio,date_of_birth,awards)
    author_list[name] = author_obj
    pass

# display specific author details(view author detail based on Author Name)

def view_author_details(author_list):
    if not author_list:
        print("Sorry, the list is empty! There are no genres added yet!!")
    
    try:
        author_id= input("Specify Author Name, whose details you want to be listed!!")

        if not author_id:
             raise ValueError
        if author_id in author_list:
             author_info = author_list[author_id]
             print(f"""----------------- Author Insights ---------------------
             {Fore.BLUE} Author Name : {Fore.GREEN}{author_info.get_name()}
             {Fore.BLUE} Biography   : {Fore.GREEN}{author_info.get_biography()}
             {Fore.BLUE}Date Of Birth: {Fore.GREEN}{author_info.get_date_of_birth()}
             {Fore.BLUE}     Awards  : {Fore.GREEN}{author_info.get_awards()}{Style.RESET_ALL}
                    """)
                     #Book Title  : {author_info.get_book_title()}
        else:
                print("Sorry, specified AuthorName doesnt exist in our system!!")
    except ValueError:
        print("Hello, Author Name cannot be empty!!")

    except Exception as e:
        print(f"Unexpected error occured :{e}")
    else:
        print("View Author details function executed")
    pass

#display list of all authors
def display_all_author_info(author_list):
    if not author_list:
        print("Sorry there are no authors added in our system!!")

    print("Here are the authors present in our system currently:")
    for author in author_list.values():
        print(f"""-----------{Fore.BLUE} Author details --------------
        {Fore.YELLOW} Author Name : {Fore.RED} {author.get_name()}
        {Fore.YELLOW} Biography   : {Fore.RED}{author.get_biography()}
       {Fore.YELLOW} Date Of Birth: {Fore.RED}{author.get_date_of_birth()}
       {Fore.YELLOW}       Awards : {Fore.RED}{author.get_awards()}{Style.RESET_ALL}
              """)
    pass

def author_menu(author_list):
    # dictionary will store the key as the book title and the value will be the whole book object 
    while True:
        print("\n1. Add Author Info\n2. View Author Information\n3. Display All Author Details\n4.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_author_info(author_list)
        elif choice == "2":
            #check_out(library,current_loans) -- handle in book_info or how to handle here
            view_author_details(author_list)
            pass
        elif choice == "3":
            display_all_author_info(author_list)
        elif choice == "4":
            print("You chose to Exit....Exciting!!")
            break
        else:
            print("Invalid choice")

