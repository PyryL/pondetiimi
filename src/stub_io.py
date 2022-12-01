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

    def tulosta(self, output):
        self.outputs.append(output)
