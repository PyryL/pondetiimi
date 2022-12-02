import re

class InputValidation:
    @classmethod
    def isbn(cls, input_string):
        # tämä ei ole kaiken kattava ratkaisu, mutta toimii useimmissa tapauksissa
        # laatimisessa käytetty virallista ohjetta täällä:
        # https://www.isbn-international.org/sites/default/files/ISBN-k%C3%A4ytt%C3%B6opas%20%28Finnish%20translation%20of%20seventh%20edition%29_0.pdf
        regexp = "^97(8|9)[- ]?\d{1,5}[- ]?\d{1,7}[- ]?\d{1,6}[- ]?\d$"
        return re.match(regexp, input_string)

    @classmethod
    def year(cls, input_string):
        # hyväksytään kaikki nelinumeroiset luvut
        return re.match("^\d{4}$", input_string)

    @classmethod
    def menu_command(cls, input_string):
        return re.match("^(0|1|2|3|4)$", input_string)

    @classmethod
    def not_empty(cls, input_string):
        return re.match(".+", input_string)
