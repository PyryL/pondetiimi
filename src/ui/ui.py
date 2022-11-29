from services.konsoli_io import KonsoliIO
from services.reference_manager import ReferenceManager
from entities.reference import Reference

class UI:
    def __init__(self, io, reference_manager):
        self._io = io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            print()
            print("Komento 'uusi' luo uuden lähdeviitteen")
            print("Komento 'listaa' listaa kaikki lähdeviitteet")
            print("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
            print("Komento 'lopeta' lopettaa ohjelman")

            komento = self._io.lue("Anna komento: ")

            if komento == "uusi":
                luettu_viite = self.lue_viite()
                self.reference_manager.lisaa_uusi_viite(luettu_viite)
            elif komento == "listaa":
                self.listaa_viitteet()
            elif komento == "vie":
                tiedostonimi = self._io.lue("Anna tiedostonimi:")
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
            elif komento == "lopeta":
                break

    def lue_viite(self):
        author = self._io.lue("Kirjoittaja:") #Nyt kirjoittajat pilkulla erotettuna --> Kysy jokainen kirjoittaja erikseen.
        title = self._io.lue("Otsikko:")
        publisher = self._io.lue("Julkaisija:")
        year = self._io.lue("Vuosi:")
        isbn = self._io.lue("ISBN:")

        viite = Reference(author, title, publisher, year, isbn)

        return viite

    def listaa_viitteet(self):
        viitteet = self.reference_manager.hae_viitteet()
        eka_rivi = ""

        for k in range(100):
            eka_rivi += "-"

        toka_rivi = f"{'| Nro: |'} {'':9} {'Kirjoittajat:'} {'':9} {'|'} {'':17} {'Otsikko:'} {'':17} {'|'} {'Vuosi: |'}"
        vali_rivi = eka_rivi
        vika_rivi = eka_rivi

        self._io.tulosta("\n" + eka_rivi)
        self._io.tulosta(toka_rivi)

        for i in range(len(viitteet)):
            self._io.tulosta(vali_rivi)

            authors_tuple = viitteet[i].get_author().split(", ")

            tulostettava_rivi = f"{'| '} {i:3} {'|'} {authors_tuple[0]:33} {'|'} {viitteet[i].get_title():44} {'|'} {viitteet[i].get_year():6} {'|'}"

            self._io.tulosta(tulostettava_rivi)

            for j in range(len(authors_tuple) - 1):
                tulostettava_rivi = "|      | "
                tulostettava_rivi += f"{authors_tuple[j + 1]:33} {'|'} {'':44} {'|'} {'':6} {'|'}"
                self._io.tulosta(tulostettava_rivi)

        self._io.tulosta(vika_rivi)
