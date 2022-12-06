from entities.reference import Reference

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
        self._journal = journal

    def get_volume(self):
        return self.get_volume

    def get_number(self):
        return self._number

    def get_pages(self):
        return self._pages
