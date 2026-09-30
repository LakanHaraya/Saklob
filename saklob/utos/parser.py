from saklob.tulong.kahilingan import HelpRequest

class ParsedCommand:
    def __init__(self, pangalan, argumento=None):
        self.pangalan = pangalan
        self.argumento = argumento or []

class Parser:
    def parse(self, teksto):
        mga_salita = teksto.strip().split()

        if not mga_salita:
            return None

        if mga_salita[0] == "?":
            if len(mga_salita) == 1:
                return HelpRequest(HelpRequest.GENERAL)

            return HelpRequest(
                HelpRequest.COMMAND,
                mga_salita[1]
            )

        if mga_salita[-1] == "?":
            return HelpRequest(
                HelpRequest.ARGUMENT,
                " ".join(mga_salita[:-1])
            )

        pangalan = mga_salita[0]
        argumento = mga_salita[1:]

        return ParsedCommand(pangalan, argumento)