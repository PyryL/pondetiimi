from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder
from services.database import Database

class BibtexService:
    def __init__(self):
        self.writer = BibTexWriter()
        self.db = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')

    def uusi_viite(self, viite):
        Database.save(viite["author"], viite["title"], viite["publisher"], viite["year"], viite["isbn"])

    def vie_viitteet(self, tiedostonimi):
        with open(f"{tiedostonimi}.bib", 'w') as bibfile:
            bibfile.write(self.writer.write(self.db))

    def listaa_viitteet(self):
        Database.get()