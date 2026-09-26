from saklob.makina.konteksto import Konteksto

class Sesyon:
    def __init__(self):
        self.gumagamit = "salig"
        self.sistema = None
        self.node = None
        self.konteksto = Konteksto("saklob")
        self.mode = "normal"

    def pasok(self, pangalan):
        self.konteksto = Konteksto(
            pangalan,
            self.konteksto
        )

    def balik(self):
        if self.konteksto.magulang is not None:
            self.konteksto = self.konteksto.magulang