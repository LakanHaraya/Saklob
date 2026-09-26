class Prompt:
    def __init__(self, sesyon):
        self.sesyon = sesyon

    def buuin(self):
        return f"{self.sesyon.konteksto}> "