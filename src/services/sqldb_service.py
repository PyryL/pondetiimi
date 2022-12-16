import sqlite3
from entities.book import Book
from entities.article import Article
from entities.inproceedings import InProceedings

class SqldbService:
    '''
    Tietokanta toiminnot.
    '''
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def luo_uusi_viitetaulu(self):
        """ Uusi doi-tietokanta:
        database = sqlite3.connect("doi_references.db")
        database.isolation_level = None

        database.execute('''CREATE TABLE VIITTEET
         (ID,
         AUTHOR,
         TITLE,
         PUBLISHER,
         YEAR,
         ISBN,
         JOURNAL,
         VOLUME,
         NUMBER,
         BOOKTITLE,
         PAGES,
         ENTRYTYPE,
         DOI
         );''')

        database.commit()
        database.close()
        """
        database = sqlite3.connect(self.dbfile)
        database.isolation_level = None

        database.execute('''CREATE TABLE VIITTEET
         (ID,
         AUTHOR,
         TITLE,
         PUBLISHER,
         YEAR,
         ISBN,
         JOURNAL,
         VOLUME,
         NUMBER,
         BOOKTITLE,
         PAGES,
         ENTRYTYPE
         );''')

        database.commit()
        database.close()

    def vie_viite_databaseen(self, viite):
        ''' Tarkistus, onko viite jo db:ssä puuttuu.'''
        database = sqlite3.connect(self.dbfile)
        database.isolation_level = None

        values = 0

        if viite.get_entrytype() == "book":
            values = (
            viite.get_id(),
            viite.get_author(),
            viite.get_title(),
            viite.get_publisher(),
            viite.get_year(),
            viite.get_isbn(),
            "", "", "", "", "",
            viite.get_entrytype()
            )
        elif viite.get_entrytype() == "article":
            values = (
            viite.get_id(),
            viite.get_author(),
            viite.get_title(),
            viite.get_publisher(),
            viite.get_year(),
            "",
            viite.get_journal(),
            viite.get_volume(),
            viite.get_number(),
            "",
            viite.get_pages(),
            viite.get_entrytype()
            )
        elif viite.get_entrytype() == "inproceedings":
            values = (
            viite.get_id(),
            viite.get_author(),
            viite.get_title(),
            viite.get_publisher(),
            viite.get_year(),
            "", "", "", "",
            viite.get_booktitle(),
            viite.get_pages(),
            viite.get_entrytype()
            )
        
        insert_sql = (
            "INSERT INTO VIITTEET "
            "(ID, AUTHOR, TITLE, PUBLISHER, YEAR, ISBN, JOURNAL, "
            "VOLUME, NUMBER, BOOKTITLE, PAGES, ENTRYTYPE) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        )

        database.execute(insert_sql, values)
        database.commit()
        database.close()

    def hae_viitteet_databasesta(self):
        viitteet = []

        database = sqlite3.connect(self.dbfile)

        database.isolation_level = None
        all_references = database.execute("SELECT * FROM VIITTEET")

        for row in all_references:
            viite = 0

            if row[11] == "book":
                viite = Book(row[1], row[2], row[3], row[4], row[5])
            elif row[11] == "article":
                viite = Article(row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[10])
            elif row[11] == "inproceedings":
                viite = InProceedings(row[1], row[2], row[3], row[4], row[9], row[10])

            viitteet.append(viite)

        database.close()

        return viitteet

    def poista_viitetaulu_databasesta(self):
        database = sqlite3.connect(self.dbfile)
        database.isolation_level = None

        database.execute("DROP table VIITTEET")

        database.commit()
        database.close()
