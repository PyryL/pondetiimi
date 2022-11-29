from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder

class BibtexService:
    def __init__(self):
        self.writer = BibTexWriter()
        self.db = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')
    
    def vie_viite_databaseen(self, viite): #Turha?
        # Tarkistus, onko viite jo db:ssä puuttuu. (Tarkistus suoritettu ref_manager-luokassa?)
        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])

        self.db.entries.append(viite)
    
    def vie_viitteet_tiedostoon(self, tiedostonimi):
        with open(f"{tiedostonimi}.bib", 'w') as bibfile:
            bibfile.write(self.writer.write(self.db))
