import unittest
from services.input_validation import InputValidation

class TestInputValidation(unittest.TestCase):
    def test_isbn_kelvoilla_syotteilla(self):
        kelvot_syotteet = [
            "978-0-596-52068-7",
            "978 0 596 52068 7",
            "9780596520687",
            "979-3-16-148410-0",
            "3161484100"
        ]
        for syote in kelvot_syotteet:
            self.assertTrue(InputValidation.isbn(syote))

    def test_isbn_epakelvolla_syotteen_alulla(self):
        # alku 977 on epäkelpo
        self.assertFalse(InputValidation.isbn("977-0-596-52068-7"))

    def test_isbn_epakelvolla_syotteen_pituudella(self):
        # numeroiden määrä jokaisessa osassa on kelpo,
        # mutta yhteensä niitä on liian paljon (ei 10 eikä 13)
        self.assertFalse(InputValidation.isbn("978-1234-123456-12345-1"))

    def test_vuosi_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.year("1985"))

    def test_vuosi_liian_pienella_maaralla_numeroilla(self):
        self.assertFalse(InputValidation.year("198"))

    def test_vuosi_liian_suurella_maaralla_numeroilla(self):
        self.assertFalse(InputValidation.year("19850"))

    def test_vuosi_ylimaaraisella_osalla(self):
        self.assertFalse(InputValidation.year("1985 abc"))

    def test_menu_komento_kelvolla_syotteella(self):
        for i in range(5):
            self.assertTrue(InputValidation.menu_command(str(i)))

    def test_menu_komento_liian_suurella_numerolla(self):
        self.assertFalse(InputValidation.menu_command("9"))

    def test_ei_tyhja_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.not_empty("ei tyhjä"))

    def test_ei_tyhja_epakelvolla_syotteella(self):
        self.assertFalse(InputValidation.not_empty(""))

    def test_nimi_oikealla_muodolla(self):
        self.assertTrue(InputValidation.name("Dijkstra, Edsger"))

    def test_useita_nimia_oikealla_muodolla(self):
        self.assertTrue(InputValidation.name("Dijkstra, Edsger; Knuth, Donald"))

    def test_nimi_epakelvolla_muodolla(self):
        self.assertFalse(InputValidation.name("Dijkstra Edsger"))