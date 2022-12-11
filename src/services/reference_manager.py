
class ReferenceManager:
    '''
    Viitteiden hallinnointi.
    '''

    def __init__(self, bibtex_service, db_service):
        self.bibtex_service = bibtex_service
        self.db_service = db_service
        self.viitteet = self.hae_viitteet_databasesta()
        self.vie_viitteet_bibtexdb()  # turha?

        self.tallennetut_hakusanat = []
        self.tallennettujen_hakusanojen_operandi = "AND"  # Default yksi operandi
        # self.tallennettujen_hakusanojen_operandit= [] Useita operandeja

        self.tallennetut_filtterit = []

    def get_filtterit(self):
        return self.tallennetut_filtterit

    def filtteri_jo_lisatty(self, filtteri):
        for tallennettu_filtteri in self.tallennetut_filtterit:
            # if tallennettu_hakusana.casefold() == hakusana.casefold():
            if tallennettu_filtteri == filtteri:
                return True
        return False

    def lisaa_filtteri(self, filtteri):
        if self.filtteri_jo_lisatty(filtteri):
            return False
        """
        for tallennettu_hakusana in self.tallennetut_hakusanat:
            if tallennettu_hakusana == hakusana:
                return False
        """
        self.tallennetut_filtterit.append(filtteri)
        return True

    def poista_filtterit(self):
        self.tallennetut_filtterit.clear()

    def hae_filtterihakusanoilla_kun_operandi_and(self):
        return self.hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and(self.viitteet, self.tallennetut_filtterit)

    # Refaktoroi
    # Laajenna avainsana muihin viitetyyppeihin ja viitetekijöihin
    def hae_viitelistasta_hakusanalla(self, viitelista, hakusana):
        lista_viitteista_haetulla_hakusanalla = []
        for viite in viitelista:
            if hakusana.casefold() in viite.get_author().casefold()\
                    or hakusana.casefold() in viite.get_title().casefold()\
                    or hakusana in viite.get_publisher().casefold():
                # or avainsana in viite.get_year() or avainsana in viite.get_isbn():
                lista_viitteista_haetulla_hakusanalla.append(viite)

        return lista_viitteista_haetulla_hakusanalla

    # Refaktoroi
    def hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and(self, viitelista, hakusanalista):
        hakusanojen_match_lista = []
        hakusanojen_match_listasta_poistettavien_lista = []
        ensimmaisen_hakusanan_match_lista = self.hae_viitelistasta_hakusanalla(
            viitelista, hakusanalista[0])

        for i in range(len(ensimmaisen_hakusanan_match_lista)):
            for j in range(len(hakusanalista) - 1):
                # Erittele eri tapaukset eri viitetyypeille ja lisää haut eri viitetekijöille:
                kytkin = False

                if not (hakusanalista[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_author().casefold() or
                        hakusanalista[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_title(
                ).casefold()
                        or hakusanalista[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()):
                    kytkin = True

                if kytkin:
                    hakusanojen_match_listasta_poistettavien_lista.append(
                        ensimmaisen_hakusanan_match_lista[i])

        for ensimmaisen_hakusanan_match in ensimmaisen_hakusanan_match_lista:
            if self.hae_viitteen_indeksi_viitelistassa(ensimmaisen_hakusanan_match, hakusanojen_match_listasta_poistettavien_lista) == -1:
                hakusanojen_match_lista.append(ensimmaisen_hakusanan_match)

        return hakusanojen_match_lista

    def tyhjenna_hakusanat(self):
        self.tallennetut_hakusanat.clear()

    # Refaktoroi hae_viitteen_indeksi_viitteissa(self, uusi_viite) kanssa
    def hae_viitteen_indeksi_viitelistassa(self, uusi_viite, viitelista):
        if uusi_viite.get_entrytype() == "book":
            for i in range(0, len(viitelista)):
                if viitelista[i].get_entrytype() == "book":
                    if viitelista[i].get_author() == uusi_viite.get_author()\
                            and viitelista[i].get_title() == uusi_viite.get_title()\
                            and viitelista[i].get_publisher() == uusi_viite.get_publisher()\
                            and viitelista[i].get_year() == uusi_viite.get_year()\
                            and viitelista[i].get_isbn() == uusi_viite.get_isbn():
                        return i

        elif uusi_viite.get_entrytype() == "article":
            for i in range(0, len(viitelista)):
                if viitelista[i].get_entrytype() == "article":
                    if viitelista[i].get_author() == uusi_viite.get_author()\
                            and viitelista[i].get_title() == uusi_viite.get_title()\
                            and viitelista[i].get_publisher() == uusi_viite.get_publisher()\
                            and viitelista[i].get_year() == uusi_viite.get_year()\
                            and viitelista[i].get_isbn() == uusi_viite.get_isbn()\
                            and viitelista[i].get_volume() == uusi_viite.get_volume()\
                            and viitelista[i].get_number() == uusi_viite.get_number()\
                            and viitelista[i].get_pages() == uusi_viite.get_pages():
                        return i

        elif uusi_viite.get_entrytype() == "inproceedings":
            for i in range(0, len(viitelista)):
                if viitelista[i].get_entrytype() == "inproceedings":
                    if viitelista[i].get_author() == uusi_viite.get_author()\
                            and viitelista[i].get_title() == uusi_viite.get_title()\
                            and viitelista[i].get_publisher() == uusi_viite.get_publisher()\
                            and viitelista[i].get_year() == uusi_viite.get_year()\
                            and viitelista[i].get_booktitle() == uusi_viite.get_booktitle()\
                            and viitelista[i].get_pages() == uusi_viite.get_pages():
                        return i

        return -1

    # Hakusanat parempi parametrina / ei oliomuuttujana?
    def hae_hakusanoilla_kun_operandi_and(self):
        hakusanojen_match_lista = []
        hakusanojen_match_listasta_poistettavien_lista = []
        ensimmaisen_hakusanan_match_lista = self.hae_viitteista_hakusanalla(
            self.tallennetut_hakusanat[0])

        for i in range(len(ensimmaisen_hakusanan_match_lista)):
            for j in range(len(self.tallennetut_hakusanat) - 1):
                # Erittele eri tapaukset eri viitetyypeille ja lisää haut eri viitetekijöille:
                kytkin = False

                if not (self.tallennetut_hakusanat[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_author(
                ).casefold()
                        or self.tallennetut_hakusanat[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_title(
                ).casefold()
                        or self.tallennetut_hakusanat[j+1].casefold() in
                        ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()):
                    kytkin = True

                if kytkin:
                    hakusanojen_match_listasta_poistettavien_lista.append(
                        ensimmaisen_hakusanan_match_lista[i])

        for ensimmaisen_hakusanan_match in ensimmaisen_hakusanan_match_lista:
            if self.hae_viitteen_indeksi_viitelistassa(ensimmaisen_hakusanan_match, hakusanojen_match_listasta_poistettavien_lista) == -1:
                hakusanojen_match_lista.append(ensimmaisen_hakusanan_match)

        return hakusanojen_match_lista

    # Laajenna avainsana muihin viitetyyppeihin ja viitetekijöihin
    def hae_viitteista_hakusanalla(self, hakusana):
        lista_viitteista_haetulla_hakusanalla = []
        for viite in self.viitteet:
            if hakusana.casefold() in viite.get_author().casefold()\
                    or hakusana.casefold() in viite.get_title().casefold()\
                    or hakusana in viite.get_publisher().casefold():
                # or avainsana in viite.get_year() or avainsana in viite.get_isbn():
                lista_viitteista_haetulla_hakusanalla.append(viite)

        return lista_viitteista_haetulla_hakusanalla

    """ USEITA OPERANDEJA, Ei käytössä:
    def get_tallennettujen_hakusanojen_operandit(self):
        return self.tallennettujen_hakusanojen_operandit

    def lisaa_operandi(self, operandi):
        self.tallennettujen_hakusanojen_operandit.append(operandi)
    """
    # Yksi operandi

    def lisaa_operandi(self, operandi):
        self.tallennettujen_hakusanojen_operandi.append(operandi)

    def get_operandi(self):
        self.tallennettujen_hakusanojen_operandi

    def get_hakusanat(self):
        return self.tallennetut_hakusanat

    def hakusana_jo_lisatty(self, hakusana):
        for tallennettu_hakusana in self.tallennetut_hakusanat:
            # if tallennettu_hakusana.casefold() == hakusana.casefold():
            if tallennettu_hakusana == hakusana:
                return True
        return False

    def lisaa_hakusana(self, hakusana):
        if self.hakusana_jo_lisatty(hakusana):
            return False
        """
        for tallennettu_hakusana in self.tallennetut_hakusanat:
            if tallennettu_hakusana == hakusana:
                return False
        """
        self.tallennetut_hakusanat.append(hakusana)
        return True

    def poista_hakusana(self, hakusana):
        if self.hakusana_jo_lisatty(hakusana):
            self.tallennetut_hakusanat.remove(hakusana)
            return True
        """
        for tallennettu_hakusana in self.tallennetut_hakusanat:
            if tallennettu_hakusana == hakusana:
                # self.tallennetut_hakusanat.remove(hakusana)
                self.tallennetut_hakusanat.remove(tallennettu_hakusana)
                return True
        """
        return False

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

    def vie_viitteet_bibtexdb(self):  # turha?
        for viite in self.viitteet:
            self.vie_viite_bibtexdb(viite)

    def vie_viite_bibtexdb(self, viite):  # turha?
        viite_as_dictionary = viite.get_as_dictionary()
        self.bibtex_service.vie_viite_databaseen(viite_as_dictionary)

    # Refaktoroi
    def tarkista_book_oikea(self, viite, uusi_viite):
        if (
            viite.get_author() == uusi_viite.get_author()
            and viite.get_title() == uusi_viite.get_title()
            and viite.get_publisher() == uusi_viite.get_publisher()
            and viite.get_year() == uusi_viite.get_year()
            and viite.get_isbn() == uusi_viite.get_isbn()
        ):
            return True
        return False

    def tarkista_inproceeding_oikea(self, viite, uusi_viite):
        if (viite.get_author() == uusi_viite.get_author()
            and viite.get_title() == uusi_viite.get_title()
            and viite.get_publisher() == uusi_viite.get_publisher()
            and viite.get_year() == uusi_viite.get_year()
            and viite.get_booktitle() == uusi_viite.get_booktitle()
                and viite.get_pages() == uusi_viite.get_pages()):
            return True
        return False

    def tarkista_article_oikea(self, viite, uusi_viite):
        if (
            viite.get_author() == uusi_viite.get_author()
            and viite.get_title() == uusi_viite.get_title()
            and viite.get_publisher() == uusi_viite.get_publisher()
            and viite.get_year() == uusi_viite.get_year()
            and viite.get_isbn() == uusi_viite.get_isbn()
            and viite.get_volume() == uusi_viite.get_volume()
            and viite.get_number() == uusi_viite.get_number()
            and viite.get_pages() == uusi_viite.get_pages()
        ):
            return True
        return False

    def hae_viitteen_indeksi_viitteissa(self, uusi_viite):
        if uusi_viite.get_entrytype() == "book":
            for viite_indeksi, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "book" and self.tarkista_book_oikea(viite, uusi_viite):
                    return viite_indeksi

        elif uusi_viite.get_entrytype() == "article":
            for viite_indeksi, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "article" and self.tarkista_article_oikea(viite, uusi_viite):
                    return viite_indeksi

        elif uusi_viite.get_entrytype() == "inproceedings":
            for viite_indeksi, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "inproceedings" and self.tarkista_inproceeding_oikea(viite, uusi_viite):
                    return viite_indeksi
                    
    """
    def hae_viitteista_kirjoittajalla(self, kirjoittaja):
        lista_viitteista_haetulla_kirjoittajalla = []

        for viite in self.viitteet:
            if viite.get_author()== kirjoittaja:
                lista_viitteista_haetulla_kirjoittajalla.append(viite)

        return lista_viitteista_haetulla_kirjoittajalla

    def hae_viitteista_otsikolla(self, otsikko):
        lista_viitteista_haetulla_otsikolla = []

        for viite in self.viitteet:
            if viite.get_title().lower() == otsikko.lower():
                lista_viitteista_haetulla_otsikolla.append(viite)

        return lista_viitteista_haetulla_otsikolla

    def hae_viitteista_julkaisijalla(self, julkaisija):
        lista_viitteista_haetulla_julkaisijalla = []

        for viite in self.viitteet:
            if viite.get_publisher().lower() in julkaisija.lower():
                lista_viitteista_haetulla_julkaisijalla.append(viite)

        return lista_viitteista_haetulla_julkaisijalla

    def hae_viitteista_vuosiluvulla(self, vuosiluku):
        lista_viitteista_haetulla_vuosiluvulla = []

        for viite in self.viitteet:
            if viite.get_year() == vuosiluku:
                lista_viitteista_haetulla_vuosiluvulla.append(viite)

        return lista_viitteista_haetulla_vuosiluvulla

    # Johtaa virheeseen muilla kuin kirjoilla?
    def hae_viitteista_isbnlla(self, isbn):
        lista_viitteista_haetulla_isbnlla = []

        for viite in self.viitteet:
            if viite.get_isbn() == isbn:
                # return viite
                lista_viitteista_haetulla_isbnlla.append(viite)

        return lista_viitteista_haetulla_isbnlla
    """

    # Laajenna avainsana muihin viitetyyppeihin ja viitetekijöihin
    # Turha pois?
    def hae_viitteista_avainsanalla(self, avainsana):
        lista_viitteista_haetulla_avainsanalla = []
        for viite in self.viitteet:
            # Toteutus ok?
            if avainsana.lower() in viite.get_author().lower()\
                    or avainsana.lower() in viite.get_title().lower()\
                    or avainsana.lower() in viite.get_publisher().lower()\
                    or avainsana in viite.get_year():
                # or avainsana in viite.get_year() or avainsana in viite.get_isbn():
                lista_viitteista_haetulla_avainsanalla.append(viite)

        return lista_viitteista_haetulla_avainsanalla

    # Seuraavat kaksi viitteiden poisto-ominaisuutta kaipaavat hiomista/toteutusta:
    def poista_viite_databasesta(self, viite):
        viitteen_indeksi = self.hae_viitteen_indeksi_viitteissa(viite)

        if viitteen_indeksi != -1:
            self.viitteet.pop(viitteen_indeksi)
            self.db_service.poista_viite_databasesta(
                viite)  # Lisää toiminnallisuus

            # TOTEUTA TOIMINNALLISUUS: self.bibtex_service.poista_viite(viite)
            # tai tyhjennä bibtexdb ja vie uudestaan kaikki

            return True  # Oikean db-toiminnallisuuden varmistamisen toteuttaminen?

        return False

    def poista_viite_viitteen_numeron_mukaan(self, viitteen_numero):
        if viitteen_numero < len(self.viitteet):  # Tsekattu validation?
            """
            poistettava_viite = self.viitteet.pop(viitteen_numero)
            # self.db_service.poista_viite_databasesta(poistettava_viite)
            """
            # ROBUST toteutus:
            self.viitteet.pop(viitteen_numero)

            self.db_service.poista_viitetaulu_databasesta()
            self.db_service.luo_uusi_viitetaulu()

            for viite in self.viitteet:
                self.db_service.vie_viite_databaseen(viite)

            # TOTEUTA TOIMINNALLISUUS: self.bibtex_service.poista_viite(viite)
            #  tai tyhjennä bibtexdb ja vie uudestaan kaikki
            self.bibtex_service.tyhjenna_bibdatabase()

            for viite in self.viitteet:
                self.vie_viite_bibtexdb(viite)

            return True  # Oikean db-toiminnallisuuden varmistamisen toteuttaminen?

        return False
    """
    def pois_viite_databasesta(self, viite):
        self.db_service.pois_viite_databasesta(viite)
        self.viitteet.remove(viite)
    """

    def hae_viite_doi(self, doi):
        viite = self.bibtex_service.hae_bibtex_doilla(doi)

        return viite
