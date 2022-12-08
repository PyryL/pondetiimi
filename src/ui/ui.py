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

            if komento == "0":
                self._tulosta_ohje_eri_viitetyyppien_lisaykselle()
                # Korjaa validation ja lisää
                lisattavan_viitetyypin_numero = self._pyyda_syote("Anna komento:", 
                                                                    None, InputValidation.hakumenu_command)

                if lisattavan_viitetyypin_numero == "0":
                    luettu_viite = self.lue_kirja()
                    #TARK ONKO JO LISTALLA TOIMII KUNNOLLA?
                    if not self.reference_manager.lisaa_uusi_viite(luettu_viite):
                        self._konsoli_io.tulosta("Viite on jo listalla!", Varit.PUNAINEN)
                    else:
                        self._konsoli_io.tulosta("Uusi kirjaviite on lisätty!", Varit.VIHREA)
                elif lisattavan_viitetyypin_numero == "1":
                    luettu_viite = self.lue_artikkeli()

                    if not self.reference_manager.lisaa_uusi_viite(luettu_viite):
                        self._konsoli_io.tulosta("Viite on jo listalla!", Varit.PUNAINEN)
                    else:
                        self._konsoli_io.tulosta("Uusi artikkeliviite on lisätty!", Varit.VIHREA)
                elif lisattavan_viitetyypin_numero == "2":
                    luettu_viite = self.lue_kongerenssiviite()

                    if not self.reference_manager.lisaa_uusi_viite(luettu_viite):
                        self._konsoli_io.tulosta("Viite on jo listalla!", Varit.PUNAINEN)
                    else:
                        self._konsoli_io.tulosta("Uusi konferenssiviite on lisätty!", Varit.VIHREA)

            elif komento == "1":
                self.listaa_viitteet(self.reference_manager.hae_viitteet())
            elif komento == "2":
                tiedostonimi = self._pyyda_syote\
                    ("Anna tiedostonimi:", None, InputValidation.not_empty)
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: ", Varit.VIHREA, lopetus="")
                self._konsoli_io.tulosta(f"{tiedostonimi}.bib", tummennus=True)
            elif komento == "3":
                poistettavan_lahdeviitteen_numero = int(self._pyyda_syote\
                    ("Anna poistettavan lähdeviitteen numero:", None, InputValidation.not_empty))
                if self.reference_manager.poista_viite_viitteen_numeron_mukaan(poistettavan_lahdeviitteen_numero):
                    self._konsoli_io.tulosta("Viite poistettu!", Varit.VIHREA, lopetus="")
                else:
                    self._konsoli_io.tulosta("Viitettä annetulla viitteen numerolla ei ole. Viitteen poisto epäonnistui.",
                                                Varit.PUNAINEN, lopetus="")
            elif komento == "4":
                self._tulosta_haku_ohje()
                hakukomento = self._pyyda_syote("Anna komento:", None, InputValidation.hakumenu_command)
                #INPUT VALIDATION ok?
                if hakukomento == "0":
                    kirjoittaja = self._pyyda_syote("Anna haettava kirjoittaja:", None, InputValidation.name)
                    lista_viitteista_haetulla_kirjoittajalla = self.reference_manager.hae_viitteista_kirjoittajalla(kirjoittaja)
                    if len(lista_viitteista_haetulla_kirjoittajalla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_kirjoittajalla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                if hakukomento == "1":
                    otsikko = self._pyyda_syote("Anna haettava otsikko:",
                                                None, InputValidation.not_empty)
                    lista_viitteista_haetulla_otsikolla = self.reference_manager.hae_viitteista_otsikolla(otsikko)
                    if len(lista_viitteista_haetulla_otsikolla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_otsikolla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                if hakukomento == "2":
                    julkaisija = self._pyyda_syote("Anna haettava julkaisija:",
                                                    None, InputValidation.not_empty)
                    lista_viitteista_haetulla_julkaisijalla = self.reference_manager.hae_viitteista_julkaisijalla(julkaisija)
                    if len(lista_viitteista_haetulla_julkaisijalla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_julkaisijalla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                if hakukomento == "3":
                    vuosiluku = self._pyyda_syote("Anna haettava vuosiluku:", None, InputValidation.year)
                    lista_viitteista_haetulla_vuosiluvulla = self.reference_manager.hae_viitteista_vuosiluvulla(vuosiluku)
                    if len(lista_viitteista_haetulla_vuosiluvulla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_vuosiluvulla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                #Ongelma muille viitetyypeille?
                if hakukomento == "4":
                    isbn = self._pyyda_syote("Anna haettava isbn:", None, InputValidation.isbn)
                    lista_viitteista_haetulla_isbnlla = self.reference_manager.hae_viitteista_isbnlla(isbn)
                    if len(lista_viitteista_haetulla_isbnlla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_isbnlla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                if hakukomento == "5":
                    avainsana = self._pyyda_syote("Anna haettava avainsana:",
                                                    None, InputValidation.not_empty)
                    lista_viitteista_haetulla_avainsanalla = self.reference_manager.hae_viitteista_avainsanalla(avainsana)
                    if len(lista_viitteista_haetulla_avainsanalla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_avainsanalla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.",
                                                    Varit.PUNAINEN, lopetus="")
                if hakukomento == "x":
                    continue
            elif komento == "5":
                doi = self._pyyda_syote("Anna haettava DOI:", None, InputValidation.doi)
                viite = self.reference_manager.hae_viite_doi(doi)
                if viite is not None:
                    self._konsoli_io.tulosta("Viite löytyi.")
                    self._konsoli_io.tulosta(viite, Varit.KELTAINEN)
                else:
                    self._konsoli_io.tulosta("Viitettä annetulla DOI:lla ei löytynyt.",
                                                Varit.PUNAINEN, lopetus="")
            elif komento == "6":
                break

    def _tulosta_menu_ohje(self):
        komennot = {
            "0": "Luo uusi lähdeviite",
            "1": "Listaa kaikki lähdeviitteet",
            "2": "Vie lähdeviitteet bibtex-tiedostoon",
            "3": "Poista lähdeviite",
            "4": "Hae hakusanalla",
            "5": "Hae viite DOI:n perusteella",
            "6": "Lopeta ohjelma"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    def _tulosta_ohje_eri_viitetyyppien_lisaykselle(self):
        komennot = {
            "0": "Lisää uusi kirjaviite",
            "1": "Lisää uusi artikkeliviite",
            "2": "Lisää uusi konferenssiviite",
            "x": "Palaa takaisin"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    def _tulosta_haku_ohje(self):
        komennot = {
            "0": "Hae kirjoittajalla",
            "1": "Hae otsikolla",
            "2": "Hae julkaisijalla",
            "3": "Hae vuosiluvulla",
            "4": "Hae ISBN:llä",
            "5": "Hae avainsanalla",
            "x": "Palaa takaisin"
        }       
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    def lue_kirja(self):
        author = self._pyyda_syote("Kirjoittaja:", 13,
                                                InputValidation.name, "nimi")
        title = self._pyyda_syote("Otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        publisher = self._pyyda_syote("Julkaisija:", 13,
                                                InputValidation.not_empty, "julkaisija")
        year = self._pyyda_syote("Vuosi:", 13,
                                                InputValidation.year, "vuosi")
        isbn = self._pyyda_syote("ISBN:", 13,
                                                InputValidation.isbn, "isbn")

        viite = Book(author, title, publisher, year, isbn)
        return viite

    def lue_artikkeli(self):
        author = self._pyyda_syote("Kirjoittaja:", 13,
                                                InputValidation.name, "nimi")
        title = self._pyyda_syote("Otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        publisher = self._pyyda_syote("Julkaisija:", 13,
                                                InputValidation.not_empty, "julkaisija")
        year = self._pyyda_syote("Vuosi:", 13,
                                                InputValidation.year, "vuosi")
        journal = self._pyyda_syote("Lehti:", 13,
                                                InputValidation.not_empty, "lehti")
        volume = self._pyyda_syote("Vuosikerta:", 13,
                                                InputValidation.not_empty, "vuosikerta")
        number = self._pyyda_syote("Numero:", 13,
                                                InputValidation.not_empty, "numero")
        pages = self._pyyda_syote("Sivut:", 13,
                                                InputValidation.not_empty, "sivut")

        viite = Article(author, title, publisher, year, journal, volume, number,pages)
        return viite

    def lue_kongerenssiviite(self):
        author = self._pyyda_syote("Kirjoittaja:", 13,
                                                InputValidation.name, "nimi")
        title = self._pyyda_syote("Otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        publisher = self._pyyda_syote("Julkaisija:", 13,
                                                InputValidation.not_empty, "julkaisija")
        year = self._pyyda_syote("Vuosi:", 13,
                                                InputValidation.year, "vuosi")
        booktitle = self._pyyda_syote("Kirjan otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        pages = pages = self._pyyda_syote("Sivut:", 13,
                                                InputValidation.not_empty, "sivut")

        viite = InProceedings(author, title, publisher, year, booktitle, pages)
        return viite

    def _pyyda_syote(self, kehote, kehotteen_pituus, validator, virheilmoitus_tyyppi="tyhja"):
        if kehotteen_pituus is None:
            kehotteen_pituus = len(kehote) + 1

        while True:
            self._konsoli_io.tulosta(f"{kehote:<{kehotteen_pituus}}", Varit.KELTAINEN, lopetus="")
            syote = self._konsoli_io.lue()
            if validator(syote):
                return syote
            self._konsoli_io.tulosta(InputValidation.error_message(virheilmoitus_tyyppi), Varit.PUNAINEN)

    def listaa_viitteet(self, viitteet):
        eka_rivi = ""
        eka_rivi += "-" * 207

        toka_rivi = f"| Nro: |  Viitetyyppi:  | {'':5} Kirjoittajat: {'':5} | {'':10} Otsikko: {'':10} |  Julkaisija:  | Vuosi: | {'':5} ISBN: {'':5} | {'':6} Journal {'':7} | Volume: | Number: |   Booktitle:    |   Pages:   |"

        vali_rivi = eka_rivi
        vika_rivi = eka_rivi

        self._konsoli_io.tulosta("\n" + eka_rivi)
        self._konsoli_io.tulosta(toka_rivi)

        for i in range(len(viitteet)):
            self._konsoli_io.tulosta(vali_rivi)

            authors_tuple = viitteet[i].get_author().split("; ")

            title = viitteet[i].get_title()
            publisher = viitteet[i].get_publisher()
            year = viitteet[i].get_year()
            isbn = "-"
            journal = "-"
            volume = "-"
            number = "-"
            booktitle = "-"
            pages = "-"
            entry_type = viitteet[i].get_entrytype()

            if entry_type == "book":
                isbn = viitteet[i].get_isbn()
            elif entry_type == "article":
                journal = viitteet[i].get_journal()
                volume = viitteet[i].get_volume()
                number = viitteet[i].get_number()
                pages = viitteet[i].get_pages()
            elif entry_type == "proceedings":
                booktitle = viitteet[i].get_booktitle()
                pages = viitteet[i].get_pages()

            tulostettava_rivi = f"|  {i:3} | {entry_type:14} | {authors_tuple[0]:25} | {title:30} | {publisher:13} | {year:6} | {isbn:17} | {journal:22} | {volume:7} | {number:7} | {booktitle:15} | {pages:10} |"

            self._konsoli_io.tulosta(tulostettava_rivi)

            for j in range(len(authors_tuple) - 1):
                tulostettava_rivi = f"|      | {'':14} | {authors_tuple[j + 1]:25} | {'':30} | {'':13} | {'':6} | {'':17} | {'':22} | {'':7} | {'':7} | {'':15} | {'':10} |"
                self._konsoli_io.tulosta(tulostettava_rivi)

        self._konsoli_io.tulosta(vika_rivi)

    def _tulosta_figlet(self):
        figlet = Figlet(font='small')

        self._konsoli_io.tulosta("\n")
        self._konsoli_io.tulosta(figlet.renderText('BibTeX-viiteohjelma'), Varit.VIHREA)
