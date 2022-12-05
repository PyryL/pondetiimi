from entities.reference import Reference

class InProceedings(Reference):
    def __init__(self,author, title, publisher, year, booktitle = None, pages = None):
        super().__init__(author, title, publisher, year)
        self._booktitle = booktitle
        self._pages = pages
        self._type = "inproceedings"

    def get_journal(self):
        return self._journal

    def set_journal(self, journal):
        self._journal = journal