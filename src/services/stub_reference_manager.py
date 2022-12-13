class StubReferenceManager:
    '''Stub-luokka viitteiden hallinnan testeille'''

    def __init__(self):
        self.viitteet = []
        self.filterit = []

    def lisaa_uusi_viite(self, viite):
        self.viitteet.append(viite)
        return True

    def hae_viitteet(self):
        return self.viitteet

    def get_filtterit(self):
        return self.filterit

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        pass

    def pois_viite_databasesta(self, viite):
        pass
