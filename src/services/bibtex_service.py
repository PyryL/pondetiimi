from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder

class BibtexService:
    def __init__(self):
        self.writer = BibTexWriter()
        self.db = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')

    def uusi_viite(self, viite):
        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])
        self.db.entries.append(viite)

    def vie_viitteet(self, tiedostonimi):
        with open(f"{tiedostonimi}.bib", 'w') as bibfile:
            bibfile.write(self.writer.write(self.db))

    def listaa_viitteet(self):
        for viite in self.db.entries:
            print(viite)