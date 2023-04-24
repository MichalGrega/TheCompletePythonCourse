import sqlite3

def add(title, author):
    create_table()
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    try:
        cursor.execute(f"INSERT INTO books(title, author, read) values (?, ?, 0)", (title, author))
    except:
        cursor.execute(f"UPDATE books SET author = ?, read = 0 WHERE title = ?", (author, title))
    db.commit()
    db.close()

def create_table():
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(title text PRIMARY KEY, author text, read integer)")
    db.commit()
    db.close()

def get():
    create_table()
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    return [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    

def mark_read(book_title: str):
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE books SET read = 1 WHERE title = '{book_title}'")
    db.commit()
    db.close()

def drop():
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE books")
    db.commit()
    db.close()

def rm(title: str):
    db = sqlite3.connect("books.db")
    cursor = db.cursor()
    print(title)
    # cursor.execute(f"DELETE FROM books WHERE title = '{title}'")
    print((title))
    cursor.execute(f"DELETE FROM books WHERE title = ?", (title,))
    db.commit()
    db.close()