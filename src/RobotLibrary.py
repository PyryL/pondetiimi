from ui.ui import UI
from stub_io import StubIO
from services.stub_reference_manager import StubReferenceManager
from entities.reference import Reference

"""
#tee reference_repository-luokka ja importtaa
from services.reference_manager import ReferenceManager
from services.sqldb_service import SqldbService
from services.bibtex_service import BibtexService
"""



class RobotLibrary:
    def __init__(self):
        self._io = StubIO()
        # alusta reference_repository
        # bibtex_service = BibtexService()
        # db_service = SqldbService()
        #self._reference_manager = ReferenceManager(bibtex_service, db_service)
        self._reference_manager = StubReferenceManager()
        self._ui = UI(self._io, self._reference_manager)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        for output in self._io.outputs:
            if value in output:
                return
        raise AssertionError(
            f"Output \"{value}\" is not in {str(outputs)}"
        )

    def run_application(self):
        self._ui.run()

    def add_new_reference(self, kirjoittaja, otsikko, julkaisija, vuosi, isbn):
        viite = Reference(kirjoittaja, otsikko, julkaisija, vuosi, isbn)
        self._reference_manager.lisaa_uusi_viite(viite)
