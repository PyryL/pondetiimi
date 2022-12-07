from pyfiglet import Figlet
from entities.reference import Reference
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
                """ Toiminnallisuuden toteutus loppuun:
                self._tulosta_ohje_eri_viitetyyppien_lisaykselle()
                lisattavan_viitetyypin_numero = self._pyyda_syote("Anna komento:", None, InputValidation.hakumenu_command)
                ...
                """

                luettu_viite = self.lue_viite()

                # Toteutus ok?
                if not self.reference_manager.lisaa_uusi_viite(luettu_viite):
                    self._konsoli_io.tulosta("Viite on jo listalla!", Varit.PUNAINEN)
                else:
                    self._konsoli_io.tulosta("Uusi viite lisätty!", Varit.VIHREA)
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
                    ("Anna poistettavan lähdeviitteen numero:", None, InputValidation.not_empty)) #Korjaa inputvalidation
                
                if self.reference_manager.poista_viite_viitteen_numeron_mukaan(poistettavan_lahdeviitteen_numero):
                    self._konsoli_io.tulosta("Viite poistettu!", Varit.VIHREA, lopetus="")
                else:
                    self._konsoli_io.tulosta("Viitettä annetulla viitteen numerolla ei ole. Viitteen poisto epäonnistui.", Varit.PUNAINEN, lopetus="") #Validointi varmistaa viitteen numeron ja tulostaa virheen?
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
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")
                if hakukomento == "1":
                    otsikko = self._pyyda_syote("Anna haettava otsikko:", None, InputValidation.not_empty)
                    lista_viitteista_haetulla_otsikolla = self.reference_manager.hae_viitteista_otsikolla(otsikko)
                    if len(lista_viitteista_haetulla_otsikolla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_otsikolla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")               
                if hakukomento == "2":
                    julkaisija = self._pyyda_syote("Anna haettava julkaisija:", None, InputValidation.not_empty)
                    lista_viitteista_haetulla_julkaisijalla = self.reference_manager.hae_viitteista_julkaisijalla(julkaisija)
                    if len(lista_viitteista_haetulla_julkaisijalla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_julkaisijalla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")              
                if hakukomento == "3":
                    vuosiluku = self._pyyda_syote("Anna haettava vuosiluku:", None, InputValidation.year)
                    lista_viitteista_haetulla_vuosiluvulla = self.reference_manager.hae_viitteista_vuosiluvulla(vuosiluku)
                    if len(lista_viitteista_haetulla_vuosiluvulla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_vuosiluvulla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")               
                if hakukomento == "4":
                    isbn = self._pyyda_syote("Anna haettava isbn:", None, InputValidation.isbn)
                    lista_viitteista_haetulla_isbnlla = self.reference_manager.hae_viitteista_isbnlla(isbn)
                    if len(lista_viitteista_haetulla_isbnlla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_isbnlla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")               
                if hakukomento == "5":
                    avainsana = self._pyyda_syote("Anna haettava avainsana:", None, InputValidation.not_empty)
                    lista_viitteista_haetulla_avainsanalla = self.reference_manager.hae_viitteista_avainsanalla(avainsana)
                    if len(lista_viitteista_haetulla_avainsanalla) > 0:
                        self.listaa_viitteet(lista_viitteista_haetulla_avainsanalla)
                    else:
                        self._konsoli_io.tulosta("Viitteitä annetulla hakusanalla ei löytynyt.", Varit.PUNAINEN, lopetus="")                               
                if hakukomento == "x":
                    continue
            elif komento == "5":
                break

    def _tulosta_menu_ohje(self):
        komennot = {
            "0": "Luo uusi lähdeviite",
            "1": "Listaa kaikki lähdeviitteet",
            "2": "Vie lähdeviitteet bibtex-tiedostoon",
            "3": "Poista lähdeviite",
            "4": "Hae hakusanalla",
            "5": "Lopeta ohjelma"
        }
        self._konsoli_io.tulosta("")
        for komento, selite in komennot.items():
            self._konsoli_io.tulosta(" ", lopetus="")
            self._konsoli_io.tulosta(komento, Varit.SININEN, tummennus=True, lopetus="")
            self._konsoli_io.tulosta(" " + selite)
    """
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
    """
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
            self._konsoli_io.tulosta(f"{kehote:<{kehotteen_pituus}}", Varit.KELTAINEN, lopetus="")
            syote = self._konsoli_io.lue("")
            if validator(syote):
                return syote
            self._konsoli_io.tulosta("Virheellinen syöte, yritä uudelleen.", Varit.PUNAINEN)

    def listaa_viitteet(self, viitteet):
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
        #
        self._konsoli_io.tulosta("\n")

        self._konsoli_io.tulosta(f.renderText('BibTeX-viiteohjelma'), Varit.VIHREA)
