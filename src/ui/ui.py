from services.konsoli_io import KonsoliIO
from services.bibtex_service import BibtexService

class UI:
    def __init__(self, io, references):
        self.bibtex_service = BibtexService()
        self._io = io
        self.references = references

    def run(self):
        while True:
            print()
            print("Komento 'uusi' luo uuden lähdeviitteen")
            print("Komento 'listaa' listaa kaikki lähdeviitteet")
            print("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
            print("Komento 'lopeta' lopettaa ohjelman")

            komento = self._io.lue("Anna komento:")

            if komento == "uusi":
                self.references._new_entry(self._io, self.bibtex_service)
            elif komento == "listaa":
                self.bibtex_service.listaa_viitteet()
            elif komento == "vie":
                self.references._export_file(self._io, self.bibtex_service)
            elif komento == "lopeta":
                break
