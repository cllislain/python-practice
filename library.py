import random
from datetime import datetime, timedelta

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.isbn = str(random.randint(10000000000, 99999999999))
        self.due_date = None
        self.borrowed = False
        
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            self.due_date = datetime.now() + timedelta(days=3)
            return True
        else:
            return False
    
    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            self.due_date = None
            return True
        else:
            return False    
        
books = []

try:
    with open("library.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            name = lines[i].strip().split(": ")[1]
            author = lines[i + 1].strip().split(": ")[1]
            books.append(Book(name, author))
except FileNotFoundError:
    print("File no Found: ERROR 8-7000")

borrowed_books = []

try:
    with open("borrowed_books.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            book_name = line.strip()
            for book in books:
                if book.name == book_name:
                    book.borrow()
                    borrowed_books.append(book)                   
except FileNotFoundError:
    print("File no Found: ERROR 8-7000")

def print_book_list():
    for index, book in enumerate(books):
        print(f"{index + 1}. {book.name} by {book.author}")
        
def print_borrowed_books():
    if borrowed_books:
        print("Borrowed Books:")
        for index, book in enumerate(borrowed_books):
            print(f"{index + 1}. {book.name} by {book.author} (Due Date: {book.due_date.strftime('%Y-%m-%d %H:%M:%S')})")
    else:
        print("\nNo books are currently borrowed.")

def save_borrowed_books():
    with open("borrowed_books.txt", "w") as file:
        for book in borrowed_books:
            file.write(f"{book.name} - Due: {book.due_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
def borrow_books():
    if len(borrowed_books) >= 5:
        print("\nBorrow limit reached. Please return some books to borrow again\n")
        return
    
    print("\nAvailable Books:")
    print_book_list()
    
    book_choice = int(input("\nEnter the number of the book you want to borrow: "))

    if 1 <= book_choice <= len(books):
        chosen_book = books[book_choice - 1]
        if chosen_book.borrow():
            borrowed_books.append(chosen_book)
            print("\n" + f"You have borrowed '{chosen_book.name}'.\n")
            save_borrowed_books()  
        else:
            print("This book is already borrowed.")
    else:
        print("Invalid choice.")

def return_books():
    if not borrowed_books:
        print("\nYou haven't borrowed any books.\n")
        return
    
    print("\nBooks you have borrowed:")
    
    for index, book in enumerate(borrowed_books):
        print(f"{index + 1}. {book.name} by {book.author}")
    book_choice = int(input("\nEnter the number of the book you want to return: "))
    
    if 1 <= book_choice <= len(borrowed_books):
        returned_book = borrowed_books.pop(book_choice - 1)
        
        if returned_book.return_book():
            print("\n" + f"You have returned '{returned_book.name}'.\n")
            save_borrowed_books()
        else:
            print("An error occurred while returning the book.")
    else:
        print("Invalid choice.")

while True:
    intro = " WELCOME "
    print("\n" + "*" * 30 + "\n")
    print(intro.center(30, "-"))
    print("\n" + "*" * 30)
    print("\nWhat can we help you with?")
    print("1. Show List of Books")
    print("2. Show List of Borrowed Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        print_book_list()
    elif choice == "2":
        print_borrowed_books()
    elif choice == "3":
        borrow_books()
    elif choice == "4":
        return_books()

    elif choice == "5":
        print("\nThank You and Have a Nice Day!")
        break
        
    else:
        print("Invalid choice. Please choose from 1, 2, or 3.")
