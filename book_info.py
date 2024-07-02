# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
#Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.

from users import User,user_menu
#from genre import Genre,display_all_genres,view_genre_details,add_genre,genre_info_driver
from genre import Genre,genre_menu,add_genre
from author import Author,author_menu

import re
from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date,timedelta,datetime

# functional example of the library management system

# create a book class to set book attributes and create getters and setters where necessary
# create a series of functions that will take our book objects and store them in a dictionary
# create driver code to prompt the user for their choices

# remove title from author

class Book(Author):
    def __init__(self, title, name,biography,genre,publication_date,date_of_birth="",awards=""):
        super().__init__(name,biography,date_of_birth,awards)
        self.__title = title
        #self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True
        self.__status = "Available"
        self.__due_date = None
        self.__fine_amount=0.0

    # Getter and Setters
    def get_title(self):
        return self.__title
    # no setter for title 
    
    def get_status(self):
        return self.__status
    
    def set_status(self,status_val):
        self._status = status_val
    
    def get_publication_date(self):
        return self.__publication_date
    
    def set_publication_date(self,new_date):
        self.__publication_date = new_date

    def get_due_date(self):
        return self.__due_date
    
    def get_fine_amount(self):
        return self.__fine_amount
    
    def reset_fine(self):
        self.__fine_amount=0.0

    # getter for __is_available
    def get_availability(self):
        return self.__is_available
    
    # setter for availability
    def set_availability(self):
        # if self.__is_available is True we set it to false
        if self.get_availability():
            self.__is_available = False
            self.__status = "Borrowed"
        # else self.__is_available is False we set it to true
        else:
            self.__is_available = True
            self.__status = "Available"

    # getter for author
    # def get_author(self):
    #     return self.__author

    # def set_author(self,new_author):
    #     self.__author = new_author

    # name and biography
    # def set_name(self, new_name):
    #     return super().set_name(new_name)
    
    def get_name(self):
        return super().get_name()
    
    # def set_biography(self, new_biography):
    #     return super().set_biography(new_biography)
    
    def get_biography(self):
        return super().get_biography()
    
    # getter for genre
    def get_genre(self):
        return self.__genre
    
    def valid_date(self,prompt):
       while True:
        date_str = input(prompt) 
        try:
            borrow_date = datetime.strptime(date_str,"%Y-%m-%d")
            return borrow_date
        except ValueError:
            print("Invalid date format. Please enter date in format YYYY-MM-DD format!!")
        
    # method for borrowing a book
    def borrow_book(self):
     try:
         while True:
                borrow_date_str = input("Enter book borrowing date (YYYY-MM-DD): ")
                try:
                    borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
                    break  # Break out of the loop if date input is valid
                except ValueError:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                    continue  # Prompt user again for valid date

        # if its available then we set use the setter to set it to the opposite which is False
         if self.get_availability():
            self.__status = "Borrowed"
            self.set_availability()
            #self.__due_date = date.today() + timedelta(14)
            self.__due_date = borrow_date + timedelta(14)
            print(f"""
                    Book Borrowed : {Fore.CYAN} {self.get_title()} {Style.RESET_ALL}
                         Due Date : {Fore.LIGHTMAGENTA_EX}{self.get_due_date()} {Style.RESET_ALL}
                  """)
            print(f"Kindly return book {Fore.YELLOW}{self.get_title()}{Style.RESET_ALL} within 14 days from the date of borrow to avoid Paying Fines!!")
            return True #returns True that we are able to borrow the book
         else:
            print(f"Book {self.get_title()} is not available for borrowing")
            return False
         
     except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        return False
     except Exception as e:
        print(f"Error: {e}")
        return False
     finally:
         print("Executed borrow book method\n")   
     pass
         
    def calculate_fine(self,days):
        if days < 5:
            return days * 2.0
        elif days >= 5 and days <= 20:
            return 5*2.0 + (days-5)*5.0
        else:
            return 5 * 2.0 + (15 * 5.0) + (days-20)* 8.0
        pass

    def return_book(self):
         try:
           while True:
                return_date_str = input("Enter book returning date (YYYY-MM-DD): ")
                try:
                    return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
                    break  # Break out of the loop if date input is valid
                except ValueError:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                    continue  # Prompt user again for valid date

           if self.__due_date and return_date > self.__due_date :
              diff_day = (return_date - self.__due_date).days
              print("diference day", diff_day)

              self.__fine_amount=self.calculate_fine(diff_day)

              print(f"Fine amount incurred is: {self.__fine_amount}")

              self.set_availability() #sets the availability back to true if its False
              self.__status = "Available"
              self.__due_date = None 
              return True
          
         except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting...")
            return False
         except Exception as e:
            print(f"Error encountered : {e}")
            return False
         finally:
            print("Executed return book method\n")   

# functionality for adding information to our dictionary which is defined in the main function below
def add_book(library,genre_val):
    title = input("Enter the book's title:\n ")
    genre = genre_val
    publication_date =input("Enter the publication date:\n")
    name = input("Enter the author's name: ")
    biography = input("Enter the author's biography: ")
    book = Book(title, name,biography, genre,publication_date)
    library[title] = book #title is the key the value is the book object
    pass
# reserve dictionary -- hold books which was reserved by users

reserve={}
def reserve_books(library,title,user_name):
    if title not in library:
        print(f"Sorry, book {title} doesnt exist in library")
    else:
        if title in reserve:
            #reserve[title].append(user_name) # if mutiple users reserve or we can modify by throwing error
            print(f"Book {title}, has already been reserved by another user!!")
            return False
        else:
            reserve[title] = user_name    #[ reserve[Famous five] : 'John Berry']
            
    print("Displaying reserve queue:")
    for title_key,user_value in reserve.items():
        print(f"{Fore.GREEN}Book : {Fore.LIGHTBLUE_EX}{title_key} ,{Fore.LIGHTMAGENTA_EX} User : {Fore.RED}{user_value} {Style.RESET_ALL}")
    print()
    return True
    pass

def check_out(library,user_list):
    title = input("Please enter the book you'd like to check out")
    if not title:
        print("Book doesnt exist in the database!!")

   #user_id of new user
    user_id = input("Please enter your library id")
    # checks if the title(key) is in the library and checking if we can borrow the book
    if user_id in user_list:
        user = user_list[user_id]
    else:
        print(f"User with id {Fore.RED}{user_id} doesnt exist {Style.RESET_ALL}")
        return

    if title in library and library[title].borrow_book():
        #current_loans[title] = user
        user.borrowed_list.append(library[title].get_title())
        print(f"""  .............................................       
                {Fore.GREEN}Book Borrowed Details {Style.RESET_ALL}
              ..........................................................
              {Fore.YELLOW}       Book : {Fore.BLUE} {library[title].get_title()}
              {Fore.YELLOW} Checked out: {Fore.BLUE} {user.get_username()} 
              {Fore.YELLOW}      Email : {Fore.BLUE} {user.get_email()} 
              {Fore.YELLOW}     UserId : {Fore.BLUE} {user_id} {Style.RESET_ALL}""")
        
        print(f"Book status is : {Fore.BLUE}{library[title].get_status()}{Style.RESET_ALL}")
    else:
        print("Book is not available or not found")
        user_ip = input("Do you want to reserve the book?")
        if user_ip == "yes":
            if reserve_books(library,library[title].get_title(),user.get_username()) == "True":
                print(f"Hi,{user.get_username()}!! Your book has been reserved. We will update you , once book {Fore.LIGHTMAGENTA_EX}{library[title].get_title()} becomes available {Style.RESET_ALL}!!")
            else:
                print(f"Unable to reserve book at the moment!!")
        else:
            print("No probs,have a good day!1")
    pass

def return_checked_book(library, user_list):
        title = input("Please enter the book you'd like to return")
        user_id = input("Please enter your library id")
      
        if user_id in user_list:
            user = user_list[user_id]
        else:
            print(f"User with id{user_id} doesnt exist")
            return 

        if title in library and library[title].return_book():
            fine_amt = library[title].get_fine_amount()
            print(f""" Book : {library[title].get_title()} 
                Returned by : {user.get_username()} 
                 User Email : {user.get_email()} 
                         Id : {user_id} {Style.RESET_ALL}
                 Fine Amount: $ {fine_amt:.2f}""") 
            
            print(f"Book {Fore.BLUE}{title}'s status is : {library[title].get_status()}{Style.RESET_ALL}")

            # print fine info and prompt
             
            if fine_amt > 0:
                print(f"Hi {user.get_username()}, you still have to pay fine ${fine_amt}")
                user_ip = input("Reply paid if you already paid your fine").lower()

                if user_ip == "paid":
                    print("Good job, you paid the fine. There are no dues pending!!")
                    library[title].reset_fine()
                else:
                    print("Fine payment pending. Please pay as soon as possible.")

                pass

            print(f"Notifying user who reserved the book :{Fore.LIGHTRED_EX} {title}{Style.RESET_ALL}")

            for key,value in reserve.items():
                print(f"Hey, User:{Fore.BLUE}{value}{Style.RESET_ALL},the book your reserved : {Fore.GREEN}{title} {Style.RESET_ALL} is now Available again!!")
        else:
            print(f"Book: {title} is not available or not found")
        pass

def search_book(library):
    # search by title,author name, genre id or name
    print(f"""    {Fore.CYAN}
             -----  Search Options: ------
              1. Search by Book Title
              2. Search by Author name
              3. Search by Genre Id
                 {Style.RESET_ALL}
          """)
    title = input("What is the title you're looking for?")
    if title in library:
        book = library[title]
        print("Book found, here is some info: ")
        print(f"""--- Book Details------
             Book title:{Fore.GREEN}{book.get_title()}
            Author Name:{Fore.YELLOW}{book.get_name()}
       Author biography:{Fore.RED}{book.get_biography()}
            Genre Id :{Fore.GREEN}{book.get_genre().get_genre_id()}
            Genre Name :{Fore.CYAN}{book.get_genre().get_genre_name()}
       Genre Desription:{Fore.BLUE}{book.get_availability()}{Style.RESET_ALL}""")
    else:
        print("Sorry! That book is not in our library.")

    user_ip = input("Do you want to search by author name").lower()
    if user_ip == "yes":
        author_name = input("Enter the author name whose book you would like to search?")
        if not author_name:
            print("Author_name is mandatory for your search!!")

        for title,book in library.items():
           if book.get_name().lower() == author_name.lower():
                 print("Book with this Author found") 
                 print(f"""---{Fore.BLUE} Book Details------{Style.RESET_ALL}
                      {Fore.YELLOW} Book title:{Fore.RED}{book.get_title()}
                      {Fore.YELLOW}Author Name:{Fore.RED}{book.get_name()}
                 {Fore.YELLOW}Author biography:{Fore.RED}{book.get_biography()}
                        {Fore.YELLOW}Genre Id :{Fore.RED}{book.get_genre().get_genre_id()}
                      {Fore.YELLOW}Genre Name :{Fore.RED}{book.get_genre().get_genre_name()}
                 {Fore.YELLOW}Genre Desription:{Fore.RED}{book.get_availability()}{Style.RESET_ALL}""")
        else:
            print(f"The Author :{author_name}'s book is unavailable")

    user_ip = input("Do you want to search by Genre Id").lower()
    if user_ip == "yes":
        genre_id = input("Enter the Genre ID related to the book you would like to search?")
        if not genre_id:
            print("Genre Id is mandatory for your search!!")

        for title,book in library.items():
           if book.get_genre().get_genre_id() == genre_id:
                 print("Book with this Author found") 
                 print(f"""---{Fore.BLUE} Book Details------{Style.RESET_ALL}
                      {Fore.YELLOW} Book title:{Fore.RED}{book.get_title()}
                      {Fore.YELLOW}Author Name:{Fore.RED}{book.get_name()}
                 {Fore.YELLOW}Author biography:{Fore.RED}{book.get_biography()}
                        {Fore.YELLOW}Genre Id :{Fore.RED}{book.get_genre().get_genre_id()}
                      {Fore.YELLOW}Genre Name :{Fore.RED}{book.get_genre().get_genre_name()}
                 {Fore.YELLOW}Genre Desription:{Fore.RED}{book.get_availability()}{Style.RESET_ALL}""")
        else:
            print(f"The Author :{author_name}'s book is unavailable")


def find_book(library,title):
        # loop through our list of book objects and match a title to a title attribute
        for title in library:
            book = library[title]
            return book
        return None # returns None if we cant find the book in our list
    # will be used in the lend_book method below

def display_books(library):
    for book in library.values():
        if book.get_genre() is not None:
            print(f"""
            {Fore.YELLOW}  Title : {Fore.GREEN} {book.get_title()} 
            {Fore.YELLOW} Author Details
            {Fore.YELLOW}  Name  : {Fore.GREEN} {book.get_name()} ,{Fore.YELLOW} Biography : {Fore.GREEN} {book.get_biography()}
            {Fore.YELLOW} (Genre: {Fore.GREEN} {book.get_genre().get_genre_name()} ,{Fore.CYAN}{book.get_genre().get_genre_id()}, {Fore.YELLOW} Description : {Fore.GREEN}{book.get_genre().get_genre_description()})
  {Fore.YELLOW}Book Availability : {Fore.GREEN} {book.get_availability()} 
  {Fore.YELLOW} Publication Date : {Fore.GREEN} {book.get_publication_date()} {Style.RESET_ALL}""")
        else:
            print("Genre object wasnt found:")
            print(f"""
              Title : {book.get_title()} 
     (Author Details):    
        Author Name : {book.get_author()} 
         Biography  : {book.get_biography()}
  Book Availability : {book.get_availability()} 
   Publication Date : {book.get_publication_date()}""")

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
            #can add validation for user_id
            raise ValueError
        else:
            if user_ip in user_list:
                  user_details = user_list[user_ip]
                  print(f"""------- Details of User : {user_details.get_username()}-------
                  Library User : {Fore.MAGENTA}{user_details.get_username()} 
                       User Id : {Fore.MAGENTA}{user_details.get_libraryid()}
                    User Email : {Fore.MAGENTA}{user_details.get_email()}
               Membership Type : {Fore.MAGENTA}{user_details.get_membership()}{Style.RESET_ALL}""")
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
        print(f"""------- Details of User : {details.get_username()}-------
                  Library User : {details.get_username()} 
                        UserId : {details.get_libraryid()}
                    User Email : {details.get_email()}
               Membership Type : {details.get_membership()}""")
        
# driver code
# def main():
#     # dictionary will store the key as the book title and the value will be the whole book object
#     library = {} #this would be fine as a list too
#     current_loans = {}
#     user_list = {} 
#     auth_list= {}
#     genre_list = {}
#     while True:
#         print("""
#               1. Add Book
#               2. Return Book
#               3. Search Book
#               4. Display All Books
#               5. Add Users to the system 
#               6. Allow Users to checkout books 
#               7. View User Details 
#               8. Display User List 
#               9. Add Author Info
#               10. Display all Authors Info
#               11. View Author Info
#               12. Display genres, add genre
#               13. Exit""")
        
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             genre = add_genre(genre_list)
#             add_book(library,genre)
#         elif choice == "2":
#             #title = input("enter the book, you would like to return")
#             return_checked_book(library,user_list)
#         elif choice == "3":
#             search_book(library)
#         elif choice == "4":
#             display_books(library)
#         elif choice == "5":
#             # user_obj = User("name","membership_type","email","library_id")
#             add_users(user_list)
#         elif choice == "6":
#             #add_users(user_list)
#             check_out(library,user_list)
#         elif choice == "7":
#             view_user_details(user_list)
#         elif choice == "8":
#             display_users(user_list)
#         elif choice == "9":
#             #author_obj = Author("J.K Rowling","Goblet of Fire","12/04/1992","Life of Azbahan","Emmy Award")
#             add_author_info(auth_list)
#         elif choice == "10":
#             display_all_author_info(auth_list)
#         elif choice == "11":
#             view_author_details(auth_list)
#         elif choice == "12":
#             display_all_genres(genre_list)
#         elif choice == "13":
#             print("Exit...........Exiting")
#             break
#         elif choice == "14":
#             print("Invalid choice")


def book_menu(library,genre_list,user_list):

    while True:
        print("""
              1. Add Book
              2. Return Book
              3. Search Book
              4. Display All Books
              5. Allow Users to checkout books 
              6. Exit""")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            genre = add_genre(genre_list)
            add_book(library,genre)
        elif choice == "2":
            return_checked_book(library,user_list)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            check_out(library,user_list)
        elif choice == "6":
            print("Exit...........Exiting")
            break
        else:
            print("Invalid choice")

#driver code
def main():
    # dictionary will store the key as the book title and the value will be the whole book object
    library = {} #this would be fine as a list too
    #current_loans = {}
    user_list = {} 
    auth_list= {}
    genre_list = {}
    while True:
        print(f"""{Fore.YELLOW}
                  Main Menu:
                  {Fore.GREEN}
              1. Book Operations
              2. User Operations
              3. Author Operations
              4. Genre Operations
              5. Exit

                  {Style.RESET_ALL}
              """)
        
        choice = input("Enter your choice: ")
        if choice == "1":
             book_menu(library,genre_list,user_list)
        elif choice == "2":
            user_menu(user_list)
        elif choice == "3":
            author_menu(auth_list)
        elif choice == "4":
            genre_menu(genre_list)
        elif choice == "5":
            print("You have chosen to exit....Exciting...")
            break
        else:
            print("Invalid Choice. Please chose from (1-5)Options")

main()
