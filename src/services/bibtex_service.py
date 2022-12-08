from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder

class FileIO:
    '''
    Bibtex tiedoston luominen.
    Args:
        filename (String): tiedoston nimi
        content (String): tiedoston sisältö
    '''
    def write(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

class BibtexService:
    '''
    Bibtex toiminnot.
    '''
    def __init__(self, file_io = FileIO()):
        self.writer = BibTexWriter()
        self.database = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')
        self.file_io = file_io

    def vie_viite_databaseen(self, viite): #Turha?
        # Tarkistus, onko viite jo db:ssä puuttuu. (Tarkistus suoritettu ref_manager-luokassa?)
        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])

        self.database.entries.append(viite)

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.file_io.write(f"{tiedostonimi}.bib", self.writer.write(self.database))

    def tyhjenna_bibdatabase(self):
        self.database = BibDatabase()