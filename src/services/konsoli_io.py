from enum import Enum
from termcolor import colored

class Varit(Enum):
    '''
    Käyttöliittymän värikartta.
    Arvot ovat termcolor-kirjaston käyttämiä avainsanoja.
    '''
    OLETUS = None
    HARMAA = "grey"
    PUNAINEN = "red"
    VIHREA = "green"
    KELTAINEN = "yellow"
    SININEN = "blue"
    VIOLETTI = "magenta"
    TURKOOSI = "cyan"

class KonsoliIO:
    '''
    Käyttäjäsyötteiden hallinointi.
    '''
    def lue(self, teksti = ""):
        return input(teksti)

    def tulosta(self, teksti,
                vari = Varit.OLETUS,
                tummennus = False,
                alleviivaus = False,
                lopetus = None):
        attributes = []
        if tummennus:
            attributes.append("bold")
        if alleviivaus:
            attributes.append("underline")

        varitetty = colored(teksti, vari.value, attrs=attributes)
        print(varitetty, end=lopetus)
