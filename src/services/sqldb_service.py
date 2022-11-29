import sqlite3
from entities.reference import Reference

class SqldbService:
    def vie_viite_databaseen(self, viite):
        # Tarkistus, onko viite jo db:ssä puuttuu.
        #Tarkistus suoritettu ref_manager metodissa lisaa_uusi_viite()?
        db = sqlite3.connect("test.db")
        db.isolation_level = None
        
        values=(viite.get_author(), viite.get_title(), viite.get_publisher(), viite.get_year(), viite.get_isbn())

        db.execute("INSERT INTO test (author, title, publisher, year, isbn) VALUES (?, ?, ?, ?, ?)",values)
        db.commit()
        db.close()

        # Tarpeellinen?
        """
        title = viite["title"]
        author = viite["author"]
        return f"Book {title} by {author} saved."
        """

    def hae_viitteet_databasesta(self):
        viitteet = []

        db = sqlite3.connect("test.db")
        db.isolation_level = None
        all = db.execute("SELECT * FROM test")

        for row in all:
            viite = Reference(row[1], row[2], row[3], row[4], row[5])
            viitteet.append(viite)

        db.close()

        return viitteet
