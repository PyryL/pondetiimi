class StubReferenceManager:
    def __init__(self):
        self.viitteet = []

    def lisaa_uusi_viite(self, viite):
        self.viitteet.append(viite)

    def hae_viitteet(self):
        return self.viitteet

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        pass

    def pois_viite_databasesta(self, viite):
        pass