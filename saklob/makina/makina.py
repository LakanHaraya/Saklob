from saklob.utos.rehistro import Rehistro
from saklob.utos.core import lumikha_core_utos
from saklob.utos.parser import Parser
from saklob.tulong.tulong import Tulong
from saklob.tulong.kahilingan import HelpRequest
from saklob.makina.konteksto_rehistro import KontekstoRehistro

from saklob.wika.setting import DEFAULT_LOCALE
from saklob.wika.tagapamahala import TagapamahalaWika

# from saklob.lndh import irehistro_lndh


class Makina:
    def __init__(self, sesyon, locale=None):
        self.sesyon = sesyon
        self.tumatakbo = True

        self.rehistro = Rehistro()
        self.parser = Parser()

        self.locale = locale or DEFAULT_LOCALE

        self.tagapamahala_wika = TagapamahalaWika(
            self.locale
        )

        self.bokabularyo = (
            self.tagapamahala_wika.buuin_bokabularyo()
        )

        self.konteksto_rehistro = KontekstoRehistro()
        # irehistro_lndh(self.konteksto_rehistro)

        self.tulong = Tulong(self)

        for utos in lumikha_core_utos(self):
            self.rehistro.idagdag(utos)

    def isagawa(self, teksto):
        command = self.parser.parse(teksto)

        if command is None:
            return

        if isinstance(command, HelpRequest):
            self.tulong.iproseso(command)
            return

        utos = self.kunin_utos(command.pangalan)

        if utos is None:
            print(
                self.mensahe(
                    "unknown_command",
                    pangalan=command.pangalan
                )
            )
            return

        konteksto = str(self.sesyon.konteksto)

        if not utos.magagamit_sa(konteksto):
            print(
                self.mensahe(
                    "command_unavailable",
                    pangalan=command.pangalan,
                    konteksto=konteksto
                )
            )
            return

        utos.isagawa(command.argumento)

    def kunin_utos(self, pangalan):
        command_id = self.bokabularyo.kunin_id(pangalan)

        if command_id is None:
            return None

        return self.rehistro.kunin_id(command_id)

    def kunin_utos_metadata(self, command_id):
        return self.tagapamahala_wika.kunin_utos(command_id)

    def mensahe(self, susi, **halaga):
        teksto = self.tagapamahala_wika.kunin_mensahe(
            susi
        )

        if teksto is None:
            raise KeyError(
                f"Message key not found: {susi}"
            )

        if halaga:
            return teksto.format(**halaga)

        return teksto