In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.



Enhanced User Interface (UI) and Menu:



Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
    Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit
Book Operations:
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books

User Operations:
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users

Author Operations:
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors




Class Structure:



Implement a class structure that represents key entities in the library management system, including:
Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
Author: A class representing book authors with attributes like name and biography.


Encapsulation:

Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.


Modules:

Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.


Menu Actions:

Implement the following actions in response to menu selections using the classes you've created:


- Adding a new book with all relevant details.
- Allowing users to borrow a book, marking it as "Borrowed."
- Allowing users to return a book, marking it as "Available."
- Searching for a book by its unique identifier (title) and displaying its details.
- Displaying a list of all books with their unique identifiers.
- Adding a new user with user details.
- Viewing user details.
- Displaying a list of all users.
- Adding a new author with author details.
- Viewing author details.
- Displaying a list of all authors.
- Quitting the application.


User Interaction:

Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)


Error Handling:

Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

The below bonus requirements have been added as well: