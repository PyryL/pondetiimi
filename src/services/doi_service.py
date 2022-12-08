import requests
from services.bibtex_service import BibtexService

class DOIService:
    def __init__(self):
        self.headers = {'Accept': 'application/x-bibtex'}

    def kutsu_bibtex(self, doi):
        url = 'http://dx.doi.org/' + doi
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.text
        else:
            return None

    def hae_bibtex_doilla(self, doi):
        bibtex = self.kutsu_bibtex(doi)
        if bibtex is None:
            return None
        else:
            tietue = BibtexService().muunna_bibtex_dictionaryksi(bibtex)
            return tietue