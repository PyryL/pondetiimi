from services.bibtex_service import BibtexService

class UI:
    def __init__(self):
        self.bibtex_service = BibtexService()

    def run(self):
        while True:
            print()
            print("Komento 'uusi' luo uuden lähdeviitteen")
            print("Komento 'listaa' listaa kaikki lähdeviitteet")
            print("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
            print("Komento 'lopeta' lopettaa ohjelman")

            komento = input("Anna komento:")
            
            if komento == "uusi":
                self._new_entry()
            elif komento == "listaa":
                self.bibtex_service.listaa_viitteet()
            elif komento == "vie":
                self._export_file()
            elif komento == "lopeta":
                break
    
    def _new_entry(self):
        author = input("Kirjoittaja:")
        title = input("Otsikko:")
        publisher = input("Julkaisija:")
        year = input("Vuosi:")
        isbn = input("ISBN:")
        viite = {"author": author, "title": title, "publisher": publisher, "year": year, "isbn": isbn, "ID": "SukunimiVuosi", "ENTRYTYPE": "book"}
        self.bibtex_service.uusi_viite(viite)

    def _export_file(self):
        tiedostonimi = input("Anna tiedostonimi:")
        self.bibtex_service.vie_viitteet(tiedostonimi)
        print(f"Tiedosto {tiedostonimi}.bib luotu")