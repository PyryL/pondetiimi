from entities.reference import Reference

class Book(Reference):
    '''
    Kirjaluokka:
    Args:
        isbn (String):
    '''
    def __init__(self,author, title, publisher, year, isbn):
        super().__init__(author, title, publisher, year)
        self._isbn = isbn
        self._type = "book"

    def get_isbn(self):
        return self._isbn

    def get_as_dictionary(self):
        viite = {"author": self._author,
                 "title": self._title,
                 "publisher": self._publisher,
                 "year": self._year,
                 "isbn": self._isbn,
                 "ID": self._id,
                 "ENTRYTYPE": self._entrytype}

        return viite