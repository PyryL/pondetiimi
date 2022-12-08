class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def add_input(self, inpt):
        self.inputs.append(inpt)

    def lue(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return "lopeta"

    def tulosta(self, output,
                vari = None,
                tummennus = False,
                alleviivaus = False,
                lopetus = None):
        # muulla kuin tulostuksen tekstillä ei ole testien kannalta väliä
        self.outputs.append(output)
