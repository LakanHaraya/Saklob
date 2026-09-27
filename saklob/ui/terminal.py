from saklob.makina.makina import Makina
from saklob.makina.sesyon import Sesyon
from saklob.ui.prompt import Prompt
from saklob.ui.input_buffer import InputBuffer
from saklob.config.kumpigurasyon import Kumpigurasyon


class Terminal:
    def __init__(self, locale=None):
        self.sesyon = Sesyon()

        self.config = Kumpigurasyon()
        self.config.ikarga()
        self.config.simulan()

        self.makina = Makina(
            self.sesyon,
            locale=locale,
            config=self.config
        )

        self.prompt = Prompt(self.sesyon)

        self.input_buffer = InputBuffer()

    def run(self):
        print(self.makina.mensahe("banner"))
        print(self.makina.mensahe("exit_hint"))
        print()

        while self.makina.tumatakbo:
            teksto = input(self.prompt.buuin())

            if not self.input_buffer.tanggapin(teksto):
                print(
                    self.makina.mensahe(
                        "input_too_long",
                        maximum=self.input_buffer.maximum
                    )
                )
                continue

            self.makina.isagawa(teksto)