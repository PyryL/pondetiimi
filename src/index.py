from services.konsoli_io import KonsoliIO
from services.sqldb_service import SqldbService
from services.bibtex_service import BibtexService
from services.reference_manager import ReferenceManager
from ui.ui import UI
#from RobotLibrary import RobotLibrary

def main():
    konsoli_io = KonsoliIO()
    bibtex_service = BibtexService()
    db_service = SqldbService()
    reference_manager = ReferenceManager(bibtex_service, db_service)

    user_interface = UI(konsoli_io, reference_manager)
    user_interface.run()

    #a = RobotLibrary()
    #a.run_application()

if __name__ == "__main__":
    main()
