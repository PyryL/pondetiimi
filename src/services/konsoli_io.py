from enum import Enum
from termcolor import colored

class Varit(Enum):
    # kaikki nämä arvot ovat termcolor-kirjaston käyttämiä
    # avainsanoja, joten niitä ei voi muuttaa
    oletus = None
    harmaa = "grey"
    punainen = "red"
    vihrea = "green"
    keltainen = "yellow"
    sininen = "blue"
    violetti = "magenta"
    turkoosi = "cyan"

class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)

    def tulosta(self, teksti, vari = Varit.oletus, tummennus = False, alleviivaus = False, lopetus = None):
        attributes = []
        if tummennus: attributes.append("bold")
        if alleviivaus: attributes.append("underline")

        varitetty = colored(teksti, vari.value, attrs=attributes)
        print(varitetty, end=lopetus)
