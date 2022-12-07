from entities.reference import Reference
from services.input_validation import InputValidation

class Article(Reference):
    '''
    Artikkeliluokka.
    Args:
        journal (String): 
        volume (String):
        number (String):
        pages (String):
        '''
    def __init__(self,author,
                    title, publisher,
                    year, journal = None,
                    volume = None, number = None,
                    pages = None):
        super().__init__(author, title, publisher, year)
        self._journal = journal
        self._volume = volume
        self._number = number
        self._pages = pages
        self._entrytype = "article"

    def get_journal(self):
        return self._journal

    def set_journal(self, journal):
        if InputValidation.not_empty(journal):
            self._journal = journal

    def get_volume(self):
        return self._volume

    def get_number(self):
        return self._number

    def get_pages(self):
        return self._pages

    def get_as_dictionary(self):
        viite = {"author": self._author,
                 "title": self._title,
                 "publisher": self._publisher,
                 "year": self._year,
                 "journal": self._journal,
                 "volume": self._volume,
                 "number": self._number,
                 "pages": self._pages,
                 "ID": self._id,
                 "ENTRYTYPE": self._entrytype}

        return viite
