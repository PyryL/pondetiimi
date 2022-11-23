from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

class BibtexService:
    def __init__(self):
        self.writer = BibTexWriter()
        self.db = BibDatabase()

    def uusi_viite(self, viite):
        self.db.entries.append(viite)

    def vie_viitteet(self, tiedostonimi):
        with open(tiedostonimi, 'w') as bibfile:
            bibfile.write(self.writer.write(self.db))
        print(f"Tiedosto {tiedostonimi}.bib luotu")

    def listaa_viitteet(self):
        for viite in self.db.entries:
            print(viite)