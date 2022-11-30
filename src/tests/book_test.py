import unittest
from entities.book import Book
from services.reference_manager import ReferenceManager
from services.bibtex_service import BibtexService
from services.sqldb_service import SqldbService
import os

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Kurose, Jim; Ross, Keith ', 'Computer Networking', 'Pearson', 2019)
        self.bibtex_service = BibtexService()
        self.db_service = SqldbService()
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)

    def test_set_new_book_title(self):
        self.book.set_title('Computer Networking. A Top-Down Approach.')
        self.assertEqual(self.book._title, 'Computer Networking. A Top-Down Approach.')
    
    def test_id_generated_correctly(self):
        id = self.book.generate_id()
        self.assertEqual(id, 'Kurose2019')
    
    def test_column_printing(self):
        text = self.book.__str__()
        self.assertEqual(text, 'Kurose, Jim; Ross, Keith       Computer Networking                      2019')

    def test_command_vie_creates_bib_file(self):
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        self.assertTrue(os.path.exists('viitteet_test.bib'))
        os.remove('viitteet_test.bib')

    def test_exported_bib_file_contains_book(self):
        self.reference_manager.lisaa_uusi_viite(self.book)
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        with open('viitteet_test.bib', 'r') as f:
            text = f.read()
            self.assertIn('author = {Kurose,', text)
        os.remove('viitteet_test.bib')
