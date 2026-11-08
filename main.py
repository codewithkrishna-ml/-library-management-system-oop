#PROJECT-Library Management System
class Library:
    def __init__(self):
        self.books_list = ["python" , "java" , "C++"]
        self.lent_books = {}

    def display_books(self):
        if len(self.books_list) ==0:
            print("there is no books in library")
        else:
           print("\n----Available books------")
           for books in self.books_list:
                print(books)
                print("----------------------\n")

    def borrow_book(self , book_name):
        if book_name in self.books_list:
            self.books_list.remove(book_name)
            print(f"successfully {book_name} has been issued to you")
        else:
            print(f"sorry, {book_name} is already issued to someone esle or does not exist")

    def return_book(self, book_name):
        self.books_list.append(book_name)
        print(f" {book_name} is successfully returned to library")

class Student:
    def request_book(self):
        book = input("Enter the name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Enter the name of the book you want to return:")
        return book

central_library = Library()
student_user = Student()

while True:
    print("\n1.Display book \n2. Request a book \n3. Return a book \n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        central_library.display_books()
    elif choice == 2:
        requested_book = student_user.request_book()
        central_library.borrow_book(requested_book)
    elif choice == 3:
        returned_book = student_user.return_book()
        central_library.return_book(returned_book)
    elif choice == 4:
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
