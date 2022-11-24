from services.konsoli_io import KonsoliIO
from services.reference_service import References
from ui.ui import UI


def main():
    io = KonsoliIO()
    references = References()
    ui = UI(io, references)
    ui.run()

if __name__ == "__main__":
    main()
