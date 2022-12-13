import unittest
from unittest.mock import Mock
from services.reference_manager import ReferenceManager
from entities.reference import Reference

class TestReferenceManager(unittest.TestCase):
    '''Viitteitä hallinnoivan luokan testit'''

    def setUp(self):
        self.bibtex_service = Mock()
        self.db_service = Mock()
        self.db_service.hae_viitteet_databasesta.return_value = []
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)
        self.viite = Reference(
            "John Doe",
            "Title of the book",
            "Best sellers Inc",
            2012
        )

    def test_alussa_entiset_viitteet_haettu_databasesta(self):
        self.db_service.hae_viitteet_databasesta.assert_called_once()
        self.assertEqual(len(self.reference_manager.hae_viitteet()), 0)

    def test_uuden_viitteen_lisays_vie_databaseen(self):
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.db_service.vie_viite_databaseen.assert_called_once()

    def test_uuden_viitteen_lisays_tallentuu_manageriin(self):
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.assertEqual(len(self.reference_manager.viitteet), 1)

    def test_uuden_viitteen_lisays_vie_bibtex_serviceen(self):
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.bibtex_service.vie_viite_databaseen.assert_called_once()
