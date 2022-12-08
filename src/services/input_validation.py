import re

class InputValidation:
    ''' Syötteiden validointi. '''

    @classmethod
    def isbn(cls, input_string):
        # Otettu pois käytöstä viitteiden lisäämisen helpottamiseksi.
        return True
        '''
        Tarkistetaan ISBN-syötteen oikellisuutta. ISBN syöte on 13 tai 10 merkkiä pitkä ja
        on oikeassa formaatissa.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        # tämä ei ole kaiken kattava ratkaisu, mutta toimii useimmissa tapauksissa
        # laatimisessa käytetty virallista ohjetta täällä:
        # https://www.isbn-international.org/sites/default/files/ISBN-k%C3%A4ytt%C3%B6opas%20%28Finnish%20translation%20of%20seventh%20edition%29_0.pdf

        # tarkista syotteen muoto, eli numeroiden määrä eri osissa
        if not input_string:
            return True
        regexp = "^(97(8|9)[- ]?)?\\d{1,5}[- ]?\\d{1,7}[- ]?\\d{1,6}[- ]?\\d$"
        if not re.match(regexp, input_string):
            return False

        pelkat_numerot = input_string.replace("-", "").replace(" ", "")
        return len(pelkat_numerot) in [10, 13]

    @classmethod
    def year(cls, input_string):
        '''
        Tarkistetaan Year-syötteen oikellisuutta. Syöte on muotoa 4 lukua.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^\\d{4}$", input_string) is not None

    @classmethod
    def name(cls, input_string):
        '''
        Tarkistetaan Author-syöte. Syöte on muotoa "Sukunimi, Etunimi; Sukunimi, Etunimi..."
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        # hyväksytään kaikki merkkijonot
        return re.match("^([A-ZÄÖ][a-zäö]+, [A-ZÄÖ][a-zäö]+;? ?)+$", input_string) is not None

    @classmethod
    def menu_command(cls, input_string):
        '''
        Tarkistetaan Menu-syöte. Syöte on luku 0 - 5.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
<<<<<<< HEAD
        return re.match("^(0|1|2|3|4|5)$", input_string) is not None

    @classmethod
    def hakumenu_command(cls, input_string):
        '''
        Tarkistetaan Hakumenu-syöte. Syöte on luku 0 - 5 tai kirjain x.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^(0|1|2|3|4|5|x)$", input_string) is not None

=======
        return re.match("^(01|02|03|1|2|3|4)$", input_string) is not None
>>>>>>> main

    @classmethod
    def not_empty(cls, input_string):
        return re.match(".+", input_string) is not None

    @classmethod
    def error_message(self, error_type="tyhja"):
        '''
        Palauttaa virheilmoituksen annetun virhetypin mukaan.
        Args:
            error_type (String): virhetyyppi
        Returns
            (String): virheilmoitus
        '''
        virheilmoitukset = {
            "nimi": "Syötteen on oltava muotoa 'Sukunimi, Etunimi; Sukunimi, Etunimi...'",
            "otsikko": "Otsikko ei voi olla tyhjä.",
            "vuosi": "Vuoden on oltava muotoa 'YYYY'.",
            "julkaisija": "Julkaisija ei voi olla tyhjä.",
            "isbn": "ISBN on oltava muotoa 'XXXXXXXXXXXXXXXX' tai tyhjä.",
            "sivut": "Sivujen on oltava muotoa 'XX-XX' tai tyhjä.",
            "lehti": "Lehden nimi ei voi olla tyhjä.",
            "vuosikerta": "Vuosikerran on oltava kokonaisluku.",
            "numero": "Lehden numeron on oltava kokonaisluku.",
            "tyhja": "Virheellinen syöte."
        }

        return virheilmoitukset[error_type]
