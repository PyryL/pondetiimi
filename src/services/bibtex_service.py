from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder

class FileIO:
    def write(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

class BibtexService:
    def __init__(self, file_io = FileIO()):
        self.writer = BibTexWriter()
        self.db = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')
        self.file_io = file_io

    def vie_viite_databaseen(self, viite): #Turha?
        # Tarkistus, onko viite jo db:ssä puuttuu. (Tarkistus suoritettu ref_manager-luokassa?)
        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])

        self.db.entries.append(viite)

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.file_io.write(f"{tiedostonimi}.bib", self.writer.write(self.db))
