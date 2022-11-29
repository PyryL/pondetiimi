from services.konsoli_io import KonsoliIO
from services.sqldb_service import SqldbService
from services.bibtex_service import BibtexService
from services.reference_manager import ReferenceManager
from ui.ui import UI

def main():
    io = KonsoliIO()
    bibtex_service = BibtexService()
    db_service = SqldbService()
    reference_manager = ReferenceManager(bibtex_service, db_service)

    ui = UI(io, reference_manager)
    ui.run()

if __name__ == "__main__":
    main()
