from services.input_validation import InputValidation

class Reference:
    '''
    Viiteluokkien kattoluokka.
        Args:

    '''
    def __init__(self, author, title, publisher, year, isbn = None, entrytype = None):
        self._author = author
        self._title = title
        self._publisher = publisher
        self._year = str(year)
        self._isbn = isbn
        self._id = self.generate_id()
        self._entrytype = entrytype or "book"

    def get_entrytype(self):
        return self._entrytype

    def get_id(self):
        return self._id

    def get_author(self):
        return self._author

    def set_author(self, author):
        if InputValidation.name(author):
            self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        if InputValidation.isbn(isbn):
            self._isbn = isbn

    def get_year(self):
        return self._year

    def set_year(self, year):
        if InputValidation.year(year):
            self._year = year

    def get_as_dictionary(self):
        viite = {"author": self._author,
                 "title": self._title,
                 "publisher": self._publisher,
                 "year": self._year,
                 "isbn": self._isbn,
                 "ID": self._id,
                 "ENTRYTYPE": self._entrytype}

        return viite

    def generate_id(self):
        # ensimmäinen sukunimi, nimen ensimmäinen sana ja vuosi
        return (
            self.get_author().split(",")[0] +
            self.get_title().split(" ")[0] +
            str(self.get_year())
        )
