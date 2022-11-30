class Book:
    def __init__(self, author, title, publisher, year, isbn=None):
        self._author = author
        self._title = title
        self._publisher = publisher
        self._year = year
        self._isbn = isbn

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._description = publisher

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def __str__(self):
        return f"{self._author:30} {self._title:40} {self._year:4}"

    def get_as_dictionary(self):
        viite = {"author": self._author,
                 "title": self._title,
                 "publisher": self._publisher,
                 "year": self._year,
                 "isbn": self._isbn,
                 "ID": "SukunimiVuosi",
                 "ENTRYTYPE": "book"}

        return viite

    def generate_id(self):
        surname = self._author.split(",")
        return surname[0]+str(self._year)
