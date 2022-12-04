from entities.reference import Reference

class Book(Reference):
    def __init__(self,author, title, publisher, year, isbn=None):
        super().__init__(author, title, publisher, year)
        self._isbn = isbn
        self._type = "book"

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def __str__(self):
        return f"{self._author:30} {self._title:40} {self._year:4}"

    def generate_id(self):
        surname = self._author.split(",")
        return surname[0]+str(self._year)
