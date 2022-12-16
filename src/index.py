from services.konsoli_io import KonsoliIO
from services.sqldb_service import SqldbService
from services.bibtex_service import BibtexService
from services.reference_manager import ReferenceManager
from ui.ui import UI

def main():
    konsoli_io = KonsoliIO()
    bibtex_service = BibtexService()
    db_service = SqldbService("references.db")
    reference_manager = ReferenceManager(bibtex_service, db_service)

    user_interface = UI(konsoli_io, reference_manager)
    user_interface.run()

if __name__ == "__main__":
    main()
