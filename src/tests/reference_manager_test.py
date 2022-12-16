import unittest
from unittest.mock import Mock
from services.reference_manager import ReferenceManager
from entities.reference import Reference
from entities.article import Article
from entities.book import Book
from entities.inproceedings import InProceedings

class TestReferenceManager(unittest.TestCase):
    '''Viitteitä hallinnoivan luokan testit'''

    def setUp(self):
        self.bibtex_service = Mock()
        self.db_service = Mock()
        self.db_service.hae_viitteet_databasesta.return_value = []
        self.reference_manager = ReferenceManager(self.bibtex_service, self.db_service)

        self.reference_manager.tyhjenna_hakusanat()
        self.reference_manager.poista_filtterit()

        self.viite = Reference(
            "John Doe",
            "Title of the book",
            "Best sellers Inc",
            2012
        )

        self.kirjaviite = Book(
            "Author",
            "Otsikko",
            "Julkaisija",
            "Vuosi",
            "ISBN"
        )

        self.kirjaviite2 = Book(
            "Author2",
            "Otsikko2",
            "Julkaisija2",
            "Vuosi2",
            "ISBN2"
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

        self.artikkeliviite2 = Article(
            "Author2",
            "Otsikko2",
            "Julkaisija2",
            "Vuosi2",
            "Lehti2",
            "Vuosikerta2",
            "Numero2",
            "Sivut2"
        )

        self.konferenssiviite = InProceedings(
            "Author",
            "Otsikko",
            "Julkaisija",
            "Vuosi",
            "Kirjan otsikko",
            "Sivut"
        )

        self.konferenssiviite2 = InProceedings(
            "Author2",
            "Otsikko2",
            "Julkaisija2",
            "Vuosi2",
            "Kirjan otsikko2",
            "Sivut2"
        )

    def _lisaa_kaikki_viitteet(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite2)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite2)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite2)

    def _lisaa_kaikki_viitteet_artikkeli_ensin(self):
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite2)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite2)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite2)

    def _lisaa_kaikki_viitteet_konferenssi_ensin(self):
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite2)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite2)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite2)

    def test_get_filtterit(self):
        self.assertEqual(len(self.reference_manager.get_filtterit()), 0)

    def test_lisaa_filtteri_kun_filtteria_ei_viela_lisatty(self):
        self.reference_manager.lisaa_filtteri("filtteri")
        self.assertEqual(self.reference_manager.get_filtterit()[0], "filtteri")

    def test_lisaa_filtteri_kun_filtteri_jo_lisatty(self):
        self.reference_manager.lisaa_filtteri("filtteri")
        self.reference_manager.lisaa_filtteri("filtteri")
        self.assertEqual(len(self.reference_manager.get_filtterit()), 1)

    def test_filtteri_jo_lisatty_kun_filtteri_jo_lisatty(self):
        self.reference_manager.lisaa_filtteri("filtteri")
        self.assertTrue(self.reference_manager.filtteri_jo_lisatty("filtteri"))

    def test_filtteri_jo_lisatty_kun_filtteri_ei_lisatty(self):
        self.reference_manager.lisaa_filtteri("filtterii")
        self.assertFalse(self.reference_manager.filtteri_jo_lisatty("filtteri"))

    def test_poista_filtterit(self):
        self.reference_manager.lisaa_filtteri("filtteri")
        self.reference_manager.poista_filtterit()
        self.assertEqual(len(self.reference_manager.get_filtterit()), 0)

    def test_hae_filtterihakusanoilla_viite_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.reference_manager.lisaa_filtteri("john")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "John Doe")

    def test_hae_filtterihakusanoilla_kirjaviite_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_filtteri("author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")

    def test_hae_filtterihakusanoilla_artikkeliviite_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_filtteri("author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")

    def test_hae_filtterihakusanoilla_konferenssiviite_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_filtteri("author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")

    def test_hae_yhdella_filtterihakusanalla_kaikki_matchaavat_viitteet_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_filtteri("author")
        self.assertEqual(len(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()), 3)
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[1].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[2].get_author(), "Author")

    def test_hae_kahdella_filtterihakusanalla_kaikki_matchaavat_viitteet_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("otsik")
        self.assertEqual(len(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()), 3)
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[1].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[2].get_author(), "Author")

    def test_hae_usealla_filtterihakusanalla_kaikki_matchaavat_viitteet_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite2)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite2)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite2)
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("otsik")
        self.reference_manager.lisaa_filtteri("julk")
        self.reference_manager.lisaa_filtteri("vuo")
        self.assertEqual(len(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()), 6)
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[1].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[2].get_author(), "Author")

    def test_hae_usealla_filtterihakusanalla_kaikki_matchaavat_viitteet_kun_operandi_and_ja_artikkeli_ensin(self):
        self._lisaa_kaikki_viitteet_artikkeli_ensin()
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("otsik")
        self.reference_manager.lisaa_filtteri("julk")
        self.reference_manager.lisaa_filtteri("vuo")
        self.assertEqual(len(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()), 6)
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[0].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[1].get_author(), "Author")
        self.assertEqual(self.reference_manager.hae_filtterihakusanoilla_kun_operandi_and()[2].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_auth_kun_lisatty_yksi_kirjaviite(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_otsikko_kun_lisatty_yksi_kirjaviite(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "otsikko")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "otsikko")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_julkaisija_kun_lisatty_yksi_kirjaviite(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "julkaisija")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "julkaisija")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_vuosi_kun_lisatty_yksi_kirjaviite(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "vuosi")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "vuosi")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_isbn_kun_lisatty_yksi_kirjaviite(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "isbn")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "isbn")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_kun_lisatty_yksi_artikkeliviite(self):
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")[0].get_author(), "Author")

    def test_hae_viitelistasta_hakusanalla_kun_lisatty_yksi_konferenssiviite(self):
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")), 1)
        self.assertEqual(self.reference_manager.hae_viitelistasta_hakusanalla(self.reference_manager.hae_viitteet(), "auth")[0].get_author(), "Author")

    def test_hae_viitelistasta_jossa_yksi_kirjaviite_matchit_hakusanalistalla_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("eiloydy")
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and(self.reference_manager.hae_viitteet(), self.reference_manager.get_filtterit())), 0)

    def test_hae_viitelistasta_jossa_yksi_artikkeliviite_matchit_hakusanalistalla_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("eiloydy")
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and(self.reference_manager.hae_viitteet(), self.reference_manager.get_filtterit())), 0)

    def test_hae_viitelistasta_jossa_yksi_konferenssiviite_matchit_hakusanalistalla_kun_operandi_and(self):
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_filtteri("author")
        self.reference_manager.lisaa_filtteri("eiloydy")
        self.assertEqual(len(self.reference_manager.hae_viitelistasta_matchit_hakusanalistalla_kun_operandi_and(self.reference_manager.hae_viitteet(), self.reference_manager.get_filtterit())), 0)

    def test_hae_viitteen_indeksi_viitelistassa_toimii_oikein(self):
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite)
        self.reference_manager.lisaa_uusi_viite(self.kirjaviite2)
        self.reference_manager.lisaa_uusi_viite(self.artikkeliviite2)
        self.reference_manager.lisaa_uusi_viite(self.konferenssiviite2)
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitelistassa(self.kirjaviite, self.reference_manager.hae_viitteet()), 0)
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitelistassa(self.artikkeliviite, self.reference_manager.hae_viitteet()), 1)
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitelistassa(self.konferenssiviite, self.reference_manager.hae_viitteet()), 2)

    def test_hae_kahdella_hakusanalla_kun_operandi_and_kun_lisatty_kaikki_viitteet_kirjaviite_ensin(self):
        self._lisaa_kaikki_viitteet()
        self.reference_manager.lisaa_hakusana("auth")
        self.reference_manager.lisaa_hakusana("otsi")
        self.assertEqual(len(self.reference_manager.hae_hakusanoilla_kun_operandi_and()), 6)

    def test_hae_kolmella_hakusanalla_kun_operandi_and_kun_lisatty_kaikki_viitteet_kirjaviite_ensin(self):
        self._lisaa_kaikki_viitteet()
        self.reference_manager.lisaa_hakusana("auth")
        self.reference_manager.lisaa_hakusana("otsi")
        self.reference_manager.lisaa_hakusana("julk")
        self.assertEqual(len(self.reference_manager.hae_hakusanoilla_kun_operandi_and()), 6)

    def test_hae_kolmella_hakusanalla_kun_operandi_and_kun_lisatty_kaikki_viitteet_kirjaviite_ensin_ja_ei_matcheja(self):
        self._lisaa_kaikki_viitteet()
        self.reference_manager.lisaa_hakusana("auth")
        self.reference_manager.lisaa_hakusana("otsi")
        self.reference_manager.lisaa_hakusana("eiloydy")
        self.assertEqual(len(self.reference_manager.hae_hakusanoilla_kun_operandi_and()), 0)

    def test_poista_hakusana_kun_hakusanaa_ei_viela_lisatty(self):
        self.assertFalse(self.reference_manager.poista_hakusana("auth"))

    def test_poista_hakusana_kun_hakusanaa_jo_lisatty(self):
        self.reference_manager.lisaa_hakusana("auth")
        self.assertTrue(self.reference_manager.poista_hakusana("auth"))

    """
    def test_lisaa_operandi(self):
        self.reference_manager.lisaa_operandi("operandi")
        self.assertEqual(len(self.reference_manager.get_operandit()), 1)
    """

    def test_get_operandi(self):
        self.assertEqual(self.reference_manager.get_operandi(), "AND")

    def test_lisaa_hakusana(self):
        self.reference_manager.lisaa_hakusana("hakusana")
        self.assertEqual(len(self.reference_manager.get_hakusanat()), 1)

    def test_tyhjenna_hakusanat(self):
        self.reference_manager.lisaa_hakusana("hakusana")
        self.reference_manager.tyhjenna_hakusanat()
        self.assertEqual(len(self.reference_manager.get_hakusanat()), 0)

    def test_hakusana_jo_lisatty(self):
        self.reference_manager.lisaa_hakusana("hakusana")
        self.assertFalse(self.reference_manager.lisaa_hakusana("hakusana"))

    def test_hae_viite_doi(self):
        self.reference_manager.hae_viite_doi("doi")
        self.bibtex_service.hae_bibtex_doilla.assert_called_once()

    def test_hae_viitteen_indeksi_viitteissa(self):
        self._lisaa_kaikki_viitteet()
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitteissa(self.kirjaviite), 0)
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitteissa(self.artikkeliviite), 1)
        self.assertEqual(self.reference_manager.hae_viitteen_indeksi_viitteissa(self.konferenssiviite), 2)
           
    def test_vie_viitelista_tiedostoon(self):
        #self._lisaa_kaikki_viitteet()
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.reference_manager.vie_viitelista_tiedostoon(self.reference_manager.hae_viitteet(), "tiedostonimi")
        self.bibtex_service.vie_viite_temporary_databaseen.assert_called_once()
        self.bibtex_service.tyhjenna_temporary_bibdatabase.assert_called_once()
        self.bibtex_service.vie_temporary_databasen_viitelista_tiedostoon.assert_called_once()

    def test_hae_viitteista_avainsanalla(self):
        self.reference_manager.lisaa_uusi_viite(self.viite)
        self.assertEqual(len(self.reference_manager.hae_viitteista_avainsanalla("john")), 1)

    def test_poista_viite_databasesta(self):
        self._lisaa_kaikki_viitteet()
        self.assertTrue(self.reference_manager.poista_viite_databasesta(self.kirjaviite))
        self.db_service.poista_viite_databasesta.assert_called_once()

    def test_poista_viite_viitteen_numeron_mukaan(self):
        self._lisaa_kaikki_viitteet()
        self.assertTrue(self.reference_manager.poista_viite_viitteen_numeron_mukaan(0))

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
