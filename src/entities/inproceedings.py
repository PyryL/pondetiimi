from entities.reference import Reference

class InProceedings(Reference):
    '''
    Konferenssiviiteluokka.
    Args:
        booktitle (String): otsikkotiedot
        pages (String): sivuviitteet
    '''
    def __init__(self,author, title, publisher, year, booktitle = None, pages = None):
        super().__init__(author, title, publisher, year)
        self._booktitle = booktitle
        self._pages = pages
        self._entrytype = "inproceedings"

    def get_booktitle(self):
        return self._booktitle

    def set_booktitle(self, journal):
        self._booktitle = journal

    def get_pages(self):
        return self._pages

    def get_as_dictionary(self):
        viite = {"author": self._author,
                 "title": self._title,
                 "publisher": self._publisher,
                 "year": self._year,
                 "booktitle": self._booktitle,
                 "pages": self._pages,
                 "ID": self._id,
                 "ENTRYTYPE": self._entrytype}

        return viite
