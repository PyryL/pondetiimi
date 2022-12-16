import unittest
import os
from entities.article import Article
from services.reference_manager import ReferenceManager
from services.bibtex_service import BibtexService
from services.sqldb_service import SqldbService

class TestArticle(unittest.TestCase):
    '''Artikkeli-tyyppisen viitteen testit'''

    def setUp(self):
        self.article = Article('Author, First; Author, Second',
                        'Test Article', 'Pearson', 2022, 'Test Journal', '2', '5', '12-15')
        self.bibtex_service = BibtexService()
        #self.db_service = SqldbService()
        self.db_service = SqldbService("test.db")
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)

    def test_set_new_journal_with_empty_value_not_change_journal(self):
        self.article.set_journal('')
        self.assertEqual(self.article.get_journal(), 'Test Journal')

    def test_set_new_journal_(self):
        self.article.set_journal('Journal')
        self.assertEqual(self.article.get_journal(), 'Journal')

    def test_get_volume_number_pages_values(self):
        self.assertEqual(self.article.get_volume(), '2')
        self.assertEqual(self.article.get_number(), '5')
        self.assertEqual(self.article.get_pages(), '12-15')

    def test_command_vie_creates_bib_file(self):
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        self.assertTrue(os.path.exists('viitteet_test.bib'))
        os.remove('viitteet_test.bib')

    def test_exported_bib_file_contains_article(self):
        self.reference_manager.lisaa_uusi_viite(self.article)
        self.reference_manager.vie_viitteet_tiedostoon('viitteet_test')
        with open('viitteet_test.bib', 'r', encoding='utf-8') as file:
            text = file.read()
            self.assertIn('author = {Author,', text)
        os.remove('viitteet_test.bib')
