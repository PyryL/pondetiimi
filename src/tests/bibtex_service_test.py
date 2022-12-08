import unittest
from services.bibtex_service import BibtexService
from entities.reference import Reference

class FileIOStub:
    def __init__(self):
        self.filename = ""
        self.content = ""

    def write(self, filename, content):
        self.filename = filename
        self.content = content

class TestBibtexService(unittest.TestCase):
    def setUp(self):
        self.file_io = FileIOStub()
        self.bibtext_service = BibtexService(self.file_io)
        self.viite = Reference(
            "John Doe åäöüß",       # testaa erikoismerkit
            "Title of the book",
            "Best sellers Inc",
            2012
            ).get_as_dictionary()

    def test_viedyssa_tiedostossa_halutut_rivit(self):
        self.bibtext_service.vie_viite_databaseen(self.viite)
        self.bibtext_service.vie_viitteet_tiedostoon("test_export")
        halutut_rivit = [
            'author = {John Doe {\\r{a}}{\\\"a}{\\\"o}{\\\"u}{\\ss}}',
            "title = {Title of the book}",
            "year = {2012}",
            "publisher = {Best sellers Inc}",
        ]
        for rivi in halutut_rivit:
            self.assertTrue(rivi in self.file_io.content)

    def test_viedyn_tiedoston_nimi_on_haluttu(self):
        self.bibtext_service.vie_viitteet_tiedostoon("test_export")
        self.assertEqual(self.file_io.filename, "test_export.bib")
