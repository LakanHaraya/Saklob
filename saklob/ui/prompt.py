class Prompt:
    def __init__(self, sesyon):
        self.sesyon = sesyon

    def buuin(self):
        if self.sesyon.mode == "kumpigurasyon":
            return "saklob(kumpig)# "

        return f"{self.sesyon.konteksto}> "