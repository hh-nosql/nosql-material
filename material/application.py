# You can initialize the MongoDB client here so it is available for every function in this file

print("Welcome to the library application!")

def print_commands():
    print("Commands:")
    print("\t1) List books")
    print("\t2) Add a book")
    print("\t3) Edit a book")
    print("\t4) Delete a book")
    print("\t5) Exit application")

def add_book():
    print("Provide the book's information")
    title = input("Title:")
    year = input("Year:")
    genres = input("Genres (comma separated):")
    copies = input("Number of copies:")
    ebook = input("Is ebook?:")
    author = input("Author ID:")
    
    # Insert the book into the database
    
    print(f"Book {name} has been added!")

def list_books():
    # Find all the books from the database and print their information
    pass

def edit_book():
    print("Which book do you want to edit?")
    # In this case, we could identify the book using the "title" attribute as well
    book_id = input("Book ID:")
    print("Provide the book's new information")

    # Request fields from the user and update the book's fields based on the book's id

def delete_book():
    # Delete a book based on the user's input (e.g. the book's id)
    pass

print_commands()

while True:
    command = input("Type in the command number:")
    
    if command == "1":
        list_books()
    elif command == "2":
        add_book()
    elif command == "3":
        edit_book()
    elif command == "4":
        delete_book()
    elif command == "5":
        break
    else:
        print("I don't know that command")

print("Goodbye!")

    
    
