class StubReferenceManager:
    '''Stub-luokka viitteiden hallinnan testeille'''

    def __init__(self):
        self.viitteet = []
        self.filterit = []
        self.hakusanat = []

    def lisaa_uusi_viite(self, viite):
        self.viitteet.append(viite)
        return True

    def lisaa_filtteri(self, viite):
        self.filterit.append(viite)

    def filtteri_jo_lisatty(self, viite):
        return False

    def poista_filtterit(self):
        self.filterit = []

    def hae_viitteet(self):
        return self.viitteet

    def get_filtterit(self):
        return self.filterit

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        pass

    def pois_viite_databasesta(self, viite):
        pass

    def poista_viite_viitteen_numeron_mukaan(self, numero):
        return True
    
    def hae_viite_doi(self, doi):
        pass
