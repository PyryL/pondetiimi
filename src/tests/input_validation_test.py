import unittest
from services.input_validation import InputValidation

class TestInputValidation(unittest.TestCase):
    '''Testit käyttäjän syötteen validioinnille'''

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

    def test_isbn_epakelvolla_merkilla(self):
        # merkki X ei ole numero
        self.assertFalse(InputValidation.isbn("978-0-5X6-52068-7"))

    def test_vuosi_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.year("1985"))

    def test_vuosi_liian_pienella_maaralla_numeroilla(self):
        self.assertFalse(InputValidation.year("198"))

    def test_vuosi_liian_suurella_maaralla_numeroilla(self):
        self.assertFalse(InputValidation.year("19850"))

    def test_vuosi_ylimaaraisella_osalla(self):
        self.assertFalse(InputValidation.year("1985 abc"))

    def test_menu_komento_kelvolla_yksinumeroisella_syotteella(self):
        for i in range(1,5):
            self.assertTrue(InputValidation.menu_command(str(i)))

    def test_menu_komento_liian_suurella_numerolla(self):
        self.assertFalse(InputValidation.menu_command("10"))

    def test_ei_tyhja_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.not_empty("ei tyhjä"))

    def test_ei_tyhja_epakelvolla_syotteella(self):
        self.assertFalse(InputValidation.not_empty(""))

    def test_nimi_oikealla_muodolla(self):
        self.assertTrue(InputValidation.name("Dijkstra, Edsger"))

    def test_tyhja_nimi(self):
        self.assertTrue(InputValidation.name(""))

    def test_useita_nimia_oikealla_muodolla(self):
        self.assertTrue(InputValidation.name("Dijkstra, Edsger; Knuth, Donald"))

    def test_nimi_epakelvolla_muodolla(self):
        self.assertFalse(InputValidation.name("Dijkstra Edsger"))

    def test_palaute_epakelvolla_nimisyotteella(self):
        self.assertEqual(InputValidation.error_message("nimi"),
                        "Syötteen on oltava muotoa 'Sukunimi, Etunimi; Sukunimi, Etunimi...'")

    def test_palaute_epakelvolla_vuosisyotteella(self):
        self.assertEqual(InputValidation.error_message("vuosi"),
                        "Vuoden on oltava muotoa 'YYYY'.")

    def test_palaute_epakelvolla_isbnsyotteella(self):
        self.assertEqual(InputValidation.error_message("isbn"),
                        "ISBN on oltava muotoa 'XXXXXXXXXXXXXXXX' tai tyhjä.")

    def test_tyhja_isbn_syote(self):
        self.assertTrue(InputValidation.isbn(""))

    def test_viitetyyppi_command_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.viitetyyppi_command("2"))

    def test_viitetyyppi_command_epakelvolla_syotteella(self):
        self.assertFalse(InputValidation.viitetyyppi_command("3"))

    def test_article_number_tyhjalla_syotteella(self):
        self.assertTrue(InputValidation.article_number(""))

    def test_article_number_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.article_number("15"))

    def test_article_number_epakelvolla_syotteella(self):
        self.assertFalse(InputValidation.article_number("1.0"))

    def test_pages_tyhjalla_syotteella(self):
        self.assertTrue(InputValidation.pages(""))

    def test_pages_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.pages("17-18"))

    def test_pages_epakelvon_muotoisella_syotteella(self):
        # syöte ei sisällä väliviivaa
        self.assertFalse(InputValidation.pages("125"))

    def test_pages_epakelvon_sisaltoisella_syotteella(self):
        # luvut eivät ole suuruusjärjestyksessä
        self.assertFalse(InputValidation.pages("18-17"))

    def test_doi_kelvolla_syotteella(self):
        self.assertTrue(InputValidation.doi("10.1000/182"))

    def test_doi_epakelvolla_syotteella(self):
        self.assertFalse(InputValidation.doi("https://doi.org/10.1000/182"))

    def test_palaute_epakelvolla_otsikkosyotteella(self):
        self.assertEqual(InputValidation.error_message("otsikko"),
                        "Otsikko ei voi olla tyhjä.")

    def test_palaute_epakelvolla_julkaisijasyotteella(self):
        self.assertEqual(InputValidation.error_message("julkaisija"),
                        "Julkaisija ei voi olla tyhjä.")

    def test_palaute_epakelvolla_tuntemattomalla_syotteella(self):
        self.assertEqual(InputValidation.error_message(), "Virheellinen syöte.")

    def test_korjaa_doi_nimi_korjaa_nimien_jarjestyksen(self):
        self.assertEqual(InputValidation.korjaa_doi_nimi(30, "Edsger Dijkstra"), "Dijkstra, Edsger")

    def test_korjaa_doi_nimi_korjaa_nimien_jarjestyksen_usealla_nimella(self):
        self.assertEqual(InputValidation.korjaa_doi_nimi(30, "Edsger Dijkstra and Donald Knuth"),
                        "Dijkstra, Edsger; Knuth, Donald")

    def test_korjaa_doi_nimi_korjaa_toisen_etunimen(self):
        result = InputValidation.korjaa_doi_nimi(30, "Edsger Wybe Dijkstra")
        self.assertEqual(result, "Dijkstra, Edsger Wybe")
