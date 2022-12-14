class StubIO:
    '''konsoli_io-luokan kaltainen toiminnallisuus testausta varten'''
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def add_input(self, inpt):
        self.inputs.append(inpt)

    def lue(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return "lopeta"

    def tulosta(self, output, *args, **kwargs): # pylint: disable=unused-argument
        ''' *args ja **kwargs täytyy olla, vaikka niitä ei käytetä,
        koska konsoli_io-luokalla on muitakin argumentteja

        muulla kuin tulostuksen tekstillä ei ole testien kannalta väliä'''

        self.outputs.append(output)
