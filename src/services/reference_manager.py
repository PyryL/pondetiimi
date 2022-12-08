
class ReferenceManager:
    '''
    Viitteiden hallinnointi.
    '''
    def __init__(self, bibtex_service, db_service):
        self.bibtex_service = bibtex_service
        self.db_service = db_service
        self.viitteet = self.hae_viitteet_databasesta()
        self.vie_viitteet_bibtexdb() #turha?

    def lisaa_uusi_viite(self, viite):
        if self.hae_loytyyko_viitteista(viite):
            return False
        self.vie_viite_databaseen(viite)
        self.viitteet.append(viite)
        self.vie_viite_bibtexdb(viite)
        return True

    def hae_loytyyko_viitteista(self, viite):
        return self.hae_viitteen_indeksi_viitteissa(viite) != -1

    def hae_viitteet_databasesta(self):
        return self.db_service.hae_viitteet_databasesta()

    def vie_viite_databaseen(self, viite):
        self.db_service.vie_viite_databaseen(viite)

    def hae_viitteet(self):
        return self.viitteet

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.bibtex_service.vie_viitteet_tiedostoon(tiedostonimi)

    def vie_viitteet_bibtexdb(self): #turha?
        for viite in self.viitteet:
            self.vie_viite_bibtexdb(viite)

    def vie_viite_bibtexdb(self, viite): #turha?
        viite_as_dictionary = viite.get_as_dictionary()
        self.bibtex_service.vie_viite_databaseen(viite_as_dictionary)

    # Refaktoroi
    def hae_viitteen_indeksi_viitteissa(self, uusi_viite):
        if uusi_viite.get_entrytype() == "book":
            for i in range(0, len(self.viitteet)):
                if self.viitteet[i].get_entrytype() == "book":
                    if self.viitteet[i].get_author() == uusi_viite.get_author()\
                        and self.viitteet[i].get_title() == uusi_viite.get_title()\
                        and self.viitteet[i].get_publisher() == uusi_viite.get_publisher()\
                        and self.viitteet[i].get_year() == uusi_viite.get_year()\
                        and self.viitteet[i].get_isbn() == uusi_viite.get_isbn():
                        return i

        elif uusi_viite.get_entrytype() == "article":
            for i in range(0, len(self.viitteet)):
                if self.viitteet[i].get_entrytype() == "article":
                    if self.viitteet[i].get_author() == uusi_viite.get_author()\
                        and self.viitteet[i].get_title() == uusi_viite.get_title()\
                        and self.viitteet[i].get_publisher() == uusi_viite.get_publisher()\
                        and self.viitteet[i].get_year() == uusi_viite.get_year()\
                        and self.viitteet[i].get_isbn() == uusi_viite.get_isbn()\
                        and self.viitteet[i].get_volume() == uusi_viite.get_volume()\
                        and self.viitteet[i].get_number() == uusi_viite.get_number()\
                        and self.viitteet[i].get_pages() == uusi_viite.get_pages():
                        return i

        elif uusi_viite.get_entrytype() == "inproceedings":
            for i in range(0, len(self.viitteet)):
                if self.viitteet[i].get_entrytype() == "inproceedings":
                    if self.viitteet[i].get_author() == uusi_viite.get_author()\
                        and self.viitteet[i].get_title() == uusi_viite.get_title()\
                        and self.viitteet[i].get_publisher() == uusi_viite.get_publisher()\
                        and self.viitteet[i].get_year() == uusi_viite.get_year()\
                        and self.viitteet[i].get_booktitle() == uusi_viite.get_booktitle()\
                        and self.viitteet[i].get_pages() == uusi_viite.get_pages():
                        return i

        return -1

    def hae_viitteista_kirjoittajalla(self, kirjoittaja):
        lista_viitteista_haetulla_kirjoittajalla = []

        for viite in self.viitteet:
            if viite.get_author() == kirjoittaja:
                lista_viitteista_haetulla_kirjoittajalla.append(viite)

        return lista_viitteista_haetulla_kirjoittajalla

    def hae_viitteista_otsikolla(self, otsikko):
        lista_viitteista_haetulla_otsikolla = []

        for viite in self.viitteet:
            if viite.get_title() == otsikko:
                lista_viitteista_haetulla_otsikolla.append(viite)

        return lista_viitteista_haetulla_otsikolla

    def hae_viitteista_julkaisijalla(self, julkaisija):
        lista_viitteista_haetulla_julkaisijalla = []

        for viite in self.viitteet:
            if viite.get_publisher() == julkaisija:
                lista_viitteista_haetulla_julkaisijalla.append(viite)

        return lista_viitteista_haetulla_julkaisijalla

    def hae_viitteista_vuosiluvulla(self, vuosiluku):
        lista_viitteista_haetulla_vuosiluvulla = []

        for viite in self.viitteet:
            if viite.get_year() == vuosiluku:
                lista_viitteista_haetulla_vuosiluvulla.append(viite)

        return lista_viitteista_haetulla_vuosiluvulla

    #Johtaa virheeseen muilla kuin kirjoilla?
    def hae_viitteista_isbnlla(self, isbn):
        lista_viitteista_haetulla_isbnlla = []

        for viite in self.viitteet:
            if viite.get_isbn() == isbn:
                #return viite
                lista_viitteista_haetulla_isbnlla.append(viite)

        return lista_viitteista_haetulla_isbnlla

    #Laajenna avainsana muihin viitetyyppeihin ja viitetekijöihin
    def hae_viitteista_avainsanalla(self, avainsana):
        lista_viitteista_haetulla_avainsanalla = []
        for viite in self.viitteet:
            #Toteutus ok?
            if avainsana in viite.get_author() or avainsana in viite.get_title()\
                or avainsana in viite.get_publisher():
                # or avainsana in viite.get_year() or avainsana in viite.get_isbn():
                lista_viitteista_haetulla_avainsanalla.append(viite)

        return lista_viitteista_haetulla_avainsanalla

    # Seuraavat kaksi viitteiden poisto-ominaisuutta kaipaavat hiomista/toteutusta:
    def poista_viite_databasesta(self, viite):
        viitteen_indeksi = self.hae_viitteen_indeksi_viitteissa(viite)

        if viitteen_indeksi != -1:
            self.viitteet.pop(viitteen_indeksi)
            self.db_service.poista_viite_databasesta(viite) #Lisää toiminnallisuus

            #TOTEUTA TOIMINNALLISUUS: self.bibtex_service.poista_viite(viite)
            # tai tyhjennä bibtexdb ja vie uudestaan kaikki

            return True # Oikean db-toiminnallisuuden varmistamisen toteuttaminen?

        return False

    def poista_viite_viitteen_numeron_mukaan(self, viitteen_numero):
        if viitteen_numero < len(self.viitteet):  # Tsekattu validation?
            """
            poistettava_viite = self.viitteet.pop(viitteen_numero)
            #self.db_service.poista_viite_databasesta(poistettava_viite)
            """
            #ROBUST toteutus:
            self.viitteet.pop(viitteen_numero)

            self.db_service.poista_viitetaulu_databasesta()
            self.db_service.luo_uusi_viitetaulu()

            for viite in self.viitteet:
                self.db_service.vie_viite_databaseen(viite)

            #TOTEUTA TOIMINNALLISUUS: self.bibtex_service.poista_viite(viite)
            #  tai tyhjennä bibtexdb ja vie uudestaan kaikki
            self.bibtex_service.tyhjenna_bibdatabase()

            for viite in self.viitteet:
                self.vie_viite_bibtexdb(viite)

            return True # Oikean db-toiminnallisuuden varmistamisen toteuttaminen?

        return False
    """
    def pois_viite_databasesta(self, viite):
        self.db_service.pois_viite_databasesta(viite)
        self.viitteet.remove(viite)
    """

    def hae_viite_doi(self, doi):
        viite = self.bibtex_service.hae_bibtex_doilla(doi)

        return viite