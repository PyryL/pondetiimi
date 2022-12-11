from pyfiglet import Figlet
from prettytable import PrettyTable, SINGLE_BORDER as PrettyTableStyle
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

            if len(self.reference_manager.get_filtterit()) > 0:
                self._tulosta_filtterit_ja_operandit(self.reference_manager.get_filtterit(), "and")

            self._tulosta_menu_ohje()

            self._konsoli_io.tulosta("")
            komento = self._pyyda_syote("Anna komento:", None, InputValidation.menu_command)
            self._konsoli_io.tulosta("")

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
                if len(self.reference_manager.get_filtterit()) > 0:
                    filtteroity_lista = self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and() #Nyt vain yksi operandi 'AND'
                    
                    if len(filtteroity_lista) > 0:
                        self.listaa_viitteet(filtteroity_lista)
                    else:
                        self._konsoli_io.tulosta("\nViitteitä asetetuilla filttereillä ei löytynyt!",
                                                Varit.PUNAINEN, lopetus="")
                else:
                    self.listaa_viitteet(self.reference_manager.hae_viitteet())

            elif komento == "2":
                tiedostonimi = self._pyyda_syote\
                    ("Anna tiedostonimi:", None, InputValidation.not_empty)
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
                self._konsoli_io.tulosta("Viitteet viety tiedostoon: ", Varit.VIHREA, lopetus="")
                self._konsoli_io.tulosta(f"{tiedostonimi}.bib", tummennus=True)
            
            elif komento == "3":
                self.listaa_viitteet(self.reference_manager.hae_viitteet())
                poistettavan_lahdeviitteen_numero = int(self._pyyda_syote\
                    ("Anna poistettavan lähdeviitteen numero:", None, InputValidation.not_empty))
                if self.reference_manager.poista_viite_viitteen_numeron_mukaan(poistettavan_lahdeviitteen_numero):
                    self._konsoli_io.tulosta("Viite poistettu!", Varit.VIHREA, lopetus="")
                else:
                    self._konsoli_io.tulosta("Viitettä annetulla viitteen numerolla ei ole. Viitteen poisto epäonnistui.",
                                                Varit.PUNAINEN, lopetus="")

            elif komento == "4":
                while(True):                   
                    if len(self.reference_manager.get_hakusanat()) > 0:
                        self._tulosta_hakusanat_ja_operandit(self.reference_manager.get_hakusanat(), "and")

                    hakusana = self._pyyda_syote("\nLisää hakusana [tyhjä lopettaa]:", None, InputValidation.hakusana) #Lisää InputValidation.hakusana

                    if hakusana == "":
                        break

                    if self.reference_manager.hakusana_jo_lisatty(hakusana): #Kirjainkoolla merkitystä?
                        self._konsoli_io.tulosta("\nHakusana on jo annettu.\n",
                                                Varit.PUNAINEN, lopetus="")
                        continue

                    self.reference_manager.lisaa_hakusana(hakusana)

                if len(self.reference_manager.get_hakusanat()) == 0:
                    self._konsoli_io.tulosta("\nHakusanoja ei annettu. Haku epäonnistui.",
                                                Varit.PUNAINEN, lopetus="")
                    continue

                hakutuloslista = self.reference_manager.hae_hakusanoilla_kun_operandi_and() #Nyt vain yksi operandi 'AND'
            
                if len(hakutuloslista) > 0:
                    self._konsoli_io.tulosta("\nHakusanojen syöttö lopetettu.\n",
                                                Varit.VIHREA, lopetus="")
                    self._tulosta_kaytetyt_hakusanat_ja_operandit(self.reference_manager.get_hakusanat(), "and")
                    self._konsoli_io.tulosta("")
                    self.listaa_viitteet(hakutuloslista)
                else:
                    self._konsoli_io.tulosta("\nHakutuloksia annetuilla hakusanoilla ei löytynyt!",
                                                Varit.PUNAINEN, lopetus="")

                self.reference_manager.tyhjenna_hakusanat()

            elif komento == "5":

                luettu_viite = self.lue_doi()
                if not self.reference_manager.lisaa_uusi_viite(luettu_viite):
                    self._konsoli_io.tulosta("Viite on jo listalla!", Varit.PUNAINEN)
                else:
                    self._konsoli_io.tulosta("Uusi artikkeliviite on lisätty!", Varit.VIHREA)


            elif komento == "6":
                while(True):
                    if len(self.reference_manager.get_filtterit()) > 0:
                        self._tulosta_filtterit_ja_operandit(self.reference_manager.get_filtterit(), "and")

                    filtteri = self._pyyda_syote("\nLisää filtteri [tyhjä lopettaa]:", None, InputValidation.hakusana) #Lisää InputValidation.filtteri

                    if filtteri == "":
                        #Tulosta: filttereitä ei annettu?
                        break

                    if self.reference_manager.filtteri_jo_lisatty(filtteri): #Kirjainkoolla merkitystä?
                        self._konsoli_io.tulosta("\nFiltteri on jo lisätty.\n",
                                                Varit.PUNAINEN, lopetus="")
                        continue

                    self.reference_manager.lisaa_filtteri(filtteri)

                self._konsoli_io.tulosta("\nFilttereiden syöttö lopetettu.\n",
                                            Varit.VIHREA, lopetus="")
            elif komento == "7":
                self.reference_manager.poista_filtterit()
                self._konsoli_io.tulosta("\nFiltterit poistettu!\n",
                                            Varit.VIHREA, lopetus="")
            
            elif komento == "8":
                self.tarkastele_viitetta()

            elif komento == "9":
                break
    
    def _tulosta_menu_ohje(self):
        komennot = {
            "0": "Luo uusi lähdeviite",
            "1": "Listaa kaikki lähdeviitteet",
            "2": "Vie lähdeviitteet bibtex-tiedostoon",
            "3": "Poista lähdeviite",
            "4": "Hae hakusanalla",
            "5": "Hae viite DOI:n perusteella",
            "6": "Lisää filttereitä",
            "7": "Poista filtterit",
            "8": "Hae viitteen kaikki tiedot",
            "9": "Lopeta ohjelma"

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
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)
    #
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
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)

    """ Ei käytössä:
    def _tulosta_operandi_ohje(self):
        komennot = {
            "0": "AND",
            "1": "OR",
            #"x": "Palaa takaisin"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)
    """

    #Refaktoroi _tulosta_kaytetyt_hakusanat_ja_operandit() kanssa:
    def _tulosta_hakusanat_ja_operandit(self, hakusanat, operandi):
        hakusanat_string = "\nKäytetyt hakusanat: '" + hakusanat[0] +"'"

        for i in range(len(hakusanat)-1):
            hakusanat_string += " " + operandi + " '" + hakusanat[i+1] + "'"
        
        self._konsoli_io.tulosta(hakusanat_string, Varit.VIHREA)

    def _tulosta_kaytetyt_hakusanat_ja_operandit(self, hakusanat, operandi):
        hakusanat_string = "\nHakutulokset hakusanoilla: '" + hakusanat[0] +"'"

        for i in range(len(hakusanat)-1):
            hakusanat_string += " " + operandi + " '" + hakusanat[i+1] + "'"
        
        hakusanat_string += ":"

        self._konsoli_io.tulosta(hakusanat_string, Varit.VIHREA)

    def _tulosta_filtterit_ja_operandit(self, filtterit, operandi):
        filtterit_string = "\nKäytössä filtterit: '" + filtterit[0] +"'"

        for i in range(len(filtterit)-1):
            filtterit_string += " " + operandi + " '" + filtterit[i+1] + "'"
        
        filtterit_string += ":"

        self._konsoli_io.tulosta(filtterit_string, Varit.VIHREA)

    def lue_kirja(self):
        author = self.lue_nimet()
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
        author = self.lue_nimet()
        title = self._pyyda_syote("Otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        publisher = self._pyyda_syote("Julkaisija:", 13, None, "julkaisija")
        year = self._pyyda_syote("Vuosi:", 13,
                                                InputValidation.year, "vuosi")
        journal = self._pyyda_syote("Lehti:", 13,
                                                InputValidation.not_empty, "lehti")
        volume = self._pyyda_syote("Vuosikerta:", 13,
                                                InputValidation.not_empty, "vuosikerta")
        number = self._pyyda_syote("Numero:", 13,
                                                InputValidation.article_number, "numero")
        pages = self._pyyda_syote("Sivut:", 13,
                                                InputValidation.pages, "sivut")

        viite = Article(author, title, publisher, year, journal, volume, number,pages)
        return viite

    def lue_kongerenssiviite(self):
        author = self.lue_nimet()
        title = self._pyyda_syote("Otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        publisher = self._pyyda_syote("Julkaisija:", 13, None, "julkaisija")
        year = self._pyyda_syote("Vuosi:", 13,
                                                InputValidation.year, "vuosi")
        booktitle = self._pyyda_syote("Kirjan otsikko:", 13,
                                                InputValidation.not_empty, "otsikko")
        pages = pages = self._pyyda_syote("Sivut:", 13,
                                                InputValidation.pages, "sivut")

        viite = InProceedings(author, title, publisher, year, booktitle, pages)
        return viite
    
    def lue_nimet(self):
        nimilista = []
        self._konsoli_io.tulosta("Syöta tekijät yksi kerrallaan muodossa Sukunimi, Etunimi. Tyhjä syöte lopettaa.\n",
                                         Varit.KELTAINEN)
        while True:
            author = self._pyyda_syote("Kirjoittaja:", 13,
                                        InputValidation.name, "nimi")
            if author == "":
                break
            nimilista.append(author)
        if not len(nimilista):
            self._konsoli_io.tulosta("Viitteella on oltava vähintään yksi kirjoittaja!",
                                         Varit.PUNAINEN)
            self.lue_nimet()
        else:
            return ' '.join(nimi+';' for nimi in nimilista)

    def lue_doi(self):
        doi = self._pyyda_syote("Anna haettava DOI:", None, InputValidation.doi)
        doi_viite = self.reference_manager.hae_viite_doi(doi)
        if doi_viite is not None:
            self._konsoli_io.tulosta("Viite löytyi.")
            viite = Article(doi_viite["author"],
                            doi_viite["title"],
                            doi_viite["publisher"],
                            doi_viite["year"],
                            doi_viite["journal"],
                            doi_viite["volume"],
                            doi_viite["number"],
                                "0")
            return viite
        
        self._konsoli_io.tulosta("Viitettä annetulla DOI:lla ei löytynyt.",
                                                Varit.PUNAINEN, lopetus="")

    def _pyyda_syote(self, kehote, kehotteen_pituus, validator, virheilmoitus_tyyppi="tyhja"):
        if kehotteen_pituus is None:
            kehotteen_pituus = len(kehote) + 1

        while True:
            self._konsoli_io.tulosta(f"{kehote:<{kehotteen_pituus}}", Varit.KELTAINEN, lopetus="")
            syote = self._konsoli_io.lue()
            if validator is None or validator(syote):
                return syote
            self._konsoli_io.tulosta(InputValidation.error_message(virheilmoitus_tyyppi), Varit.PUNAINEN)

    def listaa_viitteet(self, viitteet):
        table = PrettyTable(["Nro", "Kirjoittajat", "Otsikko", "Vuosi"], align='l', max_width=40)
        table.set_style(PrettyTableStyle)
        table.align["Nro"] = "c"
        table.add_rows([
            (i, viite.get_author().replace("; ", "\n"), viite.get_title(), viite.get_year())
            for i, viite in enumerate(viitteet)
        ])
        self._konsoli_io.tulosta(str(table))

    def tarkastele_viitetta(self):
        viitteet = self.reference_manager.hae_viitteet()
        self.listaa_viitteet(viitteet)

        def validator(input_string):
            try:
                _ = viitteet[int(input_string)]
                return True
            except (ValueError, IndexError):
                return False

        viitteen_id = self._pyyda_syote("Anna viitteen numero:", None, validator)
        viite = viitteet[int(viitteen_id)]

        kuvaukset = {
            "author": "Kirjoittaja",
            "title": "Otsikko",
            "publisher": "Julkaisija",
            "year": "Vuosi",
            "isbn": "ISBN",
            "ID": "ID",
            "journal": "Lehti",
            "volume": "Vuosikerta",
            "number": "Numero",
            "pages": "Sivut"
        }
        kuvaus_pituus = max(len(kuvaus) for kuvaus in kuvaukset.values()) + 1
        self._konsoli_io.tulosta("")
        for avain, arvo in viite.get_as_dictionary().items():
            if avain in kuvaukset:
                self._konsoli_io.tulosta(
                    f"{kuvaukset[avain]+':' : <{kuvaus_pituus}}",
                    tummennus=True,
                    lopetus=""
                )
                self._konsoli_io.tulosta(" " + arvo, Varit.VIHREA)

    def _tulosta_figlet(self):
        figlet = Figlet(font='small')

        self._konsoli_io.tulosta("\n")
        self._konsoli_io.tulosta(figlet.renderText('BibTeX-viiteohjelma'), Varit.VIHREA)
