import re
from entities.reference import Reference

class UI:
    def __init__(self, konsoli_io, reference_manager):
        self._konsoli_io = konsoli_io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            self._tulosta_menu_ohje()

            komento = self._pyyda_syote("Anna komento: ", "(^uusi$)|(^listaa$)|(^vie$)|(^lopeta$)")

            if komento == "uusi":
                luettu_viite = self.lue_viite()
                self.reference_manager.lisaa_uusi_viite(luettu_viite)
                self._konsoli_io.tulosta("Uusi viite lisätty!")
            elif komento == "listaa":
                self.listaa_viitteet()
            elif komento == "vie":
                tiedostonimi = self._konsoli_io.lue("Anna tiedostonimi:")
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: " + tiedostonimi + ".bib!")
            elif komento == "lopeta":
                break

    def _tulosta_menu_ohje(self):
        self._konsoli_io.tulosta("")
        self._konsoli_io.tulosta("Komento 'uusi' luo uuden lähdeviitteen")
        self._konsoli_io.tulosta("Komento 'listaa' listaa kaikki lähdeviitteet")
        self._konsoli_io.tulosta("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
        self._konsoli_io.tulosta("Komento 'lopeta' lopettaa ohjelman")

    def lue_viite(self):
        # Nyt kirjoittajat pilkulla erotettuna --> Kysy jokainen kirjoittaja erikseen.
        author = self._pyyda_syote("Kirjoittaja:", ".+")
        title = self._pyyda_syote("Otsikko:", ".+")
        publisher = self._pyyda_syote("Julkaisija:", ".+")
        year = self._pyyda_syote("Vuosi:", "^\d{4}$")
        isbn = self._pyyda_syote("ISBN:", "^(978-)?\d{3}-\d{5}-\d-\d$")

        viite = Reference(author, title, publisher, year, isbn)

        return viite

    def _pyyda_syote(self, kehote, regexp):
        while True:
            syote = self._konsoli_io.lue(kehote)
            if re.match(regexp, syote):
                return syote
            self._konsoli_io.tulosta("Virheellinen syöte, yritä uudelleen.")

    def listaa_viitteet(self):
        viitteet = self.reference_manager.hae_viitteet()
        eka_rivi = ""

        eka_rivi += "-" * 100

        toka_rivi = f"| Nro: | {'':9} Kirjoittajat: {'':9} | {'':17} Otsikko: {'':17} | Vuosi: |"
        vali_rivi = eka_rivi
        vika_rivi = eka_rivi

        self._konsoli_io.tulosta("\n" + eka_rivi)
        self._konsoli_io.tulosta(toka_rivi)

        for i in range(len(viitteet)):
            self._konsoli_io.tulosta(vali_rivi)

            authors_tuple = viitteet[i].get_author().split(", ")

            title = viitteet[i].get_title()
            year = viitteet[i].get_year()
            tulostettava_rivi = f"|  {i:3} | {authors_tuple[0]:33} | {title:44} | {year:6} |"

            self._konsoli_io.tulosta(tulostettava_rivi)

            for j in range(len(authors_tuple) - 1):
                tulostettava_rivi = "|      | "
                tulostettava_rivi += f"{authors_tuple[j + 1]:33} {'|'} {'':44} {'|'} {'':6} {'|'}"
                self._konsoli_io.tulosta(tulostettava_rivi)

        self._konsoli_io.tulosta(vika_rivi)
