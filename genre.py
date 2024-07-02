# creating new Genre class for achieveing good modualrity
import re
from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date,timedelta,datetime

class Genre:
    def __init__(self,genre_id,genre_name,description,color_code):
        self.__genre_id = genre_id
        self.__genre_name = genre_name
        self.__description = description
        self.__color_code = color_code
        pass

    def get_genre_id(self):
        return self.__genre_id
    
    def set_genre_id(self,id):
        self.__genre_id = id

    def set_genre_name(self,new_genrename):
        self.__genre_name = new_genrename

    def get_genre_name(self):
        return self.__genre_name
    
    def set_genre_description(self,new_desc):
        self.__genre_description = new_desc

    def get_genre_description(self):
        return self.__description
    
    def set_color_code(self,new_color):
        self.__color_code = new_color

    def get_color_code(self):
        return self.__color_code
    
# - Adding a new genre with genre details.
# - Viewing genre details.
# - Displaying a list of all genres.
        
#genre_id,genre_name,description,color_code

def add_genre(genre_list):
    genre_id = input("Enter the genre ID:\n ")
    genre_name = input("Enter name of your genre:\n")
    description = input("Provide some description:\n")
    color_code = input("Do you want to provide the color code:\n")
    genre_obj1 = Genre(genre_id,genre_name,description,color_code)
    genre_list[genre_id] = genre_obj1 #id is the key , the value is the User object
    return genre_obj1
    pass

def view_genre_details(genre_list):
    if not genre_list:
        print("Sorry, the list is empty! There are no genres added yet!!")
    
    try:
        user_genre_id= input("Specify Genre ID, for which you want details to be listed!!")

        if not user_genre_id:
             raise ValueError
        if user_genre_id in genre_list:
             genre_details = genre_list[user_genre_id]
             print(f"""-----------------{Fore.RED} Genre Insights ---------------------
            {Fore.YELLOW} Genre Id   : {Fore.CYAN}{genre_details.get_genre_id()}
            {Fore.YELLOW} Genre Name : {Fore.CYAN}{genre_details.get_genre_name()}
            {Fore.YELLOW} Description: {Fore.CYAN}{genre_details.get_genre_description()}
            {Fore.YELLOW} Color Code : {Fore.CYAN}{genre_details.get_color_code()} {Style.RESET_ALL}
                    """
                    )
        else:
                print("Sorry, specified Genre Id doesnt exist in our system!!")
    except ValueError:
        print("Hello, Genre Id cannot be empty!!")

    except Exception as e:
        print(f"Unexpected error occured :{e}")
    else:
        print("View Genre details function executed")
    pass

def display_all_genres(genre_list):
    if not genre_list:
        print("There are no genres in our system Currently!!")

    for genre_details in genre_list.values():
        print(f"""------- Genre Details of {Fore.RED}{genre_details.get_genre_name()}-------
            {Fore.YELLOW} Genre Id   : {Fore.CYAN}{genre_details.get_genre_id()}
            {Fore.YELLOW} Genre Name : {Fore.CYAN}{genre_details.get_genre_name()}
            {Fore.YELLOW} Description: {Fore.CYAN}{genre_details.get_genre_description()}
            {Fore.YELLOW} Color Code : {Fore.CYAN}{genre_details.get_color_code()} {Style.RESET_ALL}""")
    pass

def genre_menu(genre_list):
    # dictionary will store the key as the book title and the value will be the whole book object
    while True:
        print("\n1. Add genre\n2. View Genre Details\n3. Display Genre\n4.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_genre(genre_list)
        elif choice == "2":
            #check_out(library,current_loans) -- handle in book_info or how to handle here
            view_genre_details(genre_list)
            pass
        elif choice == "3":
            display_all_genres(genre_list)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
