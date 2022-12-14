import requests
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
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
        self.temporary_database = BibDatabase()
        self.encoder = UnicodeToLatexEncoder(replacement_latex_protection='braces-all')
        self.parser = BibTexParser()
        self.file_io = file_io

    def vie_viite_databaseen(self, viite):
        '''Tarkistus, onko viite jo db:ssä puuttuu.'''
        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])

        self.database.entries.append(viite)

    def vie_viite_temporary_databaseen(self, viite):

        for key in viite:
            viite[key] = self.encoder.unicode_to_latex(viite[key])

        self.temporary_database.entries.append(viite)

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.writer.indent = "      "
        self.file_io.write(f"{tiedostonimi}.bib", self.writer.write(self.database))

    def vie_temporary_databasen_viitelista_tiedostoon(self, tiedostonimi):
        self.writer.indent = "      "
        self.file_io.write(f"{tiedostonimi}.bib", self.writer.write(self.temporary_database))

    def tyhjenna_temporary_bibdatabase(self):
        self.temporary_database = BibDatabase()

    def tyhjenna_bibdatabase(self):
        self.database = BibDatabase()

    def muunna_bibtex_dictionaryksi(self, bibtex_tietue):
        ''' Parse the BibTeX data
            Args: bibtex_tietue
            Transform the BibTeX data into a dictionary
            Returns: dictionary
            '''
        self.parser.customization = convert_to_unicode
        bib_database = bibtexparser.loads(bibtex_tietue, parser=self.parser)

        bib_dict = bib_database.entries[0]

        return bib_dict

    def hae_bibtex_doilla(self, doi):
        bibtex = self.kutsu_bibtex(doi)
        if bibtex is None:
            return None

        tietue = self.muunna_bibtex_dictionaryksi(bibtex)
        return tietue

    def kutsu_bibtex(self, doi):
        url = 'http://dx.doi.org/' + doi
        headers = {'Accept': 'application/x-bibtex'}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text
        return None
