import unittest
import os
from entities.book import Book
from services.reference_manager import ReferenceManager
from services.bibtex_service import BibtexService
from services.sqldb_service import SqldbService

class TestBook(unittest.TestCase):
    '''Kirja-tyyppisen viitteen testit'''

    def setUp(self):
        self.book = Book('Kurose, Jim; Ross, Keith',
                        'Computer Networking', 'Pearson', '2019', '9780596520687')
        self.bibtex_service = BibtexService()
        #self.db_service = SqldbService()
        self.db_service = SqldbService("test.db")
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)

    def test_set_new_book_title(self):
        self.book.set_title('Computer Networking. A Top-Down Approach.')
        self.assertEqual(self.book.get_title(), 'Computer Networking. A Top-Down Approach.')

    def test_command_vie_creates_bib_file(self):
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        self.assertTrue(os.path.exists('viitteet_test.bib'))
        os.remove('viitteet_test.bib')

    def test_exported_bib_file_contains_book(self):
        self.reference_manager.lisaa_uusi_viite(self.book)
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        with open('viitteet_test.bib', 'r', encoding='utf-8') as file:
            text = file.read()
            self.assertIn('author = {Kurose,', text)
        os.remove('viitteet_test.bib')

    def test_after_setting_correct_isbn_book_contains_right_isbn(self):
        self.book.set_isbn("978-1-292-15359-9")
        self.assertEqual(self.book.get_isbn(), "978-1-292-15359-9")

    def test_after_setting_incorrect_isbn_book_isbn_not_changed(self):
        self.book.set_isbn("AAA-B-CCC-X")
        self.assertEqual(self.book.get_isbn(), '9780596520687')

    def test_id_in_correct_form(self):
        self.assertEqual(self.book.get_id(), 'KuroseComputer2019')

    def test_after_setting_author_with_incorrect_value_author_not_changed(self):
        self.book.set_author("Kurose")
        self.assertEqual(self.book.get_author(), 'Kurose, Jim; Ross, Keith')

    def test_after_setting_author_with_correct_value_author_changed(self):
        self.book.set_author('Ross, Keith')
        self.assertEqual(self.book.get_author(), 'Ross, Keith')

    def test_after_setting_year_with_incorrect_value_year_not_changed(self):
        self.book.set_year('12')
        self.assertEqual(self.book.get_year(), '2019')

    def test_after_setting_year_with_correct_value_year_changed(self):
        self.book.set_year('2020')
        self.assertEqual(self.book.get_year(), '2020')

    def test_after_setting_publisher_with_empty_value_publisher_changed(self):
        self.book.set_publisher("")
        self.assertEqual(self.book.get_publisher(), '')

    def test_after_setting_publisher_with_correct_value_publisher_changed(self):
        self.book.set_publisher("Test Pearson")
        self.assertEqual(self.book.get_publisher(), 'Test Pearson')
