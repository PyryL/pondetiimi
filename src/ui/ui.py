from entities.reference import Reference
from services.input_validation import InputValidation

class UI:
    def __init__(self, konsoli_io, reference_manager):
        self._konsoli_io = konsoli_io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            self._tulosta_menu_ohje()

            komento = self._pyyda_syote("Anna komento: ", InputValidation.menu_command)

            if komento == "0":
                luettu_viite = self.lue_viite()
                self.reference_manager.lisaa_uusi_viite(luettu_viite)
                self._konsoli_io.tulosta("Uusi viite lisätty!")
            elif komento == "1":
                self.listaa_viitteet()
            elif komento == "2":
                tiedostonimi = self._konsoli_io.lue("Anna tiedostonimi:")
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: " + tiedostonimi + ".bib!")
            elif komento == "3":
                # TODO: lähdeviitteen poisto
                pass
            elif komento == "4":
                break

    def _tulosta_menu_ohje(self):
        self._konsoli_io.tulosta("")
        self._konsoli_io.tulosta("0 Luo uusi lähdeviite")
        self._konsoli_io.tulosta("1 Listaa kaikki lähdeviitteet")
        self._konsoli_io.tulosta("2 Vie lähdeviitteet bibtex-tiedostoon")
        self._konsoli_io.tulosta("3 Poista lähdeviite")
        self._konsoli_io.tulosta("4 Lopeta ohjelma")

    def lue_viite(self):
        # Nyt kirjoittajat pilkulla erotettuna --> Kysy jokainen kirjoittaja erikseen.
        author = self._pyyda_syote("Kirjoittaja:", InputValidation.not_empty)
        title = self._pyyda_syote("Otsikko:", InputValidation.not_empty)
        publisher = self._pyyda_syote("Julkaisija:", InputValidation.not_empty)
        year = self._pyyda_syote("Vuosi:", InputValidation.year)
        isbn = self._pyyda_syote("ISBN:", InputValidation.isbn)

        viite = Reference(author, title, publisher, year, isbn)

        return viite

    def _pyyda_syote(self, kehote, validator):
        while True:
            syote = self._konsoli_io.lue(kehote)
            if validator(syote):
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
