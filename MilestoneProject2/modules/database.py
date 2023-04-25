from .database_connection import DatabaseConnection

def add(title, author):
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor = db.cursor()
        try:
            cursor.execute(f"INSERT INTO books(title, author, read) values (?, ?, 0)", (title, author))
        except:
            cursor.execute(f"UPDATE books SET author = ?, read = 0 WHERE title = ?", (author, title))

def create_table():
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(title text PRIMARY KEY, author text, read integer)")

def get():
    create_table()
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books")
        return [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    

def mark_read(book_title: str):
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor.execute(f"UPDATE books SET read = 1 WHERE title = '{book_title}'")

def drop():
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor.execute("DROP TABLE books")

def rm(title: str):
    with DatabaseConnection("books.db") as db:
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM books WHERE title = ?", (title,))