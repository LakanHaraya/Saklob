from saklob.makina.makina import Makina
from saklob.makina.sesyon import Sesyon
from saklob.ui.prompt import Prompt


class Terminal:
    def __init__(self, locale=None):
        self.sesyon = Sesyon()
        self.makina = Makina(
            self.sesyon,
            locale=locale
        )
        self.prompt = Prompt(self.sesyon)

    def run(self):
        print(self.makina.mensahe("banner"))
        print(self.makina.mensahe("exit_hint"))
        print()

        while self.makina.tumatakbo:
            teksto = input(self.prompt.buuin())
            self.makina.isagawa(teksto)