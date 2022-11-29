import unittest
from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Kurose, Jim; Ross, Keith ', 'Computer Networking', 'Pearson', 2019)

    def test_set_new_book_title(self):
        self.book.set_title('Computer Networking. A Top-Down Approach.')
        self.assertEqual(self.book._title, 'Computer Networking. A Top-Down Approach.')
    
    def test_id_generated_correctly(self):
        id = self.book.generate_id()
        self.assertEqual(id, 'Kurose2019')
    
    def test_column_printing(self):
        text = self.book.__str__()
        self.assertEqual(text, 'Kurose, Jim; Ross, Keith       Computer Networking                      2019')
