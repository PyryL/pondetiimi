
class ReferenceManager:
    '''
    Viitteiden hallinnointi.
    '''
    def __init__(self, bibtex_service, db_service):
        self.bibtex_service = bibtex_service
        self.db_service = db_service
        self.viitteet = self.hae_viitteet_databasesta()
        self.vie_viitteet_bibtexdb()
        self.tallennetut_hakusanat = []
        self.tallennettujen_hakusanojen_operandi = "AND"
        self.tallennetut_filtterit = []

    def get_filtterit(self):
        return self.tallennetut_filtterit

    def filtteri_jo_lisatty(self, filtteri):
        for tallennettu_filtteri in self.tallennetut_filtterit:
            if tallennettu_filtteri == filtteri:
                return True
        return False

    def lisaa_filtteri(self, filtteri):
        if self.filtteri_jo_lisatty(filtteri):
            return False
        self.tallennetut_filtterit.append(filtteri)
        return True

    def poista_filtterit(self):
        self.tallennetut_filtterit.clear()

    def hae_filtterihakusanoilla_kun_operandi_and(self):
        return self.hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and\
                    (self.viitteet, self.tallennetut_filtterit)


    def hae_viitelistasta_hakusanalla(self, viitelista, hakusana):
        lista_viitteista_haetulla_hakusanalla = []
        for viite in viitelista:

            if viite.get_entrytype() == "book":
                if hakusana.casefold() in viite.get_author().casefold()\
                    or hakusana.casefold() in viite.get_title().casefold()\
                    or hakusana.casefold() in viite.get_publisher().casefold()\
                    or hakusana.casefold() in viite.get_year().casefold()\
                    or hakusana.casefold() in viite.get_isbn().casefold():
                    lista_viitteista_haetulla_hakusanalla.append(viite)

            elif viite.get_entrytype() == "article":
                if hakusana.casefold() in viite.get_author().casefold()\
                    or hakusana.casefold() in viite.get_title().casefold()\
                    or hakusana.casefold() in viite.get_publisher().casefold()\
                    or hakusana.casefold() in viite.get_year().casefold()\
                    or hakusana.casefold() in viite.get_journal().casefold()\
                    or hakusana.casefold() in viite.get_volume().casefold()\
                    or hakusana.casefold() in viite.get_number().casefold()\
                    or hakusana.casefold() in viite.get_pages().casefold():
                    lista_viitteista_haetulla_hakusanalla.append(viite)

            elif viite.get_entrytype() == "inproceedings":
                if hakusana.casefold() in viite.get_author().casefold()\
                    or hakusana.casefold() in viite.get_title().casefold()\
                    or hakusana.casefold() in viite.get_publisher().casefold()\
                    or hakusana.casefold() in viite.get_year().casefold()\
                    or hakusana.casefold() in viite.get_booktitle().casefold()\
                    or hakusana.casefold() in viite.get_pages().casefold():
                    lista_viitteista_haetulla_hakusanalla.append(viite)

        return lista_viitteista_haetulla_hakusanalla


    def hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and\
            (self, viitelista, hakusanalista):
        hakusanojen_match_lista = []
        hakusanojen_match_listasta_poistettavien_lista = []
        ensimmaisen_hakusanan_match_lista = self.hae_viitelistasta_hakusanalla\
                                                (viitelista, hakusanalista[0])

        for i in range(len(ensimmaisen_hakusanan_match_lista)):
            for j in range(len(hakusanalista) - 1):
                kytkin = False

                if ensimmaisen_hakusanan_match_lista[i].get_entrytype() == "book":
                    if not (hakusanalista[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_author().casefold() or\
                        hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_title().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_year().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_isbn().casefold()):

                        kytkin = True

                elif ensimmaisen_hakusanan_match_lista[i].get_entrytype() == "article":
                    if not (hakusanalista[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_author().casefold() or\
                        hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_title().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_year().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_journal().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_volume().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_number().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_pages().casefold()):

                        kytkin = True

                elif ensimmaisen_hakusanan_match_lista[i].get_entrytype() == "inproceedings":
                    if not (hakusanalista[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_author().casefold() or\
                        hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_title().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_year().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_booktitle().casefold()\
                        or hakusanalista[j+1].casefold() in\
                            ensimmaisen_hakusanan_match_lista[i].get_pages().casefold()):

                        kytkin = True

                if kytkin:
                    hakusanojen_match_listasta_poistettavien_lista.append\
                        (ensimmaisen_hakusanan_match_lista[i])

        for ensimmaisen_hakusanan_match in ensimmaisen_hakusanan_match_lista:
            if self.hae_viitteen_indeksi_viitelistassa\
                (ensimmaisen_hakusanan_match, hakusanojen_match_listasta_poistettavien_lista) == -1:
                hakusanojen_match_lista.append(ensimmaisen_hakusanan_match)

        return hakusanojen_match_lista

    def tyhjenna_hakusanat(self):
        self.tallennetut_hakusanat.clear()


    def hae_viitteen_indeksi_viitelistassa(self, uusi_viite, viitelista):
        if uusi_viite.get_entrytype() == "book":
            for i, viite in enumerate(viitelista):
                if viite.get_entrytype() == "book":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_isbn() == uusi_viite.get_isbn():
                        return i

        elif uusi_viite.get_entrytype() == "article":
            for i, viite in enumerate(viitelista):
                if viite.get_entrytype() == "article":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_isbn() == uusi_viite.get_isbn()\
                        and viite.get_volume() == uusi_viite.get_volume()\
                        and viite.get_number() == uusi_viite.get_number()\
                        and viite.get_pages() == uusi_viite.get_pages():
                        return i

        elif uusi_viite.get_entrytype() == "inproceedings":
            for i, viite in enumerate(viitelista):
                if viite.get_entrytype() == "inproceedings":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_booktitle() == uusi_viite.get_booktitle()\
                        and viite.get_pages() == uusi_viite.get_pages():
                        return i

        return -1


    def hae_hakusanoilla_kun_operandi_and(self):
        hakusanojen_match_lista = []
        hakusanojen_match_listasta_poistettavien_lista = []
        ensimmaisen_hakusanan_match_lista = self.hae_viitteista_hakusanalla\
            (self.tallennetut_hakusanat[0])

        for i in range(len(ensimmaisen_hakusanan_match_lista)):
            for j in range(len(self.tallennetut_hakusanat) - 1):

                kytkin = False

                if not (self.tallennetut_hakusanat[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_author().casefold()\
                    or self.tallennetut_hakusanat[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_title().casefold()\
                    or self.tallennetut_hakusanat[j+1].casefold() in\
                        ensimmaisen_hakusanan_match_lista[i].get_publisher().casefold()):
                    kytkin = True

                if kytkin:
                    hakusanojen_match_listasta_poistettavien_lista.append\
                        (ensimmaisen_hakusanan_match_lista[i])

        for ensimmaisen_hakusanan_match in ensimmaisen_hakusanan_match_lista:
            if self.hae_viitteen_indeksi_viitelistassa\
                (ensimmaisen_hakusanan_match, hakusanojen_match_listasta_poistettavien_lista) == -1:
                hakusanojen_match_lista.append(ensimmaisen_hakusanan_match)

        return hakusanojen_match_lista

    def hae_viitteista_hakusanalla(self, hakusana):
        lista_viitteista_haetulla_hakusanalla = []
        for viite in self.viitteet:
            if hakusana.casefold() in viite.get_author().casefold()\
                or hakusana.casefold() in viite.get_title().casefold()\
                or hakusana in viite.get_publisher().casefold()\
                or hakusana in str(viite.get_year()).casefold():
                lista_viitteista_haetulla_hakusanalla.append(viite)

        return lista_viitteista_haetulla_hakusanalla

    """Ei käytössä?
    def lisaa_operandi(self, operandi):
        self.tallennettujen_hakusanojen_operandi.append(operandi)
    """
    def get_operandi(self):
        return self.tallennettujen_hakusanojen_operandi

    def get_hakusanat(self):
        return self.tallennetut_hakusanat

    def hakusana_jo_lisatty(self, hakusana):
        for tallennettu_hakusana in self.tallennetut_hakusanat:

            if tallennettu_hakusana == hakusana:
                return True
        return False

    def lisaa_hakusana(self, hakusana):
        if self.hakusana_jo_lisatty(hakusana):
            return False
        self.tallennetut_hakusanat.append(hakusana)
        return True

    def poista_hakusana(self, hakusana):
        if self.hakusana_jo_lisatty(hakusana):
            self.tallennetut_hakusanat.remove(hakusana)
            return True
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

    # Refaktoroi?
    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.bibtex_service.vie_viitteet_tiedostoon(tiedostonimi)

    def vie_viitelista_tiedostoon(self, viitelista, tiedostonimi):
        for viite in viitelista:
            viite_as_dictionary = viite.get_as_dictionary()
            self.bibtex_service.vie_viite_temporary_databaseen(viite_as_dictionary)

        self.bibtex_service.vie_temporary_databasen_viitelista_tiedostoon(tiedostonimi)

        self.bibtex_service.tyhjenna_temporary_bibdatabase()

    def vie_viitteet_bibtexdb(self):
        for viite in self.viitteet:
            self.vie_viite_bibtexdb(viite)

    def vie_viite_bibtexdb(self, viite):
        viite_as_dictionary = viite.get_as_dictionary()
        self.bibtex_service.vie_viite_databaseen(viite_as_dictionary)

    # Refaktoroi
    def hae_viitteen_indeksi_viitteissa(self, uusi_viite):
        if uusi_viite.get_entrytype() == "book":
            for i, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "book":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_isbn() == uusi_viite.get_isbn():
                        return i

        elif uusi_viite.get_entrytype() == "article":
            for i, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "article":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_isbn() == uusi_viite.get_isbn()\
                        and viite.get_volume() == uusi_viite.get_volume()\
                        and viite.get_number() == uusi_viite.get_number()\
                        and viite.get_pages() == uusi_viite.get_pages():
                        return i

        elif uusi_viite.get_entrytype() == "inproceedings":
            for i, viite in enumerate(self.viitteet):
                if viite.get_entrytype() == "inproceedings":
                    if viite.get_author() == uusi_viite.get_author()\
                        and viite.get_title() == uusi_viite.get_title()\
                        and viite.get_publisher() == uusi_viite.get_publisher()\
                        and viite.get_year() == uusi_viite.get_year()\
                        and viite.get_booktitle() == uusi_viite.get_booktitle()\
                        and viite.get_pages() == uusi_viite.get_pages():
                        return i

        return -1

    def hae_viitteista_avainsanalla(self, avainsana):
        lista_viitteista_haetulla_avainsanalla = []
        for viite in self.viitteet:

            if avainsana.lower() in viite.get_author().lower()\
                or avainsana.lower() in viite.get_title().lower()\
                or avainsana.lower() in viite.get_publisher().lower()\
                or avainsana in viite.get_year():

                lista_viitteista_haetulla_avainsanalla.append(viite)

        return lista_viitteista_haetulla_avainsanalla

    def poista_viite_databasesta(self, viite):
        viitteen_indeksi = self.hae_viitteen_indeksi_viitteissa(viite)

        if viitteen_indeksi != -1:
            self.viitteet.pop(viitteen_indeksi)
            self.db_service.poista_viite_databasesta(viite)

            return True

        return False

    def poista_viite_viitteen_numeron_mukaan(self, viitteen_numero):
        if viitteen_numero < len(self.viitteet):

            self.viitteet.pop(viitteen_numero)

            self.db_service.poista_viitetaulu_databasesta()
            self.db_service.luo_uusi_viitetaulu()

            for viite in self.viitteet:
                self.db_service.vie_viite_databaseen(viite)

            self.bibtex_service.tyhjenna_bibdatabase()

            for viite in self.viitteet:
                self.vie_viite_bibtexdb(viite)

            return True

        return False

    def hae_viite_doi(self, doi):
        viite = self.bibtex_service.hae_bibtex_doilla(doi)

        return viite
