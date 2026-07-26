class Book:
    def __init__(self,book_id,title,author,price,quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self):
        try:
            b_id = int(input("Enter Book id: "))
            b_title = input("Enter Book Name: ")
            b_author = input("Enter Author name: ")
            b_price = int(input("Enter Book Price: "))
            b_quantity = int(input("Enter Total Book Quantity: "))
            new_book = Book(b_id,b_title,b_author,b_price,b_quantity)
            self.book_list.append(new_book)
        except ValueError:
            print("Enter number Only....")


    def view_books(self):
        if not self.book_list:
            print("NO books Available")

        else:
            for book in self.book_list:
                print(f"Book-ID: {book.book_id}")
                print(f"Book Name: {book.title}")
                print(f"Author Name: {book.author}")
                print(f"Price: {book.price}")
                print(f"Total Book Quantity: {book.quantity}")
                print("-"*20)

    def search_book(self):
        try:
            id_to_search = int(input("Enter id: "))
            if not self.book_list:
                print("NO Books Available")
            else:
                for book in self.book_list:
                    if id_to_search == book.book_id:
                        print(f"Book Name: {book.title}")
                        print(f"Author Name: {book.author}")
                        print(f"Price: {book.price}")
                        print(f"Total Book Quantity: {book.quantity}")
                        break

                else:
                    print("BOOK NOT FOUND")
        except ValueError:
            print("Enter number Only....")


    def delete_book(self):
        try:
            id_to_delete = int(input("Enter id: "))
            if not self.book_list:
                print("NO Books Available")
            else:
                for book in self.book_list:
                    if id_to_delete == book.book_id:
                        self.book_list.remove(book)
                        print("Book Deleted....")
                        break
                else:
                    print("Book Not Found")
        except ValueError:
            print("Enter number only....")                

    def update_bookinfo(self):
        try:
            id_to_update = int(input("Enter id: "))
            if not self.book_list:
                print("NO Books Available")
            else:
                for book in self.book_list:
                    if id_to_update == book.book_id:
                        book.title = input("Enter Book Name: ")
                        book.author = input("Enter Author name: ")
                        book.price = int(input("Enter Book Price: "))
                        book.quantity = int(input("Enter Total Book Quantity: "))
                        print("Book info updated....")
                        break
                else:
                    print("Book Not Found")
        except ValueError:
            print("Enter number only....")                
        
library_obj = Library()
while True:
    print("### LIBRARY MANAGEMENT SYSTEM ###")
    print("1. ADD BOOK")
    print("2. VIEW ALL BOOKS")
    print("3. SEARCH BOOKS")
    print("4. DELETE BOOKS")
    print("5. UPDATE BOOKS INFO")
    print("0. EXIT")

    try: 
        user_input = int(input("Choose Option: "))
    except ValueError:
        print("Enter number only...")

    if user_input == 0:
        print("Thank You")
        break
    elif user_input == 1:
        library_obj.add_book()
        print("BOOK ADDED SUCCESSFULLY...")
        print("\n\n")
    elif user_input == 2:
        library_obj.view_books()
        print('\n\n')
    elif user_input == 3:
        library_obj.search_book()
        print('\n\n')
    elif user_input == 4:
        library_obj.delete_book()
        print('\n\n')
    elif user_input == 5:
        library_obj.update_bookinfo()
        print('\n\n')
    else:
        print("Invalid Option")