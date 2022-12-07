import unittest
import os
from entities.inproceedings import InProceedings
from services.reference_manager import ReferenceManager
from services.bibtex_service import BibtexService
from services.sqldb_service import SqldbService

class TestInProceedings(unittest.TestCase):
    def setUp(self):
        self.inproceedings = InProceedings('Author, First; Author, Second',
                        'Test Article', 'Pearson', 2022, 'Test Booktitle', '12-15')
        self.bibtex_service = BibtexService()
        self.db_service = SqldbService()
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)

    def test_set_new_booktitle_with_empty_value_not_change_journal(self):
        self.inproceedings.set_booktitle('')
        self.assertEqual(self.inproceedings.get_booktitle(), 'Test Booktitle')
    
    def test_set_new_booktitle(self):
        self.inproceedings.set_booktitle('Booktitle')
        self.assertEqual(self.inproceedings.get_booktitle(), 'Booktitle')
    
    def test_get_volume_number_pages_values(self):
        self.assertEqual(self.inproceedings.get_pages(), '12-15')

    def test_command_vie_creates_bib_file(self):
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        self.assertTrue(os.path.exists('viitteet_test.bib'))
        os.remove('viitteet_test.bib')

    def test_exported_bib_file_contains_inproceedings(self):
        self.reference_manager.lisaa_uusi_viite(self.inproceedings)
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        with open('viitteet_test.bib', 'r', encoding='utf-8') as file:
            text = file.read()
            self.assertIn('author = {Author,', text)
        os.remove('viitteet_test.bib')
