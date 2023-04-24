import modules.database as db

# db.drop()
# db.create_table()
# db.add("Fourth book", "Third2 Author")

# print('List books:')
# print(db.get())

# print('Update:')
# db.mark_read("Third book")
# for row in db.get():
#     print(row)

MENU_TEXT = """
Select your action:
    'a' - add a book
    'l' - list books
    'd' - delete book
    'r' - mark as read
    'q' - quit
"""

def menu():
    choice = ""
    while choice != "q":
        choice = input(MENU_TEXT)
        if choice == "a":
            add_book()
        elif choice == "l":
            get_books()
        elif choice == "r":
            mark_read()
        elif choice == "d":
            delete()

def add_book():
    title = input("Book title: ")
    author = input("Book author: ")
    db.add(title, author)

def get_books():
    for book in db.get():
        print(f"{book['title']}, {book['author']}, {'Read' if book['read'] else 'Unread'}")
        
def mark_read():
    title = input('Book title: ')
    db.mark_read(title)

def delete():
    title = input('Book title: ')
    db.rm(title)
menu()