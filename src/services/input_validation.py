import re

class InputValidation:
    ''' Syötteiden validointi. '''

    @classmethod
    def isbn(cls, input_string:str) -> bool:
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

        # hyväksy tilanne, jossa ei ole annettu ISBN:ää ollenkaan
        if input_string == "":
            return True

        # tarkista, että eri osissa on jokaisessa oikea määrä numeroita
        # lisäksi tarkista osien erottimein oikeellisuus
        regexp = "^(97(8|9)[- ]?)?\\d{1,5}[- ]?\\d{1,7}[- ]?\\d{1,6}[- ]?\\d$"
        if not re.match(regexp, input_string):
            return False

        # tarkista lisäksi, että numeroita on yhteensä oikea määrä
        pelkat_numerot = [char for char in input_string if char in "0123456789"]
        return len(pelkat_numerot) in [10, 13]

    @classmethod
    def year(cls, input_string:str) -> bool:
        '''
        Tarkistetaan Year-syötteen oikellisuutta. Syöte on muotoa 4 lukua.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^\\d{4}$", input_string) is not None

    @classmethod
    def name(cls, input_string:str) -> bool:
        '''
        Tarkistetaan Author-syöte. Syöte on muotoa "Sukunimi, Etunimi; Sukunimi, Etunimi..."
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        # hyväksytään kaikki merkkijonot

        if input_string == "":
            return True
        return re.match("^([A-ZÄÖ][a-zäö]+, [A-ZÄÖ][a-zäö]+)", input_string) is not None

    @classmethod
    def menu_command(cls, input_string:str) -> bool:
        '''
        Tarkistetaan Menu-syöte. Syöte on luku 0 - 5.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''

        return re.match("^[0-9]$", input_string) is not None


    @classmethod
    def hakumenu_command(cls, input_string:str) -> bool:
        '''
        Tarkistetaan Hakumenu-syöte. Syöte on luku 0 - 5 tai kirjain x.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^(0|1|2|3|4|5|x)$", input_string) is not None

    @classmethod
    def not_empty(cls, input_string:str) -> bool:
        return re.match(".+", input_string) is not None

    @classmethod
    def article_number(cls, input_string:str) -> bool:
        # hyväksy tyhjä syöte sekä kaikki pelkistä numeroista koostuvat syötteet
        if input_string == "":
            return True
        return re.match("^\d+$", input_string)

    @classmethod
    def pages(cls, input_string:str) -> bool:
        # hyväksy tyhjä syöte sekä kaikki muotoa a-b olevat syötteet, missä kokonaisluvut a<=b
        if input_string == "":
            return True
        match = re.match("^(\d+)-(\d+)$", input_string)
        if not match:
            return False
        start_page, end_page = match.groups()
        return int(start_page) <= int(end_page)

    @classmethod
    def doi(cls, input_string:str) -> bool:
        # tarkista, että DOI on oikeassa formaatissa
        regexp = r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b'
        if not re.match(regexp, input_string):
            return False
        return True

    @classmethod
    def hakusana(cls, input_string:str) -> bool:
        return True

    @classmethod
    def error_message(cls, error_type:str="tyhja") -> str:
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
            "numero": "Lehden numeron on oltava kokonaisluku tai tyhjä.",
            "tyhja": "Virheellinen syöte."
        }

        return virheilmoitukset[error_type]

    #@classmethod
    def korjaa_doi_nimi(cls, tekija):
        pattern_nimet = re.compile(r";|and")
        nimet = re.split(pattern_nimet, tekija)
        pattern_nimi = re.compile(r"(\w+)(\s+\w+)?\s+(\w+)")

        formatted_names = []
        for nimi in nimet:
            formatted_name = re.sub(pattern_nimi, r"\3, \1\2", nimi)
            formatted_names.append(formatted_name)
        formatted_str = ';'.join(formatted_names)
        formatted_str = re.sub(r"\s+;", ";", formatted_str)
        return formatted_str