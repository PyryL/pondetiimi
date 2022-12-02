from entities.reference import Reference
from services.input_validation import InputValidation
from services.konsoli_io import Varit
from pyfiglet import Figlet

class UI:
    def __init__(self, konsoli_io, reference_manager):
        self._konsoli_io = konsoli_io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            self._tulosta_figlet()
            self._tulosta_menu_ohje()

            komento = self._pyyda_syote("Anna komento:", None, InputValidation.menu_command)

            if komento == "0":
                luettu_viite = self.lue_viite()
                self.reference_manager.lisaa_uusi_viite(luettu_viite)
                self._konsoli_io.tulosta("Uusi viite lisätty!", Varit.vihrea)
            elif komento == "1":
                self.listaa_viitteet()
            elif komento == "2":
                tiedostonimi = self._pyyda_syote("Anna tiedostonimi:", None, InputValidation.not_empty)
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: ", Varit.vihrea, lopetus="")
                self._konsoli_io.tulosta(f"{tiedostonimi}.bib", tummennus=True)
            elif komento == "3":
                # TODO: lähdeviitteen poisto
                pass
            elif komento == "4":
                break

    def _tulosta_menu_ohje(self):
        komennot = {
            "0": "Luo uusi lähdeviite",
            "1": "Listaa kaikki lähdeviitteet",
            "2": "Vie lähdeviitteet bibtex-tiedostoon",
            "3": "Poista lähdeviite",
            "4": "Lopeta ohjelma"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.sininen, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    def lue_viite(self):
        author = self._pyyda_syote("Kirjoittaja:", 13, InputValidation.name)
        title = self._pyyda_syote("Otsikko:", 13, InputValidation.not_empty)
        publisher = self._pyyda_syote("Julkaisija:", 13, InputValidation.not_empty)
        year = self._pyyda_syote("Vuosi:", 13, InputValidation.year)
        isbn = self._pyyda_syote("ISBN:", 13, InputValidation.isbn)

        viite = Reference(author, title, publisher, year, isbn)

        return viite

    def _pyyda_syote(self, kehote, kehotteen_pituus, validator):
        if kehotteen_pituus is None:
            kehotteen_pituus = len(kehote) + 1

        while True:
            self._konsoli_io.tulosta(f"{kehote:<{kehotteen_pituus}}", Varit.keltainen, lopetus="")
            syote = self._konsoli_io.lue("")
            if validator(syote):
                return syote
            self._konsoli_io.tulosta("Virheellinen syöte, yritä uudelleen.", Varit.punainen)

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

    def _tulosta_figlet(self):
        f = Figlet(font='small')
        self._konsoli_io.tulosta(f.renderText('BibTeX-viiteohjelma'), Varit.vihrea)