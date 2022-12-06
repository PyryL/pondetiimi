from pyfiglet import Figlet
from entities.book import Book
from entities.article import Article
from entities.inproceedings import InProceedings
from services.input_validation import InputValidation
from services.konsoli_io import Varit


class UI:
    '''
    Sovelluksen käyttöliittymä.
    '''
    def __init__(self, konsoli_io, reference_manager):
        self._konsoli_io = konsoli_io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            self._tulosta_figlet()
            self._tulosta_menu_ohje()

            komento = self._pyyda_syote("Anna komento:", None, InputValidation.menu_command)

            if komento[0] == "0":
                if komento == "01":
                    luettu_viite = self.lue_kirja()
                    self.reference_manager.lisaa_uusi_viite(luettu_viite)
                    self._konsoli_io.tulosta("Uusi kirjaviite on lisätty!", Varit.VIHREA)
                elif komento == "02":
                    luettu_viite = self.lue_artikkeli()
                    self.reference_manager.lisaa_uusi_viite(luettu_viite)
                    self._konsoli_io.tulosta("Uusi artiikkeliviite on lisätty!", Varit.VIHREA)
                elif komento == "03":
                    luettu_viite = self.lue_kongerenssiviite()
                    self.reference_manager.lisaa_uusi_viite(luettu_viite)
                    self._konsoli_io.tulosta("Uusi konferenssiviite on lisätty!", Varit.VIHREA)
            elif komento == "1":
                self.listaa_viitteet()
            elif komento == "2":
                tiedostonimi = self._pyyda_syote\
                    ("Anna tiedostonimi:", None, InputValidation.not_empty)
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: ", Varit.VIHREA, lopetus="")
                self._konsoli_io.tulosta(f"{tiedostonimi}.bib", tummennus=True)
            elif komento == "3":
                # TODO: lähdeviitteen poisto
                pass
            elif komento == "4":
                break

    def _tulosta_menu_ohje(self):
        komennot = {
            "0X": "Luo uusi lähdeviite: [01] Kirja, [02] Artiikkeli, [03] Konferenssiviite",
            "1": "Listaa kaikki lähdeviitteet",
            "2": "Vie lähdeviitteet bibtex-tiedostoon",
            "3": "Poista lähdeviite",
            "4": "Lopeta ohjelma"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    def lue_kirja(self):
        author = self._pyyda_syote("Kirjoittaja:", 13, InputValidation.name)
        title = self._pyyda_syote("Otsikko:", 13, InputValidation.not_empty)
        publisher = self._pyyda_syote("Julkaisija:", 13, InputValidation.not_empty)
        year = self._pyyda_syote("Vuosi:", 13, InputValidation.year)
        isbn = self._pyyda_syote("ISBN:", 13, InputValidation.isbn)

        viite = Book(author, title, publisher, year, isbn)
        return viite

    def lue_artikkeli(self):
        author = self._pyyda_syote("Kirjoittaja:", 13, InputValidation.name)
        title = self._pyyda_syote("Otsikko:", 13, InputValidation.not_empty)
        publisher = self._pyyda_syote("Julkaisija:", 13, InputValidation.not_empty)
        year = self._pyyda_syote("Vuosi:", 13, InputValidation.year)
        journal = self._pyyda_syote("Lehti:", 13, InputValidation.not_empty)
        volume = self._pyyda_syote("Vuosikerta:", 13, InputValidation.not_empty)
        number = self._pyyda_syote("Numero:", 13, InputValidation.not_empty)
        pages = self._pyyda_syote("Sivut:", 13, InputValidation.not_empty)

        viite = Article(author, title, publisher, year, journal, volume, number,pages)
        return viite

    def lue_kongerenssiviite(self):
        author = self._pyyda_syote("Kirjoittaja:", 13, InputValidation.name)
        title = self._pyyda_syote("Otsikko:", 13, InputValidation.not_empty)
        publisher = self._pyyda_syote("Julkaisija:", 13, InputValidation.not_empty)
        year = self._pyyda_syote("Vuosi:", 13, InputValidation.year)
        booktitle = self._pyyda_syote("Otsikko:", 13, InputValidation.not_empty)
        pages = pages = self._pyyda_syote("Sivut:", 13, InputValidation.not_empty)

        viite = InProceedings(author, title, publisher, year, booktitle, pages)
        return viite

    def _pyyda_syote(self, kehote, kehotteen_pituus, validator):
        if kehotteen_pituus is None:
            kehotteen_pituus = len(kehote) + 1

        while True:
            self._konsoli_io.tulosta(f"{kehote:<{kehotteen_pituus}}", Varit.KELTAINEN, lopetus="")
            syote = self._konsoli_io.lue("")
            if validator(syote):
                return syote
            self._konsoli_io.tulosta("Virheellinen syöte, yritä uudelleen.", Varit.PUNAINEN)

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
        figlet = Figlet(font='small')
        self._konsoli_io.tulosta(figlet.renderText('BibTeX-viiteohjelma'), Varit.VIHREA)
