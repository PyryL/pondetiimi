class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def add_input(self, input):
        self.inputs.append(input)

    def lue(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return "lopeta"

    def tulosta(self, output):
        self.outputs.append(output)
