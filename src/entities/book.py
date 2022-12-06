from entities.reference import Reference

class Book(Reference):
    '''
    Kirjaluokka:
    Args:
        isbn (String):
    '''
    def __init__(self,author, title, publisher, year, isbn=None):
        super().__init__(author, title, publisher, year)
        self._isbn = isbn
        self._type = "book"

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn
