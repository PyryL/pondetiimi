from services.bibtex_service import BibtexService

class UI:
    def __init__(self):
        self.bibtex_service = BibtexService()

    def run(self):
        while True:
            print("Komento 'uusi' luo uuden lähdeviitteen")
            print("Komento 'listaa' listaa kaikki lähdeviitteet")
            print("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
            print("Komento 'lopeta' lopettaa ohjelman")

            komento = input("Anna komento:")
            
            if komento == "uusi":
                author = input("Kirjoittaja:")
                title = input("Otsikko:")
                publisher = input("Julkaisija:")
                year = input("Vuosi:")
                isbn = input("ISBN:")
                viite = {"author": author, "title": title, "publisher": publisher, "year": year, "isbn": isbn, "ID": "SukunimiVuosi", "ENTRYTYPE": "book"}
                self.bibtex_service.uusi_viite(viite)

            if komento == "listaa":
                self.bibtex_service.listaa_viitteet()
            
            if komento == "vie":
                tiedostonimi = input("Anna tiedostonimi:")
                self.bibtex_service.vie_viitteet(tiedostonimi)

            if komento == "lopeta":
                break

