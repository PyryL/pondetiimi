import sqlite3
from entities.reference import Reference

class SqldbService:
    '''
    Tietokanta toiminnot.
    '''
    def vie_viite_databaseen(self, viite):
        # Tarkistus, onko viite jo db:ssä puuttuu.
        #Tarkistus suoritettu ref_manager metodissa lisaa_uusi_viite()?
        database = sqlite3.connect("test.db")
        database.isolation_level = None

        values = (
            viite.get_author(),
            viite.get_title(),
            viite.get_publisher(),
            viite.get_year(),
            viite.get_isbn()
        )

        insert_sql="INSERT INTO test (author, title, publisher, year, isbn) VALUES (?, ?, ?, ?, ?)"
        database.execute(insert_sql, values)
        database.commit()
        database.close()

    def hae_viitteet_databasesta(self):
        viitteet = []

        database = sqlite3.connect("test.db")
        database.isolation_level = None
        all_references = database.execute("SELECT * FROM test")

        for row in all_references:
            viite = Reference(row[1], row[2], row[3], row[4], row[5])
            viitteet.append(viite)

        database.close()

        return viitteet

    def pois_viite_databasesta(self, viite):
        database = sqlite3.connect("test.db")
        database.isolation_level = None
        database.execute("DELETE FROM test WHERE id_number = ?", (viite.get_id(),))
        database.commit()
        database.close()
