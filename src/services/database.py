import sqlite3

class Database:
    def save(author, title, publisher, year, isbn):
        db = sqlite3.connect("test.db")
        db.isolation_level = None
        values=(author, title, publisher, year, isbn)
        db.execute("INSERT INTO test (author, title, publisher, year, isbn) VALUES (?, ?, ?, ?, ?)",values)
        db.commit()
        db.close()
        return f"Book {title} by {author} saved."
        
    def get():
        db = sqlite3.connect("test.db")
        db.isolation_level = None
        all=db.execute("SELECT * FROM test")
        for row in all:
            print(row)
        db.close()