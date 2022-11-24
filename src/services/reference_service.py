class References:

    def _new_entry(self, io, bibtex_service):
        author = io.lue("Kirjoittaja:")
        title = io.lue("Otsikko:")
        publisher = io.lue("Julkaisija:")
        year = io.lue("Vuosi:")
        isbn = io.lue("ISBN:")
        viite = {"author": author,
                 "title": title,
                 "publisher": publisher,
                 "year": year,
                 "isbn": isbn,
                 "ID": "SukunimiVuosi",
                 "ENTRYTYPE": "book"}
        bibtex_service.uusi_viite(viite)

    def _export_file(self, io, bibtex_service):
        tiedostonimi = io.lue("Anna tiedostonimi:")
        bibtex_service.vie_viitteet(tiedostonimi)
        print(f"Tiedosto {tiedostonimi}.bib luotu")
