import unittest
from services.sqldb_service import SqldbService
from entities.article import Article
from entities.book import Book
from entities.inproceedings import InProceedings

class TestSqldbService(unittest.TestCase):
    '''Tietokannan testit'''

    def setUp(self):
        self.db_service = SqldbService("test.db")
        self.db_service.poista_viitetaulu_databasesta()
        self.db_service.luo_uusi_viitetaulu()

        self.kirjaviite = Book(
            "Author",
            "Otsikko",
            "Julkaisija",
            "Vuosi",
            "ISBN"
        )

        self.artikkeliviite = Article(
            "Author",
            "Otsikko",
            "Julkaisija",
            "Vuosi",
            "Lehti",
            "Vuosikerta",
            "Numero",
            "Sivut"
        )

        self.konferenssiviite = InProceedings(
            "Author",
            "Otsikko",
            "Julkaisija",
            "Vuosi",
            "Kirjan otsikko",
            "Sivut"
        )

    def test_vie_kirjaviite_databaseen(self):
        self.db_service.vie_viite_databaseen(self.kirjaviite)
        self.assertEqual(len(self.db_service.hae_viitteet_databasesta()), 1)

    def test_vie_artikkeliviite_databaseen(self):
        self.db_service.vie_viite_databaseen(self.artikkeliviite)
        self.assertEqual(len(self.db_service.hae_viitteet_databasesta()), 1)

    def test_vie_konferenssiviite_databaseen(self):
        self.db_service.vie_viite_databaseen(self.konferenssiviite)
        self.assertEqual(len(self.db_service.hae_viitteet_databasesta()), 1)

    def test_lisaa_ja_hae_kolme_viitetta_databasesta(self):
        self.db_service.vie_viite_databaseen(self.kirjaviite)
        self.db_service.vie_viite_databaseen(self.artikkeliviite)
        self.db_service.vie_viite_databaseen(self.konferenssiviite)
        self.assertEqual(len(self.db_service.hae_viitteet_databasesta()), 3)
