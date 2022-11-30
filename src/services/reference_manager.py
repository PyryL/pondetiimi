from services.bibtex_service import BibtexService

class ReferenceManager:
    def __init__(self, bibtex_service, db_service):
        self.bibtex_service = bibtex_service
        self.db_service = db_service
        self.viitteet = self.hae_viitteet_databasesta()
        self.vie_viitteet_bibtexdb() #turha?

    def lisaa_uusi_viite(self, viite):
        # Tarkista, löytyykö jo self.viitteet
        self.vie_viite_databaseen(viite)
        self.viitteet.append(viite)

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
