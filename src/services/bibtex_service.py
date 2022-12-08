import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from pylatexenc.latexencode import UnicodeToLatexEncoder
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

import requests

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
        self.parser = BibTexParser()    
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

    def muunna_bibtex_dictionaryksi(self, bibtex_tietue):
        # Parse the BibTeX data
        self.parser.customization = convert_to_unicode
        bib_database = bibtexparser.loads(bibtex_tietue, parser=self.parser)

        # Transform the BibTeX data into a dictionary
        bib_dict = bib_database.entries[0]

        # Return the dictionary
        return bib_dict

    def hae_bibtex_doilla(self, doi):
        bibtex = self.kutsu_bibtex(doi)
        if bibtex is None:
            return None
        else:
            tietue = self.muunna_bibtex_dictionaryksi(bibtex)
            return tietue

    def kutsu_bibtex(self, doi):
        url = 'http://dx.doi.org/' + doi
        headers = {'Accept': 'application/x-bibtex'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return None
