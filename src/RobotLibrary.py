# tämän tiedston nimen tulee olla juuri tässä muodossa
# pylint: disable=invalid-name

from ui.ui import UI
from stub_io import StubIO
from services.stub_reference_manager import StubReferenceManager
from entities.reference import Reference

class RobotLibrary:
    '''komennot robot framework -testejä varten'''
    def __init__(self):
        self._io = StubIO()
        self._reference_manager = StubReferenceManager()
        self._ui = UI(self._io, self._reference_manager)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        for output in self._io.outputs:
            if value in output:
                return
        raise AssertionError(
            f"Output \"{value}\" is not in {str(self._io.outputs)}"
        )

    def run_application(self):
        self._ui.run()

    def add_new_reference(self, *args):
        '''argumentit kirjoittaja, otsikko, julkaisija, vuosi, isbn'''
        viite = Reference(args[0], args[1], args[2], args[3], args[4])
        self._reference_manager.lisaa_uusi_viite(viite)
