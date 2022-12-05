from entities.reference import Reference

class Article(Reference):
    def __init__(self,author, title, publisher, year, journal = None, volume = None, number = None, pages = None):
        super().__init__(author, title, publisher, year)
        self._journal = journal
        self._volume = volume
        self._number = number
        self._pages = pages
        self._type = "article"

    def get_journal(self):
        return self._journal

    def set_journal(self, journal):
        self._journal = journal

    """def __str__(self):
        return f"{self._author:30} {self._title:40} {self._year:4}"

    def generate_id(self):
        surname = self._author.split(",")
        return surname[0]+str(self._year)"""
